La presente API tiene una estructura hexagonal si no me equivoco, a continuación se explica a grandes razgos como funciona la API:

En la primera capa tenemos el archivo main.py que es el que se encarga de hacer que se ejecute la api, despues tenemos los requirements.txt que nos ayudaran a que nuestra api funcione pues tiene las librerias necesarias para que el proyecto funcione por ejemplo en la nube-.

En la segunda capa o carpeta tenemos "app" en la que tenemos el init y el config, el config para la configuracion si es entorno de desarrollo o produccion y el init en el que tenemos el create app y nuestro blueprint

En la tercera capa "api" tenemos el init que contiene nuestros endpoints, asi mismo tenemos las capas de controller y endpoints, esta vez no me dio tiempo de poner los dtos.

En el controller tenemos el metodo post y en el endpoint tenemos nuestra funcion que nos ayuda a realizar el trabajo.

# Como ejecutarlo:

El primer paso para ejecutarlo será abrir el prompt de anaconda y en el prompt escribir la ruta al codigo de main.py y posteriormente ejecutar el método de la siguiente manera "python main.py", con eso deberá ser suficiente para que el programa empiece a funcionar, deben tener en cuenta las variables de entorno ENV = dev, en este caso omití un paso fundamental que es poner __env = os.getenv("ENV") or "dev" en el main.py y fué reemplazado con un __env = "dev" para que no tuviesen problemas al ejecutarlo, de cualquier manera adjunto algunas imagenes en el archivo de github

Para ejecutar el metodo POST se deba realizar lo siguiente, estoy usando postman para visualizar el json final por lo que para visualizar el resultado de dicha api en el postman deberan elegir el metodo post, despues deberan poner el siguiente endpoint: http://127.0.0.1:8088/v1/entity/NER  

En body, en raw, deberan elegir json en el menu desplegable de la derecha e insertar el siguiente json: 

{"oraciones":["Apple está buscando comprar una startup del Reino Unido por mil millones de dólares",
            "San Francisco considera prohibir los robots de entrega en la acera"]}

posteriormente solo deberan hacer la solicitud y deberá enviarles el siguiente resultado:

{
    "resultado": [
        {
            "oracion": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares",
            "entidades": {
                "Apple": "ORG",
                "Reino Unido": "LOC"
            }
        },
        {
            "oracion": "San Francisco considera prohibir los robots de entrega en la acera",
            "entidades": {
                "San Francisco": "LOC"
            }
        }
    ]
}
