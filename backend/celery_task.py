import os
from datetime import datetime, timedelta

from celery.schedules import crontab
from jinja2 import Template
from weasyprint import HTML

from application.mail_config import send_email
from application.utils import rating_avg
from app import celery, cache
from application.models import *

@celery.on_after_finalize.connect
def setup_intervalTask(sender, **kwargs):
    sender.add_periodic_task(
        10,
        # crontab(hour=24, minute=0),
        reminder.s(),
        name="Generate Report",
    ),
    sender.add_periodic_task(
        30,
        # crontab(hour=0, minute=0, day_of_month='1'),
        send_stats.s(),
        name="Send Creator Stats Monthly",
    )

@celery.task()
def reminder():
    users = Users.query.all()
    for user in users:
        if (datetime.now() - user.last_login_at) > timedelta(hours=23):
            continue
        with open(r"templates/reminder.html") as file:
            msg_template = Template(file.read())
            send_email(to=user.email, subject="Reminder", message=msg_template.render(username=user.username))

    return "Reminder Sent"

@celery.task()
def send_stats():
    users = Users.query.all()
    creators = [user for user in users if 'creator' in user.roles]
    month = datetime.now().strftime("%m")
    month_name = datetime.now().strftime("%B")
    year = datetime.now().strftime("%Y")
    if not os.path.exists('static/monthly_reports/'):
        os.mkdir(path='static/monthly_reports/')
    for creator in creators:
        # total_albums, total_songs, song_ratings, songs_released in past month
        creator_stats = []
        albums_objs = Albums.query.filter_by(creator_id=creator.id).all()
        total_albums = len(albums_objs)
        total_songs = 0
        songs_released = 0
        average_rating = 0
        if albums_objs:
            avg_ratings = []
            for album in albums_objs:
                for song in album.album_songs:
                    avg_ratings.append(
                        rating_avg(
                            SongRatings.query.with_entities(SongRatings.rating)
                            .filter_by(song_id=song.id)
                            .all()
                        )
                    )
                    if (datetime.now() - song.release_date) < timedelta(days=30):
                        songs_released += 1
                    total_songs += 1
            if avg_ratings:
                average_rating = sum(avg_ratings) / len(avg_ratings)
            else:
                average_rating = 0
        pdf_path = f"static/monthly_reports/monthly_report_{str(creator.username)}_{month}_{year}.pdf"

        with open(r"templates/stats.html") as file:
            pdf_template = Template(file.read())

        with open(r"templates/monthly_report.html") as file:
            msg_template = Template(file.read())
        
        pdf = HTML(string=pdf_template.render(username = creator.username, total_albums = total_albums, total_songs = total_songs, average_rating = average_rating, songs_released = songs_released, month = month_name, year = year)).write_pdf(pdf_path)
        send_email(to=creator.email, subject="Monthly Report", attachment=pdf_path, message=msg_template.render(username=creator.username))
    return "Stats Sent"