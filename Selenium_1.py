from selenium import webdriver

browser = webdriver.Firefox()
print(type(browser))

browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('card-block')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# find_element_* and find_elements_* return WebElement object
"""
browser.find_element(s)_by_class_name(name)             Elements that use the CSS class name
browser.find_element(s)_by_css_selector(selector)       Elements that match the CSS selector
browser.find_element(s)_by_id(id)                       Elements with a matching id attribute value
browser.find_element(s)_by_link_text(text)              <a> elements that completely match the text provided
browser.find_element(s)_by_partial_link_text(text)      <a> elements that contain the text provided
browser.find_element(s)_by_name(name)                   Elements with a matching name attribute value
browser.find_element(s)_by_tag_name(name)               Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')

"""

# Methods of WebElement object
"""
tag_name                        The tag name, such as 'a' for an <a> element
get_attribute(name)             The value for the element’s name attribute
text                            The text within the element, such as 'hello' in <span>hello</span>
clear()                         For text field or text area elements, clears the text typed into it
is_displayed()                  Returns True if the element is visible; otherwise returns False
is_enabled()                    For input elements, returns True if the element is enabled; otherwise returns False
is_selected()                   For checkbox or radio button elements, returns True if the element is selected; otherwise returns False
location                        A dictionary with keys 'x' and 'y' for the position of the element in the page

"""