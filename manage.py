from app import create_app, db
from flask_script import Manager, Server

# Creating app instance
app = create_app('development')

# instantiate manager class
manager =Manager(app)

# command to launch application server
manager.add_command('server', Server)

