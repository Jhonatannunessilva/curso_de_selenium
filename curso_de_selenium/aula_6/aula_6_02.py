from selenium.webdriver import Firefox

browser = Firefox()

url = "http://selenium.dunossauro.live/aula_06_a.html"

browser.get(url)

# buscando pelo valor do atributo type e com o operador = [attr=valor]
# nome = browser.find_element_by_css_selector('[type="text"]')
# senha = browser.find_element_by_css_selector('[type="password"]')
# btn = browser.find_element_by_css_selector('[type="submit"]')

# buscando pelo valor do atributo name e com o operador = [attr=valor]
# nome = browser.find_element_by_css_selector('[name="nome"]')
# senha = browser.find_element_by_css_selector('[name="senha"]')
# btn = browser.find_element_by_css_selector('[name="l0c0"]')

# buscando pelo valor do atributo pelo operador * [att*=valor]
# nome = browser.find_element_by_css_selector('[name*="ome"]')
# senha = browser.find_element_by_css_selector('[name*="nha"]')
# btn = browser.find_element_by_css_selector('[name*="l0"]')

# buscando pelo valor do atributo pelo operador | [att|=valor]
# nome = browser.find_element_by_css_selector('[name|="nome"]')
# senha = browser.find_element_by_css_selector('[name|="senha"]')
# btn = browser.find_element_by_css_selector('[name|="l0c0"]')

# buscando pelo valor do atributo pelo operador ^ [att^=valor]
nome = browser.find_element_by_css_selector('[name^="n"]')
senha = browser.find_element_by_css_selector('[name^="s"]')
btn = browser.find_element_by_css_selector('[name^="l"]')


nome.send_keys("Eduardo")
senha.send_keys("batatinhas123")
btn.click()
