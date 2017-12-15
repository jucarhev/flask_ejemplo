from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

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
			validators.required(message="Requiere usuario")
		])