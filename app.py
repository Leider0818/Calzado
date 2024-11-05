from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__, template_folder='templates')

app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = '' 
app.config['MySQL_DB'] = 'calzado'
app.config['MySQL_CURSORCLASS'] = 'DictCursor' 
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index')
def admin():
    return render_template('index.html')

#Funcion de Login
@app.route('/access-login',methods = ["GET","POST"])
def login():

    if request.method == 'POST' and 'KeyUser' in request.form and 'KeyPassword':
        _user = request.form['KeyUser']
        _password = request.form['KeyPassword']

        cur = mysql.connection.cursor()
        cur.execute('select * from usuarios WHERE usuario = %s AND password =%s',(_user,_password,))
        account = cur.fetchone()

        if account :
            session['logeado'] = True
            session['id'] = account['id']

            return render_template("admin.html")
        else:
            return render_template("index.html")
            

    return render_template('login.html', mensaje="usuario incorrecto")


if __name__ == '__main__':
    app.secret_key="leider"
    app.run(debug=True, host='0.0.0.0', port='5000', threaded=True)