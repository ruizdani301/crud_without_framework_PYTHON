from http.server import HTTPServer, BaseHTTPRequestHandler 
import json
from usuario_db import crear, loguin

class APIHandler(BaseHTTPRequestHandler): 
    # se setean las cabeceras
    def set_header(self):
        self.send_response(200) 
        self.send_header('Content-Type', 'application/json') 
        self.end_headers()        

    def do_POST(self): 
        self.set_header()

        if self.path == '/usuario/loguin':
            # Toma los datos 
            # rfile.read = lee los datos q vienen en la solicitud
            # (int(self.headers['Content-Length']) me da el tamaño en bytes que 
            #reservara la memoria para almacenar los datos de solicitud.
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            #self.data_string = self.rfile.read(int(90))
            datos = json.loads(self.data_string)
            
            logui = loguin(datos["correo"], datos["password"])
            if len(logui) == 0:
                self.wfile.write(json.dumps({"msg": "credenciales no validas"}).encode()) 
                
            else:
                self.wfile.write(json.dumps({"msg": "credenciales validas"}).encode())

           
            return BaseHTTPRequestHandler(self)
      
             
        if self.path == '/usuario': 
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            datos = json.loads(self.data_string)
            crear(datos["nombre"], datos["correo"], datos["password"])

            self.wfile.write(json.dumps({"msg":"dato creado"}).encode())
            return BaseHTTPRequestHandler(self)
        else: 
            self.send_response(404)

                   
 
httpd = HTTPServer(('localhost', 8000), APIHandler) 
httpd.serve_forever() 