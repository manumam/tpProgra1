import json
import random

usuarioEnSesion = ''

def verificarUsuario():

    """Verifica si el usuario y la contraseña y existen y son correctos entre si. No recibe parametros y tiene como salida un valor booleano."""

    validacion = False
    user = str(input('Ingrese su nombre de usuario. '))
    try:
        with open("usuarios.json", "rt") as archivo:
            usuarios = json.load(archivo)

            for usuario in usuarios:
                if (usuario["userId"] == user):
                    pwd = str(input('Ingrese su contraseña. '))
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


########################################### USUARIOS #################################################

def validarIDUsuarios(id):
    validacion = False
    try:
        with open("usuarios.json", "rt") as archivo:
            usuarios = json.load(archivo)

            for usuario in usuarios:
                validacion = usuarios["id"] == id or validacion
        
    except Exception as e:
        print(e)
    
    return validacion


def crearUsuario():

    id = random.randint(0, 100)
    while(validarIDUsuarios(id)):
        id = random.randint(0,100)

    nombre = str(input('Ingrese el nombre del usuario. '))
    apellido = str(input('Ingrese el apellido del usuario. '))
    status = int(input('Que tipo de usuario está creando?\n'
                       '1. ADMIN'
                       '2. EMPLOYEE'))
    
    if status == 1:
        statusStr = "ADMIN"
    elif status == 2:
        statusStr = "EMPLOYEE"

    registro = {"id": id, "nombre": nombre, "apellido": apellido, "status": statusStr}

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
