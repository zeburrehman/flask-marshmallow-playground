import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy_utils import create_database, database_exists

from app import create_app, db
from app.blueprints import blueprint

app = create_app(os.getenv('config_env') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

@manager.command
def create_db():
    db_url = app.config["SQLALCHEMY_DATABASE_URI"]
    if not database_exists(db_url):
        create_database(db_url)
    return ""

@manager.command
def run():
    app.run(debug=True, port=5005)

if __name__ == "__main__":
    manager.run()