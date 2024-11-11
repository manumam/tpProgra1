import json
import random
import re

usuarioEnSesion = ''

def verificarUsuario(id):

    """Verifica si el usuario y la contrasena y existen y son correctos entre si. No recibe parametros y tiene como salida un valor booleano."""

    validacion = False
    try:
        with open("usuarios.json", "rt") as archivo:
            usuarios = json.load(archivo)

            for usuario in usuarios:
                if (usuario["id"] == id):
                    pwd = str(input('Ingrese su contrasena. '))
                    validacion = pwd == usuario["pwd"]
    except:
        print('Error al acceder al archivo. ')
    
    return validacion
    
########################################### PRODUCTOS #################################################

def validarIDStock(id):
    validacion = False
    try:
        with open("stock.json", "rt") as archivo:
            productos = json.load(archivo)

            for producto in productos:
                validacion = producto["id"] == id or validacion
        
    except Exception as e:
        print(e)
    
    return validacion

def crearProducto():

    id = random.randint(0, 100)
    while(validarIDStock(id)):
        id = random.randint(0,100)

    producto = str(input('Ingrese el nombre del nuevo producto. '))
    precio = int(input('Ingrese el precio del producto. '))
    cantidad = int(input('Ingrese cuantas unidades cargará inicialmente. '))

    registro = {"id": id, "producto": producto, "precio": precio, "cantidad": cantidad}

    try:
        with open("stock.json", "rt") as stock:
            productos = json.load(stock)
    
    except FileNotFoundError:
        productos = []

    productos.append(registro)

    try:
        with open("stock.json", "wt") as stock:
            json.dump(productos, stock, indent=4)
    
    except IOError:
        print("Error al cargar el archivo. ")


def obtenerPosicionPorProducto(id):
    try:
        with open("stock.json", "rt") as stock:
            posicion = 0
            productos = json.load(stock)
            for producto in productos:
                if producto["id"] == id:
                    return posicion
                else:
                    posicion = posicion + 1

                return posicion
    except IOError:
        print("Error al cargar el archivo. ")


def modificarPrecio(id):

    precio = int(input("Ingrese el nuevo precio para este producto. "))

    try:
        with open("stock.json", "rt") as stock:
            productos = json.load(stock)
    except IOError:
        print("Error al cargar el archivo. ")
    
    posicion = obtenerPosicionPorProducto(id)
    
    registro = {"id": productos[posicion]["id"], "producto": productos[posicion]["producto"], "precio": precio, "cantidad": productos[posicion]["cantidad"]}
    productos.pop(posicion)
    productos.append(registro)

    try:
        with open("stock.json", "wt") as stock:
            json.dump(productos, stock, indent=4)
    except IOError:
        print("Error al cargar el archivo. ")

def modificarStock(id):

    cantidad = int(input("Ingrese la cantidad de unidades que ingresará para este producto. "))

    try:
        with open("stock.json", "rt") as stock:
            productos = json.load(stock)
    except IOError:
        print("Error al cargar el archivo. ")
    
    posicion = obtenerPosicionPorProducto(id)
    
    registro = {"id": productos[posicion]["id"], "producto": productos[posicion]["producto"], "precio": productos[posicion]["precio"], "cantidad": productos[posicion]["cantidad"] + cantidad}
    productos.pop(posicion)
    productos.append(registro)

    try:
        with open("stock.json", "wt") as stock:
            json.dump(productos, stock, indent=4)
    except IOError:
        print("Error al cargar el archivo. ")

def mostrarProductos():
    try:
        with open("stock.json", "rt") as stock:
            productos = json.load(stock)
    except IOError:
        print("Error al ingresar al archivo. ")
    
    for producto in productos:
        print(f"{producto["id"]}. {producto["producto"]} ${producto["precio"]}")
    




########################################### USUARIOS #################################################

def validarIDUsuarios(id):
    validacion = False
    try:
        with open("usuarios.json", "rt") as archivo:
            usuarios = json.load(archivo)

            for usuario in usuarios:
                validacion = usuario["id"] == id or validacion
        
    except Exception as e:
        print(e)
    
    return validacion

def status(id):
    try:
        with open("usuarios.json", "rt") as users:
            usuarios = json.load(users)
    except IOError:
        print("Error al acceder al archivo. ")

    for usuario in usuarios:
        if(usuario["id"] == id):
            status = usuario["status"]
    
    return status

def obtenerPosicionPorUsuario(id):
    try:
        with open("usuarios.json", "rt") as users:
            posicion = 0
            usuarios = json.load(users)
            for usuario in usuarios:
                if usuario["id"] == id:
                    return posicion
                else:
                    posicion = posicion + 1

                return posicion
    except IOError:
        print("Error al cargar el archivo. ")

