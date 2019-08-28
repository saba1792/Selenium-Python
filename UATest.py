from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

b = webdriver.Firefox()
b.get("https://www.python.org")

s = b.find_element_by_name("q")
s.clear()

s.send_keys("pycon")
s.send_keys(Keys.RETURN)
time.sleep(10)

b.close()