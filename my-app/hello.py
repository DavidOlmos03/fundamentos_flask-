from flask import Flask, render_template
from datetime import datetime

# Indica que este sera el modulo(archivo) principal de nuestra aplicación
app = Flask(__name__)


# Crear mis propios filtros
# Filtros personalizados
# El add_template_filter se utiliza para agregar esta función a los filtros disponibles en las plantillas

# forma 1
# @app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

# forma 2
app.add_template_filter(today, 'today')

# Funciones personalizadas
# forma 1
# @app.add_template_global
def repeat(s,n):
    return s*n
# forma 2
app.add_template_global(repeat, 'repeat')

# Asignar varias rutas a una vista
@app.route('/')
@app.route('/index')
def index():
    # Enviar datos al template con render_template de flask
    name = 'David'
    # name = None
    friends = ['David','Juan','Ana','Sara']
    date = datetime.now()
    return render_template(
        'index.html', 
        name = name, 
        friends = friends, 
        # asi se haria sin el filtro
        # date = today(date)
        # Así se hace con el filtro
        date = date
        # aqui tambien puedo enviar funciones como por ejemplo 
        # repeat = repeat
        )




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
    

# Se utiliza escape !!!! para evitar ataques (como ataque de inyecciones), con esto lo que se ingrese en la url se ejecuta como texto plano
from markupsafe import escape
@app.route('/code/<path:code>')
def code(code):
    return f'{escape(code)}'