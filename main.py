from flask import Flask
from flask import render_template
from flask import request


import forms

app = Flask(__name__)
# app = Flask(__name__,template_folder ='prueba')

@app.route('/',methods=['GET','POST'])
def index():
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		print comment_form.username.data
		print comment_form.email.data
		print comment_form.comment.data

	title = "Curso flask"
	return render_template('index.html',title=title,form=comment_form)

if __name__ == '__main__':
	app.run(debug = True,port = 8000)