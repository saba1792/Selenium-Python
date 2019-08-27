from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser=webdriver.Firefox();
browser.get('https://www.python.org');
elem=browser.find_element_by_name("q")
elem.clear();
elem.send_keys("pycon");
elem.send_keys(Keys.RETURN);
time.sleep(8);

browser.close();