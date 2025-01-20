from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/login')
def login ():
    return render_template('admin/login.html')
@app.route('/')
def ini ():
    return render_template('usuario/index.html')

@app.route('/mujer')
def mujer ():
    return render_template('usuario/mujer.html')

@app.route('/hombre')
def hombre ():
    return render_template('usuario/hombre.html')

@app.route('/niño')
def niño ():
    return render_template('usuario/niño.html')

@app.route('/novedades')
def novedades ():
    return render_template('usuario/novedades.html')

@app.route('/ofertas')
def ofertas ():
    return render_template('usuario/ofertas.html')

if __name__ == '__main__':
    app.run(debug=True)
