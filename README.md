# CRUD CON PYTHON CRUDO (SIN FRAMEWORK)

Esta es la resolución de una prueba técnica la cual consiste
en desarrollar un crud pero solamente con python sin usar framework; 
Se encontraron algunos desafios y ayudo a comprender lo mucho que 
un framework contribuye con el ahorro de tiempo y esfuerzo, permitiendo 
destinar nuestro tiempo a resolver desafios mas relevantes durante el desarrollo
web.


El backend de un framework se encarga de ayudar a los desarrolladores a construir una interfaz intuitiva y bien estructurada. Crea formularios y páginas, y controla la base de datos y las peticiones HTTP. Básicamente, lo que un framework backend web hace, es que el proceso de desarrollo sea más cómodo.

# RETO

** Crear una API que permita la creación de usurios,
* datos
- Nombre
- email
- contraseña
 ** Crear una API que sirva de loguin (autenticación) para los usuarios del punto anterior.
  - La respuesta debe ser si las credenciales son o no correctas.
  - Para la creación solo necesita titulo y descripción.
 
 ** Crear una API que permita adicionar comentarios a las noticias creadas.

## Archivos

### coneccion.py :

Contiene la coneccion ala base de datos.

### api.py y api_noticias.py

Tiene la clase que contendra los metodos http y manejadores de ruta para la ejecución del crud

### usuario_db.py y noticias_db.py

Contiene los metodos que ejecutan las consultas para crear, actualizar, obtener, eliminar.
