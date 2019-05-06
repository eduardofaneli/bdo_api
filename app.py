from flask import Flask, Blueprint
from flask_cors import CORS
from log import log
from restplus import api
from endpoints.boss import ns_boss

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

def initializa_app(app):
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['ERROR_404_HELP'] = False

    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)

    api.add_namespace(ns_boss)

    app.register_blueprint(blueprint)    

def main():
    initializa_app(app)
    log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))

    app.run()

if __name__ == "__main__":
    main()