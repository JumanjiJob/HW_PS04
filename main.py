# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.get("https://www.sports.ru/football/")
# browser.save_screenshot("dom.png")
# time.sleep(5)
# browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
# browser.save_screenshot("dom1.png")
# time.sleep(3)
# browser.refresh()

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()