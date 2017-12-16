from flask import Flask
from flask import render_template
from flask import request

from flask import flash

from flask import redirect
from flask import url_for

from flask import session

from flask import make_response

# proteccion
from flask_wtf import CSRFProtect

import forms

app = Flask(__name__)
# app = Flask(__name__,template_folder ='prueba')

app.secret_key = "my_secret_key"
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

@app.route('/login',methods=['GET','POST'])
def login():
	loginform = forms.FormLogin(request.form)
	if request.method == 'POST' and loginform.validate():
		session['username'] = loginform.username.data
		username_1 = loginform.username.data
		success_messages = "Bienvenido {}".format(username_1)
		flash(success_messages)

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

if __name__ == '__main__':
	app.run(debug = True,port = 8000)