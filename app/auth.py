from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


# LOGIN/REGISTER PAGE
@auth.route('/login-register', methods=['GET', 'POST'])
def loginRegister():
  return render_template('login_register.html',
    section=request.args.get('section'),
    error=request.args.get('error'))
#include error arg in url if user data not found -> see html login form