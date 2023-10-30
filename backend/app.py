from create_app import create_app, db
from flask_security import hash_password

app = create_app()
app.app_context().push()
db.create_all()


admin_role = app.security.datastore.find_or_create_role(
    name="admin", description="can create, delete, update shows and venues"
)

sub_role = app.security.datastore.find_or_create_role(
    name="patron", description="can download songs and don't bother about advertisements in between playlists"
)

creator_role = app.security.datastore.find_or_create_role(
    name="creator", description="can create, delete, update Albums and songs in Albums and"
)

end_user_role = app.security.datastore.find_or_create_role(
    name="melophile", description="can create playlists, rate and flag songs"
)

if not app.security.datastore.find_user(email="admin@spotlight.com"):
    app.security.datastore.create_user(
        username="admin",
        email="admin@spotlight.com",
        password=hash_password("light123"),
        roles=[admin_role],
    )

db.session.commit()
if __name__ == "__main__":
    app.run(port=8000)