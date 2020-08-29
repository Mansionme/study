from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import config
db = SQLAlchemy(use_native_unicode='utf8')

def create_app(config_name):
    app = Flask(__name__)
    try:
        app.config.from_object(config[config_name])
        config[config_name].init_app(app)
    except Exception as e:
        print('config {}'.format(app.config))
        print(e)

    db.init_app(app)
   
    from .department import department as department_blueprint
    app.register_blueprint(department_blueprint, url_prefix='/api/department')

    from .errorhanlder import error as error_blueprint
    app.register_blueprint(error_blueprint)

    from .teachweek import teachweek as teachweek_blueprint
    app.register_blueprint(teachweek_blueprint, url_prefix='/api/teachweek')

    from .teachplan import teachplan as teachplan_blueprint
    app.register_blueprint(teachplan_blueprint, url_prefix='/api/teachplan')

    return app
