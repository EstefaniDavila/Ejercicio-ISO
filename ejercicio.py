# PROGRAMA PRINCIPAL
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}


def Menu():
    i=0
    print("="*50)
    print("Lista de Productos:")
    print("="*50)
    for x in Productos:  
        i +=1
        print(i,end=" "*5)
        print(Productos[x],end=" "*5)
        print(Precios[x],end=" "*5)
        print(Stock[x])
    print("="*50)
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")

def Agregar():
    print("="*19)
    print("| AGREGANDO DATOS |")
    print("="*19)
    llave = int(input("Ingrese el ID del Producto: "))
    product = input("Ingrese el NOMBRE del Producto: ")
    price = float(input("Ingrese el PRECIO del Producto: "))
    stock = int(input("Ingrese el STOCK a tener del Producto: "))
    Productos[llave] = product
    Precios[llave] = price
    Stock[llave] = stock

def Eliminar():
    print("="*20)
    print("| ELIMINANDO DATOS |")
    print("="*20)
    erase = int(input("Ingrese el NUMERO DE ORDEN del producto que desea ELIMINAR: "))
    Productos.pop(erase)
    Precios.pop(erase)
    Stock.pop(erase)

def Actualizar():
    print("="*24)
    print("|¿Que desea ACTUALIZAR?|")
    print("="*24)
    print("|     [1] Productos    |")
    print("|     [2] Precios      |")
    print("|     [3] Stock        |")
    print("="*24)
    kill = int(input("Elija Su Opción a Actualizar: "))
    if kill == 1:
        print("Actualizando PRODUCTOS")
        numero = int(input("Ingrese el NUMERO DE ORDEN del Producto: "))
        nombre = input("Nuevo Nombre del producto: ")
        Productos[numero]=nombre
    elif kill == 2:
        print("Actualizando PRECIOS")
        numero = int(input("Ingrese el NUMERO DE ORDEN del Producto: "))
        precio = float(input("Nuevo Precio: "))
        Precios[numero]=precio
    else:
        print("Actualizando STOCK")
        numero = int(input("Ingrese el NUMERO DE ORDEN del Producto: "))
        stocks = int(input("Nuevo Stock: "))
        Stock[numero]=stocks

def Adios():
    print("Gracias por usar nuestro servicio")

while True:
    try:
        Menu()
        opcion = int(input("Elija opción: "))
        print("="*50)
    except ValueError:
        print("Disculpe, Esa no es una opcion...")
        continue
    if opcion == 1: #Agregar
        Agregar()
        continue
    elif opcion == 2: #Eliminar
        Eliminar()
        continue
    elif opcion == 3: #Actualizar
        Actualizar()
        continue
    elif opcion == 4: #Salir
        Adios()
        break
