from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://login.yahoo.com")

try:
    UserElement = browser.find_element_by_id("login-username")
    UserElement.send_keys("UserDoesNotExist")
    for i in range(5):
        UserElement.send_keys(Keys.BACK_SPACE)
    SubmitElement = browser.find_element_by_id("login-signin")
    SubmitElement.submit()      # Can use UserElement.submit() as well
    # SubmitElement.click()     # Submit does the same thing in case of forms
    HtmlElement = browser.find_element_by_tag_name("html")
    HtmlElement.send_keys(Keys.HOME)        # Scrolls to the top of the page
    time.sleep(5)       # Wait
    HtmlElement.send_keys(Keys.END)         # Scrolls to the bottom of the page
    browser.quit()

except:
    print("Not Found")

# KEYS
"""
Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
Keys.ENTER, Keys.RETURN
Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP
Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE
Keys.F1, Keys.F2, . . . , Keys.F12
Keys.TAB
"""

# BROWSER BUTTONS
"""
browser.back() Clicks the Back button.
browser.forward() Clicks the Forward button.
browser.refresh() Clicks the Refresh/Reload button.
browser.quit() Clicks the Close Window button.
"""