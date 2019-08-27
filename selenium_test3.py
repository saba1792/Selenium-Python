from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.seleniumhq.org")

element_id = browser.find_element_by_id("q")
print(element_id)

element_name = browser.find_element_by_name("q")
print(element_name)

element_xp = browser.find_element_by_xpath("//*[@id ='mainContent']/h2[1]")
print(element_xp)

ele_cl = browser.find_element_by_class_name('selenium-sponsors')
print(ele_cl)

browser.close()
