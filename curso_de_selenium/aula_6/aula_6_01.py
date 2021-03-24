from selenium.webdriver import Firefox

browser = Firefox()

url = "http://selenium.dunossauro.live/aula_06_a.html"

browser.get(url)

browser.find_element_by_css_selector("input").send_keys("eduardo")
