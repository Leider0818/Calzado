from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def inicio ():
    return render_template('admin/login.html')


@app.route('/ini')
def ini ():
    return render_template('sitio/index.html')

@app.route('/mujer')
def mujer ():
    return render_template('sitio/mujer.html')

@app.route('/hombre')
def hombre ():
    return render_template('sitio/hombre.html')

@app.route('/niño')
def niño ():
    return render_template('sitio/niño.html')

@app.route('/novedades')
def novedades ():
    return render_template('sitio/novedades.html')

@app.route('/ofertas')
def ofertas ():
    return render_template('sitio/ofertas.html')

if __name__ == '__main__':
    app.run(debug=True)