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

'''