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
- **browser.find_element_by_id("id_qualquer")**: Utilizado para retornar o WebElement que tem em seu atributo "id" o valor passado como argumento.
- **browser.find_element_by_class_name("classe_qualquer")**: Utilizado para retornar a primeira ocorrência de um WebElement que tenha em seu atributo "class" o valor passado como argumento.
- **browser.find_elements_by_class_name("classe_qualquer")**: Utilizado para retornar todos os WebElements que tenham em seu atributo "class" o valor passado como argumento.
- **browser.find_element_by_name("nome_qualquer")**: Utilizado para retornar a primeira ocorrência de um WebElement que tenha em seu atributo "name" o valor passado como argumento.
- **FirefoxWebElement.send_keys("texto")**: Utilizado para "digitar" o texto passado como argumento.
- **browser.find_element_by_css_selector("seletor_css_qualquer")**: Utilizado para retornar a primeira ocorrência de um WebElement que atenda ao seletor css passado como argumento.
- **browser.find_elements_by_css_selector("seletor_css_qualquer")**: Utilizado para retornar todas as ocorrências de um WebElement que atenda ao seletor css passado como argumento.
- **Seletores CSS**:
  - **#nome_do_id**: Seletor utilizado para retornar o WebElement que tenha em seu atributo "id" o valor depois da "#".
  - **tag**: Seletor utilizado para retornar a primeira ocorrência da tag passada como argumento.
  - **.nome_da_classe**: Seletor utilizado para retornar o WebElement que tenha em seu atributo "class" o valor depois do ".".
  - **tag.nome_da_classe**: Seletor que combina a tag e a seleção pela classe.
  - **[nome_do_atributo]**: Seletor utilizado para retornar o WebElement que tenha o atributo passado entre os "[ ]".
  - **[atributo operador valor]**:
    - **nome_do_atributo = valor**: Operador utilizado para retornar o WebElement que tenha em seu atributo o valor exatamente igual ao valor passado depois do "=".
    - **nome_do_atributo \*= valor**: Operador utilizado para retornar o WebElement que tenha em seu atributo a ocorrência do valor passado depois do "*=".
    - **nome_do_atributo |= valor**: Operador utilizado para retornar o WebElement que tenha em seu atributo o valor exatamente igual ou iniciar com valor passado depois do "|=".
    - **nome_do_atributo ^= valor**: Operador utilizado para retornar o WebElement que tenha em seu atributo um valor que inicie com valor passado depois do "^=".
    - **nome_do_atributo $= valor**: Operador utilizado para retornar o WebElement que tenha em seu atributo um valor que termine com valor passado depois do "$=".
    - **nome_do_atributo ~= valor**: Operador utilizado para retornar o WebElement que tenha em seu atributo um de seus valores exatamente igual ao valor passado depois do "~=".
  - **\***: Seletor utilizado para retornar qualquer WebElement, pode ser chamado de "seletor universal".
  - **Seletor "combinado"**: Utilizado para usar vários tipos de seletores ao mesmo tempo. Todos os seletores mostrados podem ser utilizados em conjunto, alguns exemplos:
    - **tag[nome_do_atributo]**
    - **tag[nome_do_atributo operador valor]**
    - **\*[nome_do_atributo operador valor]**
  - **seletor_qualquer , seletor_qualquer**: Utilizado para trazer o resultado do primeiro seletor junto com o resultado do segundo seletor. É possível agrupar o resultado de n seletores.
  - **Seletores Combinadores**
    - **seletor_qualquer + seletor_qualquer**: Utilizado para pegar os WebElements irmãos adjacentes do primeiro seletor e que esteja de acordo com o segundo seletor.
    - **seletor_qualquer ~ seletor_qualquer**: Utilizado para pegar os WebElements que estão no mesmo nível do primeiro seletor e que esteja de acordo com o segundo seletor.
    - **seletor_qualquer > seletor_qualquer**: Utilizado para pegar os WebElements que são diretamente filhos do primeiro seletor e que esteja de acordo com o segundo seletor.
    - **seletor_qualquer seletor_qualquer**: Utilizado para pegar os WebElements que são diretamente ou indiretamente filhos do primeiro seletor (os descendentes) e que esteja de acordo com o segundo seletor.

**Observações**:

- Entenda **browser** como a instância do driver escolhido, ou seja, escolhendo o "from selenium.webdriver import Firefox" então **browser = Firefox()**
- Entenda **FirefoxWebElement** como o tipo de retorno de métodos como o **browser.find_element_by_tag_name("nome_da_tag")**, caso você esteja usando outra instância de navegador esse tipo irá mudar, mas sempre seguirá o modelo de um WebElement.
