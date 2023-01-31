import mysql.connector

def conect():
    conn = mysql.connector.connect(
                user='root',
                port='3306',
                password='root',
                host='127.0.0.1',
                database='bd',
            )
    if conn.is_connected:
        return(conn)
    else:
        print("error de coneccion")