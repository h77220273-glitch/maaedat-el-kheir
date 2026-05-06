from flask import Blueprint

bp = Blueprint('tables',__name__,template_folder='templates')

from Project.tables import views