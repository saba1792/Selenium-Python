from selenium import webdriver
import time
from selenium.webdriver import ActionChains

b = webdriver.Firefox()
b.get("https://jqueryui.com/droppable")
b.switch_to.frame(0)

ac = ActionChains(b)

src = b.find_element_by_id('draggable')
trgt = b.find_element_by_id('droppable')
ac.drag_and_drop_by_offset(src, 100, 100).perform()
time.sleep(4)
ac.drag_and_drop(src, trgt).perform()
time.sleep(4)

b.close()