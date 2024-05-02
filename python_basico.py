numeros = [1,2,3,4,5,6,7]
saludo = "Hola Mundo"

#TIPOS DE DATOS
#STRING
#INT
#FLOAT
#LIST
#TUPLE
#DICT
#SET
#BOOL

#IMPRIMIR EN PANTALLA
#print(saludo)

#SABER EL TIPO DE DATOS
#print(type(saludo))

#COMENTARIO
# EN UNA LINEA
"""
    EN VARIAS LINEAS
"""

#OPERACIONES CON STRINGS
#CONCATENAR
    #saludo = saludo + " desde Python"
    #print(saludo)

#DUPLICAR
    #print(saludo*3)

#CONTAR => count()
    #print(saludo.count("o"))

#ENCONTRAR => find()
    #print(saludo.find("Mundo"))

#REEMPLAZAR => replace()
    #print(saludo.replace("Mundo","Python"))

#MAYUSCULAS => upper()
    #print(saludo.upper())

#MINUSCULAS => lower()
    #print(saludo.lower())

#CAPITALIZE => capitalize()
    #print(saludo.capitalize())

#DIVIDIR => split()
    #print(saludo.split(" "))
    #print(saludo.split("o"))

#TITULOS => title()
    #print(saludo.title())

#CONTAR NUMERO DE CARACTERES => len()
    #print(len(saludo))

#UNIR ELEMENTOS SEPARADOS => join()
    #print(" ".join(saludo))

#SALTO DE LINEA => \n
    #print("Hola\nMundo")

#INTERPOLACION DE STRINGS
    #nombre = "Juan"
    #edad = 25
    #print(f"Hola, mi nombre es {nombre} y tengo {edad} años")

#PRECISION DE DATOS NUMERICOS
    #numero = 3.1416
    #print(f"{numero:.2f}")

#INGRESO DE DATOS POR TECLADO => input()
    #nombre = input("Ingrese su nombre: ")
    #print(f"Hola {nombre}")

#PARSEAR DATOS => int(), float(), str()
    #numero = "3.1416"
    #print(float(numero))

#OPERADORES ARITMETICOS
    # +, -, *, /, %, **, //
#EJEMPLO
    #a = 5
    #b = 2
    #print(a+b)
    #print(a-b)
    #print(a*b)
    #print(a/b)
    #print(a%b)
    #print(a**b)
    #print(a//b)

#OPERADORES DE ASIGNACION
    # =, +=, -=, *=, /=, %=, **=, //=
    #EJEMPLO
    #a = 5
    #a += 2
    #print(a)

#OPERADORES DE COMPARACION
    # ==, !=, <, >, <=, >=
    #EJEMPLO
    #a = 5
    #b = 2
    #print(a == b)
    #print(a != b)
    #print(a < b)
    #print(a > b)
    #print(a <= b)
    #print(a >= b)


#OPERADORES LOGICOS
    # and, or, not
    #EJEMPLO
    #a = 5
    #b = 2
    #c = 3
    #print(a > b and a < c)
    #print(a > b or a < c)
    #print(not a > b)


#OPERADORES DE PERTENENCIA
    # in, not in
    #EJEMPLO
    #saludo = "Hola Mundo"
    #print("Mundo" in saludo)
    #print("Python" not in saludo)

#IMPORTACION DE LIBRERIA
    #import math
    #print(math.pi)
    #print(math.e)
    #print(math.sin(90))
    #print(math.cos(90))
    #print(math.tan(90))

#USO DE CONDICIONALES
    #if 5 > 2:
    #    print("5 es mayor que 2")
    #else:
    #    print("5 no es mayor que 2")

#USO DE ELIF
    #a = 5
    #b = 5
    #if a > b:
    #    print("a es mayor que b")
    #elif a < b:
    #    print("a es menor que b")
    #else:
    #    print("a es igual a b")

#USO DE CICLOS
    #FOR
    #for i in range(10):
    #    print(i)
    #for i in range(2,10):
    #    print(i)
    #for i in range(2,10,2):
    #    print(i)
    #for i in range(10,0,-1):
    #    print(i)
    #for i in saludo:
    #    print(i)
    #for i in numeros:
    #    print(i)

    #WHILE
    #i = 0
    #while i < 10:
    #    print(i)
    #    i += 1

