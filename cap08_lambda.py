x = lambda a: a + 10
x(5)

y = lambda a, b: a * b
y(3, 4)

z = lambda a, b, c: a + b + c
z(1, 2, 3)

iniciales = lambda nombre, apellido: nombre[0] + apellido[0]
iniciales("Juan", "Perez")


def multiplicador(n):
    return lambda x: x * n


duplicador = multiplicador(2)
triplicador = multiplicador(3)
cuadruplicador = multiplicador(4)

duplicador(5)
triplicador(5)
cuadruplicador(5)

suma_numeros = lambda *args: sum(args)
suma_numeros(1, 2, 3, 4, 5)
