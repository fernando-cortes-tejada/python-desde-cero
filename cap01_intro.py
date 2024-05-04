# Entendiendo la sintaxis de Python

# primer print
print("Hello, World")

# suma de números
1 + 1

# multiplicación de números
1 * 5

# indentación
if 2 > 1:
    print("2 es mayor que 1")

# doble indentación
if 2 > 1:
    print("2 es mayor que 1")
    if 3 > 2:
        print("3 es mayor que 2")


# Declaración de variables

# Declaramos nuestra primera variable
x = 5

# Imprimimos el valor de x * 4
print(x * 4)

# Declaramos una segunda variable
y = 10

# Hacemos operaciones entre variables
print(x * y)
print(x + y)
print(y)

# Vemos cuál es el tipo de variable de x
type(x)

# Casteamos x a string
str(x)

# Probamos sumar el casteo de x a string con un número y nos da error
str(x) + 5

# Convertimos x de entero (integer) a decimal (float)
float(x)

# Declaramos un string
y = "fernando"

# "sumamos" y con la forma string de x y vemos que lo concatena
y + str(x)

# Vemos que la asignación de variables es case sensitive
X = 6  # X mayúscula es diferente a x minúscula

x + X

# Asignamos múltiples variables al mismo tiempo
x, y, z = 1, 2, 3
print(x, y, z)

# También las podemos extraer de una lista
x, y, z = [4, 5, 6]
print(x, y, z)
