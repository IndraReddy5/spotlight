from celery import Celery

def create_celery_inst(app):
    celery = Celery(
        app.import_name,
        broker_url = 'redis://localhost:6379/1',
        result_backend = 'redis://localhost:6379/2',
        timezone = 'Asia/Kolkata',
    )
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                print("Starting a new task")
                return self.run(*args, **kwargs)
            
    celery.Task = ContextTask
    return celery