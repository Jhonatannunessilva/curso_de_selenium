from json import loads
from time import sleep
from urllib.parse import urlparse

from selenium.webdriver import Firefox

browser = Firefox()

browser.get("https://selenium.dunossauro.live/exercicio_04.html")


def fill_form(browser, name, email, password, phone_number):
    browser.find_element_by_name("nome").send_keys(name)
    browser.find_element_by_name("email").send_keys(email)
    browser.find_element_by_name("senha").send_keys(password)
    browser.find_element_by_name("telefone").send_keys(phone_number)
    browser.find_element_by_name("btn").click()


sleep(2)

base_structure = {
    "name": "Teste",
    "email": "teste@teste.com",
    "password": "012345",
    "phone_number": "88999738672",
}

fill_form(browser, **base_structure)

sleep(2)

result = loads(
    browser.find_element_by_tag_name("textarea").text.replace("'", '"')
)

expectted_result = {}

for item in urlparse(browser.current_url).query.split("&")[0:-1]:
    [key, value] = item.split("=")

    if key == "email":
        value = value.replace("%40", "@")

    expectted_result[key] = value

assert expectted_result == result

browser.quit()
