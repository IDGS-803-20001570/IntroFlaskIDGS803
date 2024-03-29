from flask import Flask,render_template,request,Response
from flask_wtf.csrf import CSRFProtect
from flask import redirect

from flask import g

import forms
from flask import flash

app =Flask(__name__)
app.secret_key='esta es la clave secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

#----------------------------- Primero que lanza antes de acceder a cualquier ruta
@app.before_request
def before_request():
    # g.nombre = 'Erick'
    # print('before_request')
    print('antes de cargar')
#-----------------------------------------------------------------------------------
@app.after_request
def after_request(response):
    # print('ultimo')
    if 'Erick' not in g.nombre and request.endpoint not in ['/index']:
        return redirect('index.html')
    return response
# -----------------------------------------------------------------------------------


@app.route("/index")
def index():
    
    #return "<h1>Hola Mundo!!</h1>"
    escuela ="UTL!!!"
    alumnos = ["Mario","Pedro","Luis","Dario"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)
# @app.route("/alumnos")
# def alum():
#     return render_template("alumnos.html")
@app.route("/alumnos",methods=["GET","POST"])
def alum():
    print('dentro de alumnos')
    print('Hola: {}'.format(g.nombre))
    nom=""
    ama=""
    apa=""
    alum_form=forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)

        print("Nombre: {}".format(nom))
        print("apepaterno: {}".format(apa))
        print("apematerno: {}".format(ama))

    return render_template("alumnos.html",form=alum_form,nom=nom,ama=ama,apa=apa)


@app.route("/maestros")
def maes():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<p> <h1>Hola desde Hola!! <br> Mundo</h1> </p>"
@app.route("/user/<string:name>")
def user(name):
    return "<h1>Hola"+name
@app.route("/numero/<int:n>")
def numero(n):
    return "El número es: {}".format(n)
@app.route("/user/<int:id>/<string:name>")
def func(id,name):
    return "ID: {} Nombre: {}".format(id,name)
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "El valor de {} + {} = {}".format(n1,n2,n1+n2)
@app.route("/default")
@app.route("/default/<string:ab>")
def func1(ab="UTL"):
    return "El valor es:"+ab

@app.route("/multiplicar",methods=["GET","POST"])
def mult():
    if request.method == "POST":
        num1= request.form.get("n1")
        num2= request.form.get("n2")
        return "<h1>La multiplicacion es: {} </h1>".format(str(int(num1)*int(num2)))
    else:
        return '''
        <form action="/multiplicar" method="POST">
            <label>N1:</label>
            <input type = "text" name="n1"/>
            <label>N2:</label>
            <input type = "text" name="n2"/>
            
            <input type="submit"/>
        </form>
        '''
@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/resultado",methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        num1= request.form.get("n1")
        num2= request.form.get("n2")
        return "<h1>La multiplicacion es: {} </h1>".format(str(int(num1)*int(num2)))

@app.route("/formulario2")
def formulario2():
    return render_template("formulario2.html")
#Metodo que inicializa la aplicacion del proyecto

if __name__ == "__main__":
    app.run(debug=True)

