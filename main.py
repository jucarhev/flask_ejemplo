from flask import Flask
from flask import render_template
from flask import request

import json

from flask import g

from flask import flash

from flask import redirect
from flask import url_for

from flask import session

from flask import make_response

# proteccion
from flask_wtf import CSRFProtect

import forms

from models import db
from models import User

from config import DevelopmentConfig

app = Flask(__name__)
# app = Flask(__name__,template_folder ='prueba')

app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

@app.before_request
def before_request():
	if 'username' not in session and request.endpoint in ['comment']:
		return redirect(url_for('login'))
	elif 'username' in session and request.endpoint in ['login','create']:
		return redirect(url_for('index'))

@app.after_request
def after_request(response):
	return response

@app.route('/login',methods=['GET','POST'])
def login():
	loginform = forms.FormLogin(request.form)
	if request.method == 'POST' and loginform.validate():
		username = loginform.username.data
		password = loginform.password.data

		user = User.query.filter_by(username=username).first()
		if user is not None and user.verify_password(password):
			success_messages = "Bienvenido {}".format(username)
			flash(success_messages)
			session['username'] = username
			return redirect(url_for('index'))
		else:
			error_message = 'usuario no valido'
			flash(error_message)

		session['username'] = loginform.username.data

	title = "Curso flask login"
	return render_template('login.html',title=title,form=loginform)

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
	return redirect(url_for('index'))

@app.route('/cookie')
def cookie():
	response = make_response(render_template('cookie.html'))
	response.set_cookie('custom_cookie','jose')
	return response

@app.route('/')
def index():
	custom_cookie = request.cookies.get('custom_cookie')
	print custom_cookie

	if 'username' in session:
		username = session['username']
		print username
	title = "Curso flask"
	return render_template('index.html',title=title)
	
@app.route('/comment',methods=['GET','POST'])
def comment():
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		print comment_form.username.data
		print comment_form.email.data
		print comment_form.comment.data
	else:
		print "Error en formulario"

	title = "comments"
	return render_template('comment.html',title=title,form=comment_form)

@app.route('/reviews')
def review():
	pass

@app.route('/create',methods=['GET','POST'])
def create():
	createform = forms.FormCreate(request.form)
	if request.method == 'POST' and createform.validate():
		user = User(createform.username.data,
					createform.email.data,
					createform.password.data)

		db.session.add(user)
		db.session.commit()

		success_messages = 'Usurario registrado en la base de datos'
		flash(success_messages)
	return render_template('create.html',title='Create',form=createform)

@app.route('/ajax-login',methods =['POST'])
def ajax_login():
	print request.form['username']
	username = request.form['username']
	response = {'status':200,'username':username,'id':1}
	return json.dumps(response)

if __name__ == '__main__':
	csrf.init_app(app)
	db.init_app(app)
	
	with app.app_context():
		db.create_all()

	app.run(port = 8000)