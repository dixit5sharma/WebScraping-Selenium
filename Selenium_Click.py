from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://inventwithpython.com")

element = browser.find_element_by_link_text("Invent with Python Blog")
print(type(element))
element.click()