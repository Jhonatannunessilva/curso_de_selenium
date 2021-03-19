"""
1. Pegar todos os links de aulas
    {'nome da aula': 'link da aula'}
2. Navegar até o exercício 3
    achar a url do exercício 3 e ir até lá
"""
from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox()

browser.get("http://selenium.dunossauro.live/aula_04.html")


def get_links(browser, elemento):  # retorna um dicionário
    """
    Pega todos os links dentro de um elemento
    - browser = a instância do navegador
    - elemento = nome da tag do elemento a ser buscado [body, main, ul, ...]
    """
    resultado = {}
    elemento_web = browser.find_element_by_tag_name(elemento)
    ancoras = elemento_web.find_elements_by_tag_name("a")
    for acora in ancoras:
        resultado[acora.text] = acora.get_attribute("href")

    return resultado


"""
Parte 1
"""
sleep(2)

aulas = get_links(browser, "aside")

pprint(aulas)

"""
browser.get(resultado_1['Aula 3'])
browser.get(resultado_1['Aula 4'])
"""


"""
Parte 2
"""
exercicios = get_links(browser, "main")

pprint(exercicios)

browser.get(exercicios["Exercício 3"])

browser.quit()
