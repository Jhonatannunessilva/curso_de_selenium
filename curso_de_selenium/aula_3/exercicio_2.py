from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.webelement import FirefoxWebElement

url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

browser = Firefox()

browser.get(url)

sleep(2)

a: FirefoxWebElement = browser.find_element_by_tag_name("a")

while True:
    a.click()

    result: str = browser.find_elements_by_tag_name("p")[-1].text

    if not result.isdigit():
        break

browser.quit()
