# Curso de Selenium

## Descrição

Esse projeto está sendo feito com base no curso [Selenium com Python](https://www.youtube.com/watch?v=PHHXksljGNA&list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B) ministrado pelo [Eduardo Mendes](https://www.youtube.com/channel/UCAaKeg-BocRqphErdtIUFFw). O objetivo desse repositório é copiar os códigos das aulas e resolver os exercícios propostos.

## Conhecimentos Utilizados

- **Download dos Drivers**: [Chromedriver](https://chromedriver.chromium.org/downloads) (Chrome) e [Geckodriver](https://github.com/mozilla/geckodriver/releases) (Firefox)
- **from selenium.webdriver import [Firefox, Chrome, etc]**: Utilizado para ter acesso a biblioteca que se comunicará com os drivers do navegador escolhido.
- **browser.get("url_qualquer")**: Utilizado para fazer com que o navegador faça uma requisição do tipo GET para a url passada como argumento.
- **browser.find_element_by_tag_name("nome_da_tag")**: Utilizado para retornar a primeira ocorrência da tag passada como argumento.
- **browser.find_elements_by_tag_name("nome_da_tag")**: Utilizado para retornar todas as ocorrências da tag passada como argumento.
- **FirefoxWebElement.click()**: Utilizado para fazer a "função de clicar" no elemento que chamou esse método.
- **FirefoxWebElement.text()**: Utilizado para retornar o texto que está dentro desse elemento.
- **browser.quit()**: Utilizado para fechar o navegador.
- **FirefoxWebElement.get_attribute("nome_do_atributo")**: Utilizado para retornar o valor que pertence ao atributo passado como argumento, caso o elemento não tenha o atributo será retornado **None**.
- **Busca Aninhada**: Utilizada para buscar apenas elementos que estão dentro de um elemento em especifico, ou seja, é uma busca apenas no escopo do elemento "pai".
- **FirefoxWebElement.find_element_by_tag_name("nome_da_tag")**: Utilizado para retornar a primeira ocorrência da tag passada como argumento, mas essa busca irá ser feita apenas no escopo interno do WebElement que chamou o método.
- **FirefoxWebElement.find_elements_by_tag_name("nome_da_tag")**: Utilizado para retornar todas as ocorrências da tag passada como argumento, mas essa busca irá ser feita apenas no escopo interno do WebElement que chamou o método.
- **browser.back()**: Utilizado para voltar no histórico da janela.
- **browser.forward()**: Utilizado para avançar no histórico da janela.
- **browser.current_url**: Utilizado para obter a url da janela/página atual.
- **from urllib.parse import urlparse()**: Biblioteca built-in utilizada para converter a url, que está no formato str, para um objeto que facilita a extração de valores específicos.
- **browser.title**: Utilizado para obter o titulo da janela/página atual.
- **browser.refresh()**: Utilizado para atualizar (F5) a janela/página atual.

**OBS**:

1. Entenda **browser** como a instância do driver escolhido, ou seja, escolhendo o "from selenium.webdriver import Firefox" então **browser = Firefox()**
2. Entenda **FirefoxWebElement** como o tipo de retorno de métodos como o **browser.find_element_by_tag_name("nome_da_tag")**, caso você esteja usando outra instância de navegador esse tipo irá mudar, mas sempre seguirá o modelo de um WebElement.
