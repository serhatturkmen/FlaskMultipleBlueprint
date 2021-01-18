from flask import Flask, render_template
from controller import controllerBlueprint

from apicontroller import apiBlueprint

app = Flask(__name__)


app.config['SECRET_KEY'] = 'hjo2tasdfa_DoT_07pyws_!88#'

app.register_blueprint(controllerBlueprint, url_prefix="/")

app.register_blueprint(apiBlueprint, url_prefix="/api/v1.0/8897/")

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8808, debug=True)
 