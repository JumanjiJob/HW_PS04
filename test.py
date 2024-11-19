import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

url = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"

browser = webdriver.Chrome()
browser.get(url)
question = str(input("Введите запрос "))

assert "Википедия" in browser.title
time.sleep(5)

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(question)
time.sleep(2)
search_box.send_keys(Keys.RETURN)


paragraphs = browser.find_elements(By.CLASS_NAME, "toctext")


index = int(input("Выберите действие из списка 1 - листать параграфы; 2 - перейти на одну из связанных страниц; 3 - выйти из программы "))
if index == 1:
    for paragraph in paragraphs:
     paragraph.click()
     time.sleep(5)

if index == 2:
    links = browser.find_elements(By.TAG_NAME, "a")
    link = random.choice(links).get_attribute("href")
    browser.get(link)
    time.sleep(10)




# for paragraph in paragraphs:
#     print(paragraph.text)
#     input()


