'''

1 clase -> Response Model


@app.post('/person/new/', response_model=PersonOut)
def create_person(
        person : Person = Body(...)
):
    return person

aqui vimos algo nuevo, y es en la path operation decoration el key response_model, lo que estamos diciendo con eso
es que vamos a devolver como respuesta el modelo que tenemos despues del = , es decir, el modelo
PersonOut, esto lo hicimos porque agregamos un nuevo atributo a la clase Person, donde el usuario nos enviaba un request
body con la contraseña, pero nosotros le devolviamos la contraseña, eso esta mal, la contraseña no se le envia al cliente,
la contraseña no se almacena en texto plano, por lo tanto lo que hicimos es crear un nuevo modelo llamado PersonOut y le quitamos
el campo de la clave, y lo devolvemos

documentacion oficial

https://fastapi.tiangolo.com/tutorial/response-model/


Para realiza una aplicación segura debemos tener dos temas en cuenta a la hora de la creación de la contraseña

La contraseña no se le envía al cliente
La contraseña no se almacena en texto plano

Response Model:
Es un atributo de nuestro path operation el cual es llamado desde nuestro Path Operation Decorator, el cual es utilizado para evitar el filtrado de información sensible


en este definiremos un nuevo modelo que será el que se usará para el Response, por ejemplo si una persona realiza un POST con su contraseña en él, no podemos enviar
la contraseña de regreso en el Response, esto sería un problema de seguridad bastante fuerte

El response model, es una utilidad de seguridad importante ya que evita que se filtre información que puede estar almacenada en nuestros modelos.
Su importancia radica en que al momento de que tu tengas X objeto (diccionario) que devuelvas, lo que hará FAST API será simplemente solo devolver los datos indicados en response_model.


2 clase -> Mejorando la calidad del código: eliminando líneas duplicadas

como se puede observar, lo que hicimos en la clase pasada, nosotros generamos duplicidad en el codigo, tomamos el modelo Person,
copie todo lo que estaba adentro tal cual como estaba en otro modelo, esto no deberia pasar jamas, esto se soluciona con las funciones
ya que nos sirven para evitar duplicidad, pero en este caso en particular no, lo vamos hacer con la herencia

3 clase status Code Personalizados -> https
    los codigo de estado, que le indica al cliente que paso con la respuesta de esta petición, en esa
    respuesta siempre va a venir un status code.

            ----status Code----

            100 -> quiere decir que la respuesta http es de informacion(information)
            200 -> significa que todo esta bien, que la respuesta es correcta
                    -- 201 -> quiere decir que algo se creo, por ejemplo, si estamos en una path operation
                              que envia una peticion de tipo post desde el cliente al servidor y en esa
                              peticion creamos un usuario y guardamos el usuario en la bd, responderiamos
                              201, para indicarle al cliente que se creo correctamente ese usuaio
                    -- 204 -> queire decir, que no encontro el contenido, que no hay ninguna respuesta para
                              el usuario
            300  -> redirecciones, queire decir decir que cada vez que respondamos con un 300 esa respuesta
                    va a rederigir a otra URL de nuestro servicio para ponder contestar al cleinte ahora si
                    con un 200, que significa que todo salio bien  o con otro status code
            400 -> client - error, error del cliente
                    --- 404 -> que halla tratado de acceder a un endpoint que no existe (not exist)
                    --- 422 -> este es un validecion error, quiere decir que el cliente nos envia un dato
                               que no estaba en el formato que nosotros esperabamos, por ejemplo, nosotros
                               decimos que esperabamos un string de 20 caracteres y el nos envia solo 1, eso
                               esta mal
            500 -> la mas peligrosa, internal server error , esto sucede cuando tenemos un error en el codigo
                    por lo tanto tenemos que ir a la aplicacion a corregirlo

4 clase Formularios
    cuando estes construyendo tu aplicación te vas a dar cuenta que hay casos en los cuales los datos
    que vas a transmitir a traves desde tu APi no lo vas hacer desde un parametro, por ejemplo un query parameter
    o path parameter o ni siquiera en forma de request body , hay veces en la  que tu aplicacion que ya sabe como esta
    compuesta porque lo aprendiste en el curso de introducción al desarrollo backend que tiene un frond y un
    backend, hay veces en la que el usuario que esta viendo su aplicación va estar en el frontend, va a estar en
    la interfaz , por ejemplo en este frontend, en esa interfaz , el usuario va a tener un formulario

    la forma de entrada de datos de un formulario es una entrada de datos avanzada prodriamos decirle y es diferente
    a como se entra datos a traves de path parameters, query parameters y request body

    --como hacer para que tu API pueda resivir datos del frontend y particularmente de los formularios--
        -para tarbajar con formularios, necesitamos una libreria extra
        pip install python-multipart

    Nota: recodar que response_model = es la respuesta que le vamos a dar al usuario, la funcion path operation
    function debe ser parecida al nombre que nosotros ponemos en el path


    @app.post(
    path= '/login/',
    response_model = LoginOut,
    status_code= status.HTTP_200_OK
    )
    def login(username : str = Form):
        pass

    Form que se tiene que importar de FastApi nos dice para indicar que un parametro dentro de una path
    operation function viene de un formulario

    Nota: siempre leer los errores del final hasta el principio

    Importante, como es el ingreso de de fuente de datos
    ya aprendiste como ingresar datos a tu API, mediante
    1. --> path parameter
    2 ---> query parameter
    3 ---> request body
    4--> formularios

    existen mas fuentes de datos exoticos que podemos explorar para cuando te sean utiles

    5. -----> Cookies
    6. ---> Header Parameters

                        -------- Definiciones --------

    Una parte de una petición o respuesta HTTP que contiene datos sobre la petición o la respuesta, como el
    formato, quien la hizo, el contenido, etc…

    recordar que un Header es simplemente una parte de una petición o respuesta HTTP que contiene
    datos sobre tal cosa, es decir, sobre tal petición y respuesta por ejemplo quien la hizo, en que
    fecha se hizo, en que formato viene, en clase anterior por ejemplo en la documentación interactiva
    vimos una, vimos el header que nos dice a nosotros en que formato esta la respuesta, vemos que normalmente
    cuando estamos trabajando con una API el formato es apliccation/json pero vimos tambien que hay
    otro aplication/x-www-form... que signifca que el formato para la entrada de datos es de formulario, asi como
    existen esos headers, existen otros , esta como por ejemplo el user agent, ese es el que nos dice quien
    esta entrando a nuestra web y quien esta usando nuestra APPI

    Una cookie es simplemente, una pieza de codigo muy pequeña que un servidor mete en tu computadora, cuando
    estas  nevagando en la web, es decir, cada vez que entras a una web que esta trabajando con cookies, ese
    sitio web esta incrustando codigo en tu computadora para poder almacenar una cierta cantidad de datos
    que van hacer utiles despues para la navegación, por ejemplo, para loguearte en el sitio web, sin volver a poner
    la contraseña otra vez

    user_agent = nos dice quien esta entrando a nuestra web
    el funcionamiento de las cookies a veces capturan la informacion de navegación que tienes para poder
    darle datos al creador del sito web que te la ha puesto en tu computadora

-- clase 8:

        Tipos de entradas de datos en FastAPI:

    Path Parameters -> URL y obligatorios
    Query Parameters -> URL y opcionales
    Request Body -> JSON
    Formularios -> Campos en el frontend
    Headers -> Cabeceras HTTP que pueden ser de cliente a servidor y viceversa
    Cookies -> Almacenan información
    Files -> Archivos como imágenes, audio, vídeo, etc.
    Para manejar archivos con FastAPI necesitamos de las clases ‘File’ y ‘Upload File’.

    Upload file tiene 3 parámetros:

    Filename -> Nombre del archivo
    Content_Type -> Tipo de archivo
    File -> El archivo en sí mismo

    FastApi utiliza dos clases para trabajar con archivo

    @app.post(
    path = '/post-image/'
    )
    def post_image(
        image : UploadFile = File()
    ):
        pass

    UploadFile -> una para definir el tipo de la variable o del parametro
    File () -> y otra para definir el valor que va a contener esa variable o parametro

    viendo la documentación en la cabecera
    multipart/form-data, lo que quiere decir esto es que estamos trabajando con archivos

    Nota: si yo divido la cantidad en bytes de un archivo en 1024 eso me va a dar la cantidad
    en kb

Video 10 -> HTTPException
    Que pasa si un usuario de tu aplicación trata de acceder a un dato de tu aplicacion que no existe
    o que tal si un usuario de tu aplicacion trata de acceder a un dato de tu aplicacion que no tiene
    permiso, para poder solucionar este tipo de situaciones FastApi nos proporciona
    HTTPException

    HTTPException nos va a servir para casos que por ejemplo tenemos un error, generalemente van hacer para
    errores de clientes, como que el usuario intenta acceder  a un dato que no existe o intenta
    acceder a un dato por lo cual no tiene permiso, es decir a errores, que tienen un status code de la
    clase de los 400, ahi vamos a usar httpException para poder hacer que nuestras path operation esten
    mas completas

------------------------------- Video 11 -> comenzando a ordenar nuestra documentación: etiquetas-----------------
etiquetas : nos van a permitir dar un orden a la documentación interactiva
nos vamos a ir a cada uno de las path operations que traten  como persona y las voy a clasificar, es decir,
les voy a poner etiquetas, mediante un nuevo parametro del path operation decorater

@app.post(path='/person/new/', response_model=PersonOut, status_code=status.HTTP_201_CREATED, tags = ['Persons'])

como se puede observar agrego un nuevo parametro llamado tags que recibe una lista y el nombre de la etiqueta
en este caso le puse Persons, ahora me voy a ir a clasificar todos los endpoint que tengan que ver con
persons y agregar ese mismo parametro


---- Nombre y descripcioón de una path operation
el docstring es la documentación de las funciones, todo esto viene desde base
el docstring permite documentar las funciones, es una buena practica con python

prototipo recomendado por el profesor

    - Titulo
    - Descripcion
    - Parametros
    - Resultado

summary = 'Create Person in the app'
summary permite colocarle un titulo personalizado a las funciones, por default swager Ui le coloca
el nombre que le damos a las funciones, pero eso se puede cambiar con esto


@app.post(path='/person/new/', response_model=PersonOut, status_code=status.HTTP_201_CREATED, tags = ['Persons'], summary = 'Create Person in the app')

------- Deprecar una path operation

Mientras nuestra API este viva, mientras nuestra aplicación este funcionando mas de una vez vamos a mejorar
la misma, a medida que nosotros mejoramos nuestra Api, la hacemos mejor, le agregamos funcionalidades hay algunas
path operations que nosotros vamos a mantener pero hay otras que vamos a dejar sin efecto, este proceso de dejar
sin efecto una pieza de codigo , se le dice en jerga popular de los programadores, deprecar, deprecar una pieza de
codigo sucede por varias cuestiones

1.Se encuentra un mejor método mas eficiente para resolver un problema que nosotros ya tenemos. Lo que
hacemos no es eliminar dicho método si no la dejamos sin efecto.
Para aprovechar el código posteriormente si lo requerimos nuevamente.

explicacion:
tenemos una path operation con un metodo  que resuelve un problema, pero resulta que en el camino, es decir
en la evolución de la empresa y de nuestra aplicación, encontramos otro metodo que es mejor, que resuelve mejor
el problema , en este caso en vez de eliminar la path operation, la deprecamos, es decir la dejamos sin efecto

Porque no la eliminamos?
porque puede que la necesitemos en otro momento, quien sabe si este nuevo metodo al final no funciona
y tenemos que volver al pasado, en ese caso, aprovechamos el codigo de nuevo



2.Una funcionalidad diferente de nuestro código a la que ya tenemos definidos.

explicacion:

vamos hacer exactamente el mismo proceso pero de una manera distinta, vamos a encontrar
un camino mas distinto para hacer el proceso, en este caso deprecamos nuestro primer codigo


3.Cuando se esta realizando una refactorización profunda del código, debido a que no tiene las mejores practicas,
se define deprecar las path operation que se tienen por otras nuevas y se reemplazan.

no se eliminan

Nota: Siempre es
mejor mantener el código que modificarlo desde cero salvo rara excepciones

no quiere decir que el codigo que hizo la otra persona esta mal, vale mas la pena pararse y leer el codigo, entenderlo
y mantenerlo que cambiarlo desde cero
'''