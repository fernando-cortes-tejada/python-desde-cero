def imprimir():
    print("Fernando Cortés")
    return 1


x = imprimir()


def imprimir_nombre(nombre: str) -> str:
    print(nombre)
    return nombre[0]


x = imprimir_nombre("Fernando")


def imprimir_nombre_completo(nombre: str, apellido: str) -> str:
    print(nombre, apellido)
    return nombre[0] + apellido[0]


x = imprimir_nombre_completo(apellido="Cortés", nombre="Fernando")
y = imprimir_nombre_completo("José", "Pérez")
z = imprimir_nombre_completo("María", apellido="Gómez")
w = imprimir_nombre_completo(apellido="García", nombre="Luis")


def imprimir_familia_cortes(nombre: str, apellido: str = "Cortés") -> str:
    print(nombre, apellido)
    return nombre[0] + apellido[0]


imprimir_familia_cortes("Fernando")
imprimir_familia_cortes("Fernando", "Gómez")


def suma_numeros(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


suma_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9)


def imprima_parametros_y_valores(**kwargs):
    for parametro, valor in kwargs.items():
        print(parametro, valor)


imprima_parametros_y_valores(nombre="Fernando", apellido="Cortés", edad=30)


def obtener_iniciales(nombre: str, apellido: str) -> str:
    return nombre[0] + apellido[0]


def imprimir_nombre_completo(nombre: str, apellido: str):
    iniciales = obtener_iniciales(nombre, apellido)
    print(iniciales, nombre, apellido)


imprimir_nombre_completo("josé", "Pérez")
iniciales = obtener_iniciales("Fernando", "Cortés")
