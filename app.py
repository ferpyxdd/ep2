from flask import Flask,redirect,url_for,render_template,request,flash
from config import ConfiguracionDesarrollo
from model import db, Usuarios

app=Flask(__name__)
app.config.from_object(ConfiguracionDesarrollo)
db.init_app(app)

@app.route('/', methods = ['GET', 'POST'])
def home():
    titulo = 'Bievenido'
    return render_template('login.html',titulo=titulo)

@app.route('/procesar_credenciales', methods = ['POST'])
def procesarCredenciales():
    if request.method=='POST':
        datos = request.form
        ci = datos['txtCi']
        nombre = datos['txtNombre']
        apellido = datos['txtApellido']
        if(ci=="" or nombre=="" or apellido==""):
            flash("Debe completar los campos","alerta")
            return redirect(url_for('home'))
        else:
            comprobar = Usuarios.query.filter_by(nro_cedula = ci, nombres = nombre, apellidos = apellido ).first()
            if comprobar is not None:
                flash("Las credenciales ingresadas son correctas", "correcto")
                return redirect(url_for('principal'))
            else:
                flash("Credenciales incorrectas","alerta")
                return redirect(url_for('home'))

@app.route('/principal')
def principal():
    return render_template('index.html')
    
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)