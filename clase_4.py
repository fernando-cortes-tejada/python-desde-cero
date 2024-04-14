x = {}

type(x)
bool(x)

x = {
    "nombre": "Fernando",
    "apellido": "Carrillo",
    "edad": 27,
}

len(x)

x["nombre"]
x["apellido"]
x.get("nombre")

x["distrito"]
x.get("distrito", "No tiene distrito")

y = x.get("distrito")

if not y:
    x["distrito"] = "Lince"

x["edad"] = 30
x

domicilio = {
    "direccion": "Manuel Villavecencio 123",
    "distrito": "Lince",
    "provincia": "Lima",
    "pais": "Perú",
}

x = {"nombre": "Fernando", "apellido": "Carrillo", "edad": 27, "domicilio": domicilio}

x = {
    "nombre": "Fernando",
    "apellido": "Carrillo",
    "edad": 27,
    "domicilio": {
        "direccion": "Manuel Villavecencio 123",
        "distrito": "Lince",
        "provincia": "Lima",
        "pais": "Perú",
    },
    "documento": {
        "tipo": "dni",
        "numero": "12345678",
        "emision": "2023-12-01",
        "votaciones": [
            {"eleccion": 2005, "candidato": "Pepito"},
            {"eleccion": 2010, "candidato": "Juanito"},
            {"eleccion": 2015, "candidato": "Pablito", "mesa": 1234},
            {
                "eleccion": 2020,
                "candidato": "Fulanito",
                "mesa": 5678,
                "lugar_de_votacion": {
                    "nombre": "IE 1234",
                    "distrito": "Lince",
                    "provincia": "Lima",
                    "pais": "Perú",
                },
            },
        ],
    },
}

x.keys()
x["domicilio"]["provincia"]

x["documento"].keys()
x["documento"]["votaciones"][0]["candidato"]

x.values()

x.items()

for key, value in x.items():
    print(key, value)


x.pop("documento")
x


x = {
    "nombre": "Fernando",
    "apellido": "Carrillo",
    "edad": 27,
    "distrito": "Lince",
}
y = {
    "nombre": "Jose",
    "apellido": "Perez",
    "edad": 30,
    "numeros_favoritos": [1, 2, 3, 4, 5],
}
z = {
    "nombre": "Maria",
    "apellido": "Gomez",
    "edad": 25,
    "comida_favorita": "arroz con pollo",
}

personas = [x, y, z]

import pandas as pd

df = pd.DataFrame(personas)
df
