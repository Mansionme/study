#!/usr/bin/env python
import os
from app import create_app, db
from flask_script import Server, Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app('default')
# print(app.config)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command("runserver",  Server(host="0.0.0.0", port=9000))

if __name__ == '__main__':
    manager.run()


#flask db init
#flask db migrate
#flask db upgrade