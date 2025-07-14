def stock_marca(marca):
    total_stock = 0
    for modelo,lista in productos.items():
        if stock[modelo][1] != 0 and lista[0].lower() == marca:
            total_stock += stock[modelo][1]
    print(f"El stock es: {total_stock}")
            

def busqueda_precio(p_min,p_max):
    modelos_mostrar = []
    for modelo,(precio,stock_modelo) in stock.items():
        if p_min <= precio <= p_max:
            if stock[modelo][1] != 0:
                modelos_mostrar.append(f"{productos[modelo][0]}--{modelo}")
            
    if modelos_mostrar:
        print(f"Los notebooks entre los precios consultados son: {sorted(modelos_mostrar)}")
    else:
        print("No hay notebooks en ese rango de precio")


def actualizar_precio(modelo,p):
    if modelo in stock:
        stock[modelo][1] = p
        return True
    else:
        return False


productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

while True:
    print("BIENVENIDO A 'Pybooks'")
    print("*** MENU PRINCIPAL ***")
    print("[1]. Stock marca")
    print("[2]. Busqueda por precio")
    print("[3]. Actualizar precio")
    print("[4]. Salir")
    opcion = input("Ingrese opcion: ")
    match opcion:
        case "1":
            marca = input("Ingrese marca a consultar: ").lower()
            stock_marca(marca)

        case "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    busqueda_precio(p_min,p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")

        case "3":
            while True:
                modelo = input("Ingrse modelo a actualizar: ")
                try:
                    p = int(input("Ingrese precio nuevo: "))
                except ValueError:
                    print("El precio debe ser un numero entero")
                if actualizar_precio(modelo,p):
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe")
                
                confirmacion = input("Desea actualizar otro precio (s/n): ")
                if confirmacion == "n":
                    break

        case "4":
            print("Programa finalizado.")
            break

        case _:
            print("Debe seleccionar una opcion valida!!")