#LISTAS
    #print(numeros)
    #print(numeros[0])
    #print(numeros[1])
    #print(numeros[2])
    #print(numeros[3])
    #print(numeros[4])
    #print(numeros[5])
    #print(numeros[6])
    #print(numeros[-1])
    #print(numeros[-2])
    #print(numeros[-3])
    #print(numeros[-4])
    #print(numeros[-5])
    #print(numeros[-6])
    #print(numeros[-7])

    #print(numeros[0:3])
    #print(numeros[:3])
    #print(numeros[3:])
    #print(numeros[::2])
    #print(numeros[::-1])

    #numeros[0] = 10
    #print(numeros)

    #numeros.append(8)
    #print(numeros)

    #numeros.insert(0,0)
    #print(numeros)

    #numeros.pop()
    #print(numeros)

    #numeros.pop(0)
    #print(numeros)

    #numeros.remove(3)
    #print(numeros)

    #numeros.clear()
    #print(numeros)

    #del numeros
    #print(numeros)

    #numeros = [1,2,3,4,5,6,7]
    #print(len(numeros))

    #print(numeros.count(3))

    #numeros.sort()
    #print(numeros)

    #numeros.sort(reverse=True)
    #print(numeros)

    #numeros.reverse()
    #print(numeros)

    #numeros2 = numeros.copy()
    #print(numeros2)

    #numeros2 = numeros
    #print(numeros2)

    #numeros2[0] = 10
    #print(numeros)
    #print(numeros2)

    #numeros2 = numeros[:]
    #print(numeros2)

    #numeros2[0] = 10
    #print(numeros)
    #print(numeros2)

    #numeros2 = list(numeros)
    #print(numeros2

#DICIONARIOS
"""
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Lima"
}
CICLOS
for i in persona:
    print(i)
    print(persona[i])

for i in persona.values():
    print(i)

for i in persona.keys():
    print(i)

for i,j in persona.items():
    print(i,j)

print(persona["nombre"])
print(persona.get("nombre"))
print(persona.get("apellido","No existe"))


"""
#METODOS DE ESTRUCTURAS DE DATOS
"""
APPEND => AGREGA UN ELEMENTO AL FINAL DE LA LISTA => append()
EJEMPLO
    numeros.append(8)

SORT => ORDENA LOS ELEMENTOS DE LA LISTA => sort()
EJEMPLO
    numeros.sort()

COPY => COPIA UNA LISTA => copy()
EJEMPLO
    numeros2 = numeros.copy()

REMOVE => ELIMINA UN ELEMENTO ESPECIFICO DE LA LISTA => remove()
EJEMPLO
    numeros.remove(3)

POP => ELIMINA EL ULTIMO ELEMENTO DE LA LISTA => pop()
EJEMPLO
    numeros.pop()

CLEAR => ELIMINA TODOS LOS ELEMENTOS DE LA LISTA => clear()
EJEMPLO
    numeros.clear()

INSERT => AGREGA UN ELEMENTO EN UNA POSICION ESPECIFICA => insert()
EJEMPLO
    numeros.insert(0,0)

COUNT => CUENTA EL NUMERO DE VECES QUE SE REPITE UN ELEMENTO => count()
EJEMPLO
    numeros.count(3)

REVERSE => INVIERTE EL ORDEN DE LOS ELEMENTOS DE LA LISTA => reverse()
EJEMPLO
    numeros.reverse()

INDEX => DEVUELVE LA POSICION DE UN ELEMENTO => index()
EJEMPLO
    numeros.index(3)

DEL => ELIMINA UNA LISTA => del
EJEMPLO
    del numeros

SLICE => DEVUELVE UNA PORCION DE LA LISTA => []
EJEMPLO
    numeros[0:3]
    numeros[:3]
    numeros[3:]
    numeros[::2]
    numeros[::-1]

LEN => DEVUELVE EL NUMERO DE ELEMENTOS DE LA LISTA => len()
EJEMPLO
    len(numeros)

SORTED => ORDENA LOS ELEMENTOS DE LA LISTA => sorted()
EJEMPLO
    sorted(numeros)
    
"""
#FUNCIONES
"""
SUMA sum(a,b)

EJEMPLO
    sum(5,2)
MAX max(a,b)

EJEMPLO
    max(5,2)

MIN min(a,b)
EJEMPLO
    min(5,2)
"""

#APIS
"""
VERBOS HTTP
GET => OBTENER INFORMACION
POST => ENVIAR INFORMACION
PUT => ACTUALIZAR INFORMACION
DELETE => ELIMINAR INFORMACION
PATCH => ACTUALIZAR PARCIALMENTE INFORMACION
HEAD => OBTENER INFORMACION DE CABECERA
"""

#CREAR ENTORNO VIRTUAL
"""
pip install virtualenv
solo si no lo tienes instalado

virtualenv env
env\Scripts\activate => WINDOWS
source env/bin/activate => LINUX

pip install requests => para poder hacer peticiones a una API
"""
#PETICIONES A UNA API
"""
GET
    EJEMPLO
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(response.status_code) 
    print(response.json())

POST
    EJEMPLO
    import requests
    payload = {
        "title":"foo",
        "body":"bar",
        "userId":1
    }
    headers = {
        "Content-Type":"application/json"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts",data=payload,headers=headers)
    print(response.status_code) 
    print(response.json())

PUT
    EJEMPLO
    import requests
    payload = {
        "title":"foo",
        "body":"bar",
        "userId":1
    }
    headers = {
        "Content-Type":"application/json"
    }
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1",data=payload,headers=headers)
    print(response.status_code) 
    print(response.json())

DELETE
    EJEMPLO
    import requests
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    print(response.status_code) 
    print(response.json())
    
"""





