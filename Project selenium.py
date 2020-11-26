from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
item = input()
path = 'D:\Programming\Python\PyCharm Community Edition 2020.1.2\Selenium\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.lazada.sg/')
search = driver.find_element_by_id('q')
#accessing elements = id,name,class
search.send_keys(item)
search.send_keys(Keys.RETURN)
specific_laptop = driver.find_element_by_class_name('c2prKC')
print(specific_laptop.text)

driver.quit()