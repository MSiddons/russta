from datetime import datetime
from flask import render_template, session, redirect, url_for, request
from . import main
from .forms import LoginForm
from .. import db
from ..models import User

################################################################################
#                                  Home page.                                  #
################################################################################

@main.route('/')
def home(): 
    return render_template('index.html')


################################################################################
#                                Admin w/login.                                #
################################################################################

@main.route('/admin', methods = ['POST', 'GET'])
def admin():
    if not session.get('logged_in'):
        return render_template('login.html', form = LoginForm())	
    else:
        return render_template('admin.html')

@main.route('/login', methods=['POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        password = User.query.filter_by(password=form.name.data).first()
        # if (user == 'test' and password == 'test')
        #     session['logged_in'] = True
        #     return redirect('admin')
        # else:
        session['logged_in'] = False
        ### log
        return render_template('403.html')
		
@main.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

