from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json


PATH = "/Users/ashirm1999/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

link = input("Enter the link of the Ted Talk")
driver.get(link)
time.sleep(5)

a = driver.find_element_by_xpath("//div[contains(text(), 'Read transcript')]")
a.click()

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
time.sleep(3)
html.send_keys(Keys.HOME)

x = driver.find_elements_by_class_name("w-full.mb-6")
result = ""
for i in x:
    result = result + i.text

f = open(str(link.split("/")[-1]) + ".txt","w+")
f.write(result)
f.close
print(result)