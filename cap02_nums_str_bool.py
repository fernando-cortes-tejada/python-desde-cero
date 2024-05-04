##### NUMEROS

# Integers
x = 1
float(x)

# Floats
y = 2.7
z = 1.0
type(z)
z = int(z)
type(z)

# Cuando aplico int(float) se trunca el valor decimal
int(y)

# Float con más decimales
z = 2.931267312

# Floats con notiación científica
3e5
4e7
5e-2

# Redondeo de un float a un decimal
round(0.05, 1)

# Casteo de strings a números
w = "0.7"
int(float(w))

w = "1"
int(w)


# Operaciones

# Suma y resta
1 + 2
1 - 2
round(1.1 - 2.9, 2)

# Multiplicación y división
3 * 2
12312 / 4156

# Módulo
7 % 2

0  # enero
1  # febrero
2  # marzo
3  # abril
5  # junio
147 % 12

# Expoentes
2**3
2**0.5

# Floor division
9 // 4

# Operaciones con la misma variable
x += 1
x = x + 1

x -= 1

x *= 2
x = x * 2


# Strings o cadena de caracteres
x = "Hola Mundo"
x = "Hola Mundo"

# String de múltiples líneas
y = """
Hola
soy
Fernando
"""
print(y)

# Extracción de caracteres
x[0]  # python está indizado desde 0
x[5]
x[-1]

x[5:]
x[5:10]

len(x)
x[5 : len(x)]

x[-5:]

# Iterando sobre una cadena de texto
for i in x:
    print(i)

# Comprobar pertenencia de un string en otro string
y = "Mundo"

y in x

# Qué pasa cuando se compara minúsculas con mayúsculas
y = "mundo"
y in x

# convertir a minúsculas
y.lower() in x.lower()

# convertir a mayúsculas
y.upper() in x.upper()

# Quitar espacios iniciales y finales
x = "    Hola Mundo    "
print(x)

print(x.strip())

# Separar strings por un caracter
x = "hola, mi nombre es Fernando, tengo 30 años"
x.split(" ")
x.split(",")

# Reemplazamos un caracter por otro
x.replace("o", "a")

# Concatenamos strings
"hola" + "chau"
"hola" + " " + "chau"
y = 213134
f"abc {x}, chau {y}"


## Booleans
True
False

# Hacemos una asignación y luego una comparación
x = 1
x == 1
x == 2

x > 2
x < 2
x <= 2

# podemos asignar a una variable el resultado de una comparación
y = x == 1

# casteos de datos a bool
bool(1)
bool(3217893281)
bool(-231)
bool(0)

bool("hola")
bool(" ")
bool("")

bool([1, 2, 3])
bool([])

if 5:
    print("sí entró al if")

if 0:
    print("no entró al if")
