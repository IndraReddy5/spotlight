import csv
import os
from datetime import datetime, timedelta

from celery.schedules import crontab
from jinja2 import Template
from weasyprint import HTML

from application.mail_config import send_email
from app import celery, cache
from models import *

@celery.on_after_finalize.connect
def setup_intervalTask(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=0, minute=0),
        reminder.s(),
        name="Generate Report",
    ),
    # sender.add_periodic_task(
    #     crontab(hour=0, minute=0),
    #     send_stats.s(),
    #     name="Clear Cache",
    # )

@celery.task()
def reminder():
    users = Users.query.all()
    for user in users:
        if (datetime.now() - user.last_login_at) > timedelta(hours=23):
            continue

    with open(r"../templates/reminder.html") as file:
        msg_template = Template(file.read())
        send_email(to=user.email, subject="Reminder", template=msg_template.render(name=user.username))

    return "Reminder Sent"