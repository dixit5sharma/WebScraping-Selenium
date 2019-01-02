from selenium import webdriver
import pyperclip,sys

webB = webdriver.Chrome()
webB.maximize_window()
if len(sys.argv)<2:
    clip = pyperclip.paste()
    webB.get("https://www.google.com/maps/place/" + clip)

else:
    clip = " ".join(sys.argv[1:])
    webB.get("https://www.google.com/maps/place/" + clip)
