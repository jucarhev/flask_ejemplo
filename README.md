# Curso Flask CodigoFacilito

## Anotaciones
```
@app.before_request
def before_request():
	if 'username' not in session and request.endopint not in ['index']:
	return redirect('/login')

@app.after_request
def after_request(response):
	return response
```

### varable global
```
g.test = 'test1'
```

## Dependencias
pip install Flask-SQLAlchemy
pip install wtForm
pip install flask_wtf