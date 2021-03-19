from functools import reduce
from time import sleep
from typing import List
from urllib.parse import urlparse

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.webelement import FirefoxWebElement


def find_element_by_nested_tag_name(browser, tags) -> FirefoxWebElement:
    return reduce(
        lambda element, tag_name: element.find_element_by_tag_name(tag_name),
        tags,
        browser,
    )


def find_elements_by_nested_tag_name(
    browser, nested_tags, tag
) -> List[FirefoxWebElement]:
    element = find_element_by_nested_tag_name(browser, nested_tags)
    return element.find_elements_by_tag_name(tag)


browser = Firefox()

# Step 1

browser.get("https://selenium.dunossauro.live/exercicio_03.html")

sleep(2)

# main: FirefoxWebElement = browser.find_element_by_tag_name("main")
# element: FirefoxWebElement = main.find_element_by_tag_name("a")

element = find_element_by_nested_tag_name(browser, ["main", "li", "a"])

element.click()

# Step 2

sleep(2)

# main: FirefoxWebElement = browser.find_element_by_tag_name("main")
# elements: FirefoxWebElement = main.find_elements_by_tag_name("a")

element = find_elements_by_nested_tag_name(browser, ["main"], "p")[1]

splitted_text = element.text.split()

number_1 = int(splitted_text[0])
number_2 = int(splitted_text[2])

result = number_1 * number_2

elements = find_elements_by_nested_tag_name(browser, ["main"], "a")

for a in elements:
    if int(a.text) != result:
        a.click()
        break

# Step 3

sleep(30)

# main: FirefoxWebElement = browser.find_element_by_tag_name("main")
# elements: FirefoxWebElement = main.find_elements_by_tag_name("a")

elements = find_elements_by_nested_tag_name(browser, ["main"], "a")

for a in elements:
    if a.text == browser.title:
        a.click()
        break

# Step 4

sleep(2)

parsed_url = urlparse(browser.current_url)

# main: FirefoxWebElement = browser.find_element_by_tag_name("main")
# elements: FirefoxWebElement = main.find_elements_by_tag_name("a")

elements = find_elements_by_nested_tag_name(browser, ["main"], "a")

for a in elements:
    if a.text in parsed_url.path:
        a.click()
        break

# Step 5

sleep(2)

browser.refresh()

sleep(1)

browser.quit()
