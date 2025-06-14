from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask (__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Jinnie320"
app.config['MYSQL_DB']="dbflask"
# app.config['MYSQL_PORT']="3306" //se puede usar en caso de cambio de puerto

mysql = MySQL(app)

#RUTA para probar la coneccion a MYSQL
@app.route('/DBCheck')
def DBChek():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify({'status':'ok','message':'Conexión exitosa'}),200
    except MySQLdb.MySQLError as e:
        return jsonify({'status':'Error','message':str(e)}),500



#RUTA SIMPLE
@app.route('/')
def home():
    return 'Hola, Mundo FLASK!'

#RUTA CON PARAMETRO
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola,'+nombre+'!!!'

#RUTA TRY-CATCH
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8 !!!',404

#RUTA DOBLE
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Soy el mismo recurso del servidor'

#RUTA POST
@app.route('/formulario',methods=['POST'])
def formulario():
    return 'Soy un formulario'



if __name__ == "__main__":
    app.run(port=3000,debug=True)
    