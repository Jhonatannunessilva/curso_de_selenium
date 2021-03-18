from pprint import pprint
from time import sleep
from typing import List

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.webelement import FirefoxWebElement

url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

browser = Firefox()

browser.get(url)

sleep(2)

expected_result = {
    "H1": {
        "texto1": "Essa página é top de mais",
        "texto2": "E eu vou pegar todos os dados com selenium",
        "texto3": "Pq aqui não é brincadeira",
    }
}

result = {"H1": {}}

elements: List[FirefoxWebElement] = browser.find_elements_by_tag_name("p")

for p in elements:
    result["H1"][p.get_attribute("atributo")] = p.text

pprint(result)
print(result == expected_result)

browser.quit()
