from selenium import webdriver
from selenium.webdriver.common.by import By

print("Here the sample test case will be started")
driver = webdriver.Chrome()

driver.get("https://listado.mercadolibre.com.pe/teclados")

elementos = driver.find_elements(
    by=By.CLASS_NAME,
    value="ui-search-layout__item.shops__layout-item.ui-search-layout__stack",
)

len(elementos)

elemento = elementos[0]

ele_precio = elemento.find_element(
    by=By.CLASS_NAME, value="andes-money-amount__fraction"
)

ele_precio.text

datos = []
dato = {}
for elemento in elementos:
    ele_titulo_url = elemento.find_element(
        by=By.CLASS_NAME,
        value="ui-search-item__group__element.ui-search-link__title-card.ui-search-link",
    )
    titulo = ele_titulo_url.get_attribute("title")
    url = ele_titulo_url.get_attribute("href")

    ele_precio = elemento.find_element(
        by=By.CLASS_NAME, value="andes-money-amount__fraction"
    )
    print(ele_precio.text)
    try:
        ele_centavos = elemento.find_element(
            by=By.CLASS_NAME,
            value="andes-money-amount__cents.andes-money-amount__cents--superscript-24",
        )
        print(f"{ele_precio.text}.{ele_centavos.text}")
    except Exception as e:
        ele_centavos = None

    try:
        ele_descuento = elemento.find_element(
            by=By.CLASS_NAME, value="ui-search-price__second-line"
        ).find_element(by=By.CLASS_NAME, value="andes-money-amount__fraction")
        print(ele_descuento.text)
    except Exception as e:
        ele_descuento = None

    dato = {
        "precio_entero": ele_precio.text,
        "precio_decimal": ele_centavos.text if ele_centavos else None,
        "descuento": ele_descuento.text if ele_descuento else None,
    }

    # ahora append a todos los datos a la lista
    datos.append(dato)


import pandas as pd

df = pd.DataFrame(datos)

driver.close()


###########################
# si quieren entrar a los comentarios de un producto
# primero tienen que entrar a la url del producto

# driver.get(url)

# luego al elemento de comentarios
# ele_coments = driver.find_elements(
# by=By.CLASS_NAME, value="ui-review-capability-comments__comment"
# )

# y luego iterar sobre los comentarios
# for ele_coment in ele_coments:
#     ele_coment.text
