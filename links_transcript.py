import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import json


PATH = "/Users/ashirm1999/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

df = pd.read_csv("/Users/ashirm1999/Downloads/Ted_Speaker_Url.csv")
for k,j in zip(df['Speaker'], df['Url']):
    driver.get(j)
    time.sleep(2)
    a = driver.find_element_by_xpath("//div[contains(text(), 'Read transcript')]")
    a.click()
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(2)
    html.send_keys(Keys.HOME)

    x = driver.find_elements_by_class_name("w-full.mb-6")
    result = ""
    for i in x:
        result = result + i.text

    temp = str(k) + ".txt"
    f = open( "/Users/ashirm1999/Downloads/Ted Talks Transcript/" + temp ,"w+")
    f.write(result)
    f.close
    print(result)
    print("===================================================================")
