from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

b = webdriver.Firefox()
b.get("https://www.python.org")

try:
    e = WebDriverWait(b, 10).until(
        EC.presence_of_element_located((By.ID, "start-shell"))
        )

finally:
    b.quit()

