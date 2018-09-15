from app import create_app, db
from flask_script import Manager, Server

# Creating app instance
app = create_app('development')

# instantiate manager class
manager =Manager(app)

# command to launch application server
manager.add_command('server', Server)

@manager.command
def test():
    """
    run tests
    """
    import unittest
    tests =unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# manager shell decorator to create shell context
@manager.shell
def make_shell_context():
    """
    shell context function allowing passing of properties into our shell
    :return:
    """
    return dict(app=app, db=db, User=User,)
