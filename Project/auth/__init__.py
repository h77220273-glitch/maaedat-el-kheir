from flask import Blueprint
bp = Blueprint("auth",__name__,template_folder='templates')
from Project.auth import views