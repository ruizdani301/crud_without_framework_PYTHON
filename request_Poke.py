import requests
import pprint
import json
import mysql.connector
from coneccion import conect
"""
resultado = requests.get('https://jsonplaceholder.typicode.com/todos')
#pprint.pprint (resultado.json())
data = (resultado.json())
#pprint.pprint(json.loads(resultado.content))
#print (len(data))
for item in range(len(data)):
   user_id = data[item]['id']
   completed= data[item]['completed']
   title = data[item]['title']
   
   se realiza conexion ala base de datos
   conn = mysql.connector.connect(
            user='root',
            port='3306',
            password='root',
            host='127.0.0.1',
            database='bd',
        )
   if conn.is_connected():
        cursor = conn.cursor()

        sql = "INSERT INTO cliente (user_id, completed, title) VALUES(%s, %s, %s)"
        cursor.execute(sql, (user_id, completed, title))
        print ("resgitro ok")
        conn.commit()

conn.close()
"""
def delete():

     conn = conect()
    
     cursor = conn.cursor()
     sql = "SELECT completed FROM cliente where user_id = 4"
     asd = cursor.execute(sql)
     linea = cursor.fetchall()
     print(asd)
     print(sql)
     print (linea)
     conn.commit()
     conn.close()


delete()  
        
#if __name__ == '_main_':
     

#value =( str(resultado.content))
#pprint.pprint(value)
#newclass = json.loads(value('unicode_escape'))
#print(type(newclass))

#for value in resultado:
#    value = resultado.content.abilities[0].ability.name
#    print(value)