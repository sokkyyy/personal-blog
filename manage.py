from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Comment,Subscriber
from flask_migrate import Migrate,MigrateCommand

#Creating App Instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role,Comment=Comment, Subscriber=Subscriber)

if __name__ == '__main__':
    manager.run()
