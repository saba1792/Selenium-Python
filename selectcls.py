from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

b = webdriver.Firefox()
b.get("file:///C:/Users/sabar/Selenium%20Python/index.html?numReturn=400&Send=Submit")

s = Select(b.find_element_by_name('numReturn'))
s.select_by_index(4)        #index based on the option we want to select
time.sleep(4)
s.select_by_visible_text("200")
time.sleep(4)
s.select_by_value("600")
time.sleep(4)

o = s.options
print(o)

sb = b.find_element_by_name('Send')
sb.submit()
time.sleep(6)

b.close()