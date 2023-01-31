from coneccion import conect

def noticia(titulo, descripcion, usuario):
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
    print(id)
    conn = conect()
    cursor = conn.cursor()
    sql = """ SELECT * FROM `database`.noticias where id = %s """
    #valores = (id)
    cursor.execute(sql, id)
    dato = cursor.fetchall()
    conn.commit()
    conn.close
    return dato

def noticia_todas():
    conn = conect()
    cursor = conn.cursor()
    sql = """ SELECT * FROM `database`.noticias """
    cursor.execute(sql)
    todo = cursor.fetchall()
    conn.commit()
    conn.close
    return todo

def actualizar(**datos):
    conn = conect()
    cursor = conn.cursor()
    sql = """ UPDATE `database`.noticias SET titulo=%s descripcion=%s usuario_id=%s"""