def crearUsuario():

    id = random.randint(0, 100)
    while(validarIDUsuarios(id)):
        id = random.randint(0,100)

    nombre = str(input('Ingrese el nombre del usuario. '))
    apellido = str(input('Ingrese el apellido del usuario. '))
    status = int(input('Que tipo de usuario está creando?\n'
                       '1. ADMIN\n'
                       '2. EMPLOYEE\n'))
    
    if status == 1:
        statusStr = "ADMIN"
    elif status == 2:
        statusStr = "EMPLOYEE"

    registro = {"id": id, "nombre": nombre, "apellido": apellido, "status": statusStr, "pwd": ""}

    try:
        with open("usuarios.json", "rt") as users:
            usuarios = json.load(users)
    
    except FileNotFoundError:
        usuarios = []

    usuarios.append(registro)

    try:
        with open("usuarios.json", "wt") as users:
            json.dump(usuarios, users, indent=4)
    
    except IOError:
        print("Error al cargar el archivo. ")

def chequearRegEx(password):
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    requisitos = bool(re.match(patron, password))
    while(requisitos == False):
        password = str(input("La contrasena ingresada no cumple los requisitos minimos.\n"
                            "Recuerde que debe cumplir con:\n"
                            "1 letra mayuscula\n" 
                            "1 letra minuscula\n"
                            "1 caracter numerico\n"
                            "longitud minima de 8 caracteres.\n"))
        requisitos = bool(re.match(patron, password))
    
    return password


def administrarPassword(id):
    try:
        with open("usuarios.json", "rt") as users:
            usuarios = json.load(users)
    except IOError:
        print("Error al cargar el archivo.")

    for usuario in usuarios:
        if(usuario["id"] == id):
            nombre = usuario["nombre"]
            apellido = usuario["apellido"]
            statusStr = usuario["status"]
            if(usuario["pwd"] == ""):
                password = str(input("Ingrese la nueva contrasena para este usuario.\n"
                          "La misma debe contar con al menos: \n"
                          "1 letra mayuscula\n" 
                          "1 letra minuscula\n"
                          "1 caracter numerico\n"
                          "longitud minima de 8 caracteres.\n"))
                password = chequearRegEx(password)
            elif(usuario["pwd"] != ""):
                oldPassword = str(input("Ingrese la contrasena anterior. "))
                if(usuario["pwd"] == oldPassword):
                    password = str(input("Ingrese la nueva contrasena para este usuario.\n"
                          "La misma debe contar con al menos: \n"
                          "1 letra mayuscula\n" 
                          "1 letra minuscula\n"
                          "1 caracter numerico\n"
                          "longitud minima de 8 caracteres.\n"))
                    password = chequearRegEx(password)
                else:
                    while(usuario["pwd"] != oldPassword):
                        oldPassword = str(input("Contrasena anterior incorrecta. Ingrese nuevamente. "))
                    password = str(input("Ingrese la nueva contrasena para este usuario.\n"
                                        "La misma debe contar con al menos: \n"
                                        "1 letra mayuscula\n" 
                                        "1 letra minuscula\n"
                                        "1 caracter numerico\n"
                                        "longitud minima de 8 caracteres.\n"))
                    password = chequearRegEx(password)
    
    posicion = obtenerPosicionPorUsuario(id)

    registro = {"id": id, "nombre": nombre, "apellido": apellido, "status": statusStr, "pwd": password}
    usuarios.pop(posicion)
    usuarios.append(registro)
    
    try:
        with open("usuarios.json", "wt") as users:
            json.dump(usuarios, users, indent=4)
    except IOError:
        print("Error al intentar abrir el archivo. ")

def cambiarStatus(id):
    try:
        with open("usuarios.json", "rt") as users:
            usuarios = json.load(users)
    except IOError:
        print("Error al intentar acceder al archivo. ")
    
    for usuario in usuarios:
        if(usuario["id"] == id):
            nombre = usuario["nombre"]
            apellido = usuario["apellido"]
            password = usuario["pwd"]
            status = int(input(f"El status actual del usuario es {usuario["status"]}. Ingrese el nuevo status.\n"
                               "1. ADMIN\n"
                               "2. EMPLOYEE\n"))
            if(status == 1):
                statusStr = "ADMIN"
            elif(status == 2):
                statusStr = "EMPLOYEE"
    
    posicion = obtenerPosicionPorUsuario(id)

    registro = {"id": id, "nombre": nombre, "apellido": apellido, "status": statusStr, "pwd": password}
    usuarios.pop(posicion)
    usuarios.append(registro)

    try:
        with open("usuarios.json", "wt") as users:
            json.dump(usuarios, users, indent=4)
    except IOError:
        print("Error al intentar acceder al archivo. ")

def eliminarUsuario(id):
    try:
        with open("usuarios.json", "rt") as users:
            usuarios = json.load(users)
    except IOError:
        print("Error al ingresar al archivo. ")
    
    indice = 0
    while (usuarios[indice]["id"] != id):
        indice = indice + 1

    usuarios.pop(indice)

    try:
        with open("usuarios.json", "wt") as users:
            json.dump(usuarios, users, indent=4)
    except IOError:
        print("Error al intentar acceder al archivo. ")
        


def mostrarUsuarios():
    try:
        with open("usuarios.json", "rt") as users:
            usuarios = json.load(users)
    except IOError:
        print("Error al acceder al archivo. ")

    for usuario in usuarios:
        print(f"{usuario["id"]}. {usuario["nombre"]} {usuario["apellido"]} - {usuario["status"]}")