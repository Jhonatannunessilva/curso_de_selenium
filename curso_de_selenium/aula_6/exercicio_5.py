from time import sleep
from selenium.webdriver import Firefox

browser = Firefox()

browser.get("https://selenium.dunossauro.live/exercicio_05.html")

while True:
    sleep(1)
    form_class = browser.find_element_by_css_selector("header span").text

    if form_class in "... Mentira, você conseguiu terminar":
        break

    form = browser.find_element_by_css_selector(f".form-{form_class}")

    form.find_element_by_css_selector("input[type='text']").send_keys("teste")

    form.find_element_by_css_selector("input[type='password']").send_keys(
        "teste"
    )

    form.find_element_by_css_selector("input[type='submit']").click()

browser.quit()
