from flask import Flask

# Indica que este sera el modulo(archivo) principal de nuestra aplicación
app = Flask(__name__)

# Asignar varias rutas a una vista
@app.route('/')
@app.route('/index')
def index():
    return "Página de Inicio"

# Enviar datos a travez de las rutas con <>
# string @app.route('/hello/<string:name>')
# int @app.route('/hello/<itn:name>')
# float """"
# path """"   (Tiene un manejo mas amplio que el string)
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def hello(name = None, age = None):
    if name == None and age == None:
        return '<h1>Hola Mundo</h1>'
    elif age == None:
        return f'Hola, {name}'
    else:
        return f'Hola, {name}! Tu edad es: {age}'