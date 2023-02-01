from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse
from noticias_db import noticia, leer_noticia, noticia_todas, actualizar, eliminar

""" Se crea la clase que contendra las rutas y los metodos http
    para realizar el crud se utuliza BaseHTTPRequestHandler que es el manejador
    de rutas
"""


class noticias(BaseHTTPRequestHandler):
    """ se setean las cabeceras """
    def set_header(self):
        self.send_response(200)
        self.send_header('content-Type', 'application/json')
        self.end_headers()

    def do_POST(self):
        """ seteamos las cabeceras """
        self.set_header()
        """ Parseamos la cedena con urlparse """
        if self.path == '/noticia/':
            # se lee el contenido y se reserva memoria para almacenas el
            # contenido
            self.data = self.rfile.read(int(self.headers['Content-Length']))
            # Se convierte a un diccionario python
            datos = json.loads(self.data)
            noticia(datos['titulo'], datos['descripcion'], datos['usuario_id'])
            self.wfile.write(json.dumps({"msg": "dato creado"}).encode())
            return BaseHTTPRequestHandler(self)
        else:
            self.send_response(404)

    def do_GET(self):
        """ seteamos las cabeceras """
        self.set_header()
        """ Parseamos la cedena con urlparse """
        parseada = urlparse(self.path)
        print(parseada.path)
        if parseada.path == "/noticia/id/":
            print(parseada.query)
        #    self.data = self.rfile.read(int(self.headers['Content-Length']))
            una_noticia = leer_noticia(list(parseada.query))
            #new =  [*leer[0]]
            dic = {
                'id': una_noticia[0][0],
                'titulo': una_noticia[0][1],
                'desc': una_noticia[0][2],
                'usuario_id': una_noticia[0][3]
                }
            self.wfile.write(json.dumps(dic).encode())
            return BaseHTTPRequestHandler(self)

        elif parseada.path == "/noticia/deta/":
            lista = []
            todo = noticia_todas()
            """ se crea el diccionario manualmente """
            for p in range(len(todo)-1):
                dic = {}
                dic['id'] = todo[p][0]
                dic['titulo'] = todo[p][1]
                dic['desc'] = todo[p][2]
                dic['usuario_id'] = todo[p][3]
                lista.append(dic)
            self.wfile.write(json.dumps(lista).encode())
            return BaseHTTPRequestHandler(self)
        else:
            return self.send_response(404)

    def do_PUT(self):
        """ seteamos las cabeceras """
        self.set_header()
        """ Parseamos la cedena con urlparse """
        parseada = urlparse(self.path)
        print(parseada.path)
        if parseada.path == "/noticia/":
            # se lee el contenido y se reserva memoria para almacenas el
            # contenido
            self.data = self.rfile.read(int(self.headers['Content-Length']))
            # Se convierte a un diccionario python
            datos = json.loads(self.data)
            actual = actualizar(**datos)
            self.wfile.write(json.dumps({"msg": actual}).encode())
            return BaseHTTPRequestHandler(self)
        else:
            return self.send_response(404)

    def do_DELETE(self):
        """ seteamos las cabeceras """
        self.set_header()
        """ Parseamos la cedena con urlparse """
        parseada = urlparse(self.path)
        if parseada.path == "/noticia/id/":
            valor_id = parseada.query
            print(valor_id)
            borrar = eliminar(valor_id)
            self.wfile.write(json.dumps({"msg": borrar}).encode())
            return BaseHTTPRequestHandler(self)
        else:
            return self.send_response(404)


httpd = HTTPServer(('localhost', 8000), noticias)
httpd.serve_forever()
