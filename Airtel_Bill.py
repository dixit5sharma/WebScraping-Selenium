from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Learing from WEB
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as expected

MobileNumber = "9717829269"
Password = "Dixit@123"

broswer = webdriver.Chrome()
wait = WebDriverWait(broswer, timeout=10)       # Learing from WEB
broswer.get("https://www.airtel.in/s/selfcare?normalLogin")

time.sleep(10)
broswer.maximize_window()
UserElement = broswer.find_element_by_name("mobileNumber")
UserElement.send_keys(MobileNumber)

PassElement = broswer.find_element_by_name("password")
PassElement.send_keys(Password)

SubmitElement = broswer.find_element_by_id("loginButtonSpan")
SubmitElement.click()
time.sleep(12)

# BillsElement = broswer.find_element_by_class_name("link pull-right")
BillsElement = broswer.find_element_by_css_selector("a.link.pull-right")
BillsElement.click()
time.sleep(8)

DetailElement = broswer.find_element_by_css_selector("a.pull-left.font-size-14.link.cursor-pointer.mt-10.hidden-xs")
DetailElement.click()
time.sleep(12)

HTML = broswer.find_element_by_tag_name("html")
HTML.send_keys(Keys.END)

LastPayment = broswer.find_elements_by_css_selector("i.icon-outlined-plus")
LastPayment[1].click()
time.sleep(8)

HTML = broswer.find_element_by_tag_name("html")
HTML.send_keys(Keys.END)
time.sleep(2)

DownloadButton = broswer.find_element_by_css_selector("i.icon.icon-outlined-download.icon-size-20.color-grey")
DownloadButton.click()