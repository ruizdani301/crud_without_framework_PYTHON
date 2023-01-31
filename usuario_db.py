from coneccion import conect
import hashlib


def encriptar(contraseña):
    h = hashlib.new("sha512",bytes(contraseña, 'utf-8'))
    return h.hexdigest()
   

def crear(nombre, correo, contraseña):
    conn = conect()
    cursor = conn.cursor()
    sql = """INSERT INTO `database`.usuario(nombre, correo, password)
             VALUES(%s, %s, %s);
          """
    valores = (nombre, correo, encriptar(contraseña))
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()

def loguin(correo, contraseña):
    conn = conect()
    cursor = conn.cursor()
    sql = """SELECT id, nombre, correo, password
             FROM `database`.usuario where correo = %s and password = %s;
          """
    valores = (correo, encriptar(contraseña))
    cursor.execute(sql, valores)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data