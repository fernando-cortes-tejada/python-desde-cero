from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import time

driver = webdriver.Chrome()

datos = []
dato = {}


def get_precio(elemento: WebElement):
    return float(
        elemento.find_element(
            by=By.CLASS_NAME, value="andes-money-amount__fraction"
        ).text
    )


def get_descuento(elemento: WebElement):
    try:
        elemento_descuento = elemento.find_element(
            by=By.CLASS_NAME, value="ui-search-price__discount"
        )
        desc_string = elemento_descuento.text
        return float(desc_string.replace("% OFF", "")) / 100
    except Exception:
        return None


def get_label(elemento: WebElement):
    try:
        return elemento.find_element(
            by=By.CLASS_NAME,
            value="ui-search-item__highlight-label__container",
        ).text
    except Exception:
        return None


def get_foto_url(elemento: WebElement):
    try:
        elemento_padre = elemento.find_element(
            by=By.CLASS_NAME,
            value="andes-carousel-snapped__slide.andes-carousel-snapped__slide--active",
        )
        elemento_foto = elemento_padre.find_element(
            by=By.CLASS_NAME, value="ui-search-result-image__element"
        )
        return elemento_foto.get_attribute("src")
    except Exception:
        return None


driver.get("https://listado.mercadolibre.com.pe/audifonos")
for pagina in range(1, 2):
    print(f"Pagina {pagina}")
    time.sleep(3)
    elementos = driver.find_elements(
        by=By.CLASS_NAME,
        value="ui-search-layout__item.shops__layout-item.ui-search-layout__stack",
    )

    print(f"Elementos en la pagina {pagina}: {len(elementos)}")
    for elemento in elementos:
        precio = get_precio(elemento)
        porc_desc = get_descuento(elemento)
        label = get_label(elemento)
        foto_url = get_foto_url(elemento)

        dato = {
            "precio": precio,
            "descuento": porc_desc,
            "label": label,
            "foto_url": foto_url,
        }
        datos.append(dato)

    elemento_siguiente = driver.find_element(
        by=By.CLASS_NAME,
        value="andes-pagination__button.andes-pagination__button--next",
    )
    ele_sig = elemento_siguiente.find_element(
        by=By.CLASS_NAME, value="andes-pagination__link"
    )
    siguiente_pagina_url = ele_sig.get_attribute("href")
    driver.get(siguiente_pagina_url)


import pandas as pd

df = pd.DataFrame(datos)

datos[0].get("foto_url")

import requests

img_data = requests.get(datos[0].get("foto_url")).content
id_img1 = "audifonos_sony"
with open(f"fotos/{id_img1}.jpg", "wb") as handler:
    handler.write(img_data)

df.label.value_counts()

df[df["label"] == "MÁS VENDIDO"]

~df["vendedor"].isna()


driver.close()


[elemento.get("url") for elemento in elementos]
