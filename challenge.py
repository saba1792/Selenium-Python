from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

#Open in Firefox
b = webdriver.Firefox()
b.get('https://wiki.python.org/moin/FrontPage')
time.sleep(10)

#Search a text box
s = b.find_element_by_name("value")
s.clear()

#Search the value and click Enter
s.send_keys("Beginner")
s.send_keys(Keys.RETURN)
time.sleep(10)

#Change value of a dropdown
mb = Select(b.find_element_by_xpath('//*/form/div/select'))
mb.select_by_value("raw")
time.sleep(30) #Wait time after the action is performed

#Close the browser
b.close()



