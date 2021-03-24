from time import sleep
from selenium.webdriver import Firefox

browser = Firefox()

browser.get("https://selenium.dunossauro.live/exercicio_06.html")

sleep(1)

number_of_times_to_fill = int(
    browser.find_element_by_css_selector("header p").text.split()[3]
)

for i in range(0, number_of_times_to_fill):
    sleep(1)
    form_class = browser.find_element_by_css_selector("header span").text

    form = browser.find_element_by_css_selector(f".form-{form_class}")

    form.find_element_by_css_selector("input[type='text']").send_keys("teste")

    form.find_element_by_css_selector("input[type='password']").send_keys(
        "teste"
    )

    sleep(1)

    form.find_element_by_css_selector("input[type='submit']").click()

browser.quit()
