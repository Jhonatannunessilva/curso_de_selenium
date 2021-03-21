from selenium.webdriver import Firefox

url = "http://selenium.dunossauro.live/aula_05_a.html"

browser = Firefox()

browser.get(url)

div_py = browser.find_element_by_id("python")
print(div_py.text)

div_hk = browser.find_element_by_id("haskell")
print(div_hk.text)

browser.quit()
