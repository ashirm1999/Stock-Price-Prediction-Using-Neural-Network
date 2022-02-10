import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import json


PATH = "/Users/ashirm1999/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)
time.sleep(2)

df = pd.read_csv('/Users/ashirm1999/Downloads/Speaker.csv')

url = []
for i in df['Speaker']:
    ans1 = i.split('_')
    query = str(ans1[0]) + " " + str(ans1[1]) + " ted talk"
    driver.get('https://www.google.com')
    time.sleep(1)
    search = driver.find_element_by_name('q')
    search.send_keys(query)
    search.send_keys(Keys.RETURN)
    links = driver.find_elements_by_xpath("//a[@href]")

    for i in links:
        if 'www.ted.com/talks/' in (i.get_attribute("href")):
            print(i.get_attribute("href"))
            url.append(i.get_attribute("href"))
            break

print(len(df), len(url))
df["Url"] = url
df.to_csv(r'/Users/ashirm1999/Downloads/Ted_Speaker_Url.csv', index = False)
driver.quit()