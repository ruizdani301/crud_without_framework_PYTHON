from coneccion import conect

""" Se crean las conecciones a base de datos y
    se ejecutan los query que solicita api_noticias.py
"""


def noticia(titulo, descripcion, usuario):
    """ Metodo que realiza la inserción de datos"""
    conn = conect()
    cursor = conn.cursor()
    sql = """INSERT INTO `database`.noticias(titulo, descripcion,usuario_id)
            VALUES(%s, %s, %s);
            """
    valores = (titulo, descripcion, usuario)
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()


def leer_noticia(id):
    """ Metodo que realizada la solicitud de datos por id"""
    print(id)
    conn = conect()
    cursor = conn.cursor()
    sql = """ SELECT * FROM `database`.noticias where id = %s """
    cursor.execute(sql, id)
    dato = cursor.fetchall()
    conn.commit()
    conn.close
    return dato


def noticia_todas():
    """ Metodo que realizada la solicitud de todos los datos """
    conn = conect()
    cursor = conn.cursor()
    sql = """ SELECT * FROM `database`.noticias """
    cursor.execute(sql)
    todo = cursor.fetchall()
    conn.commit()
    conn.close
    return todo


def actualizar(**datos):
    """ Metodo que realizada la actualización de datos """
    print(datos["titulo"])
    conn = conect()
    cursor = conn.cursor()
    sql = """ UPDATE `database`.noticias SET titulo=%s, descripcion=%s,
              usuario_id=%s
              where id=%s
            """
    valores = (datos["titulo"], datos["descripcion"], datos["usuario_id"],
               datos["id"])
    cursor.execute(sql, (valores))
    conn.commit()
    conn.close()
    return("exitoso")


def eliminar(valor_id):
    """ Metodo que realizada la eliminacion por id """
    print("entro al db")
    conn = conect()
    cursor = conn.cursor()
    sql = """ DELETE FROM `database`.noticias where id=%s """
    cursor.execute(sql, list(valor_id))
    conn.commit()
    conn.close()
    return("eliminación exitosa")
