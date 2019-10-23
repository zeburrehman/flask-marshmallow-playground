from flask_script import Manager

from app import create_app
from app.blueprints import blueprint

app = create_app()
app.register_blueprint(blueprint)

manager = Manager(app)

@manager.command
def run():
    app.run(debug=True, port=5005)

if __name__ == "__main__":
    manager.run()