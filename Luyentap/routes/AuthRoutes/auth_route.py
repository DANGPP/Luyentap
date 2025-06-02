from flask import Blueprint
from controllers.AuthControllers  import auth_controller as auCtl

auth_bp = Blueprint('auth_bp',__name__)

@auth_bp.route('/api/login', methods = ['POST'])
def login():
   return auCtl.login_controller()
@auth_bp.route('/api/register', methods = ['POST'])
def register():
   return auCtl.register_controller()