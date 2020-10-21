# -*- coding: utf-8 -*-
from flask_script import Manager, Server
from app import app
from app.models import db, User, Order

manager = Manager(app)
manager.add_command("server", Server())

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Order=Order)

if __name__ == "__main__":
    manager.run()
