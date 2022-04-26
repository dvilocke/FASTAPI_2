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
'''