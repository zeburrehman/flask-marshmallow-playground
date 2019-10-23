import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.blueprints import blueprint

app = create_app(os.getenv('config_env') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

@manager.command
def run():
    app.run(debug=True, port=5005)

if __name__ == "__main__":
    manager.run()