x = []

len(x)

bool(x)

x = [1, 2, 3, 4, 5]
len(x)

x[0]
x[4]

y = ["abc", "xyz", "fernando", "abc"]

z = [1.2, 3.4, 5.6, 7.8]
w = [True, False, False, True]

type(w)
type(z)

wz = [1.2, True]
wz = [w, z]

len(wz)
wz[1][2]
wz[0][-1]

# Slicing
w[2:]
w[1:3]

5 in z
5.6 in z

z[1] = 4.3

z[1:3] = [3.4, 6.5]

z[1:3] = [10.5]

z.insert(0, 0.5)

z.insert(2, 2.5)

x.append(6)
x.append([7, 8, 9])
x.append(7)
x.append(8)
x.append(9)

x.extend([10, 11, 12])

x += [13, 14, 15]

x.remove([7, 8, 9])
x.insert(5, [7, 8, 9])

x.pop(5)
x


del x[2]
x

x.clear()

frutas = ["papaya", "manzana", "pera", "mango"]

for fruta in frutas:
    print(fruta)

frutas.index("pera")

frutas.sort()
frutas[2]

frutas.sort(reverse=True)

x = [4, 2, 5, 1, 3]
x.sort()

x = [
    ["nombre", "apellido", "edad", "distrito"],
    ["Fernando", "Cortes", 30, "Lince"],
    ["Juan", "Perez", 25, "San Miguel"],
]

import pandas as pd

df = pd.DataFrame(x)

x[1:3]
x[0]

df = pd.DataFrame(x[1:], columns=x[0])
