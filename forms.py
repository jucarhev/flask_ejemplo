from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import HiddenField

def length_honeypot(form,field):
	if len(field.data) > 0:
		raise validators.ValidationError("El campo debe estar vacio")

class CommentForm(Form):
	username = StringField('username',
		[
			validators.length(min=4,max=35,message="Ingrese usuario valido"),
			validators.required(message="Requiere usuario")
		])

	email = EmailField('Correro electronico',
		[
			validators.Email()
		])

	comment = TextField('Comentario',
		[
			validators.required(message="Requiere usuario"),
		])
	honeypot = HiddenField("",[length_honeypot])

class FormLogin(Form):
	username = StringField('username',
		[
			validators.length(min=4,max=35,message="Ingrese usuario valido"),
			validators.required(message="Requiere usuario")
		])
	password = PasswordField('password',
		[
			validators.length(min=4,max=35,message="Ingrese passwrod valido"),
			validators.required(message="Requiere password")
		])
	honeypot = HiddenField("",[length_honeypot])
		