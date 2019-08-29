from selenium import webdriver

b = webdriver.Firefox()
b.implicitly_wait(10)
b.get("https://www.python.org")
myde = b.find_element_by_id('start-shell')

b.close()
