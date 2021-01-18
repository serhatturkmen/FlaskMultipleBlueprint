from flask import Blueprint

apiBlueprint = Blueprint("apiController", __name__)

from . import apiHomeController
