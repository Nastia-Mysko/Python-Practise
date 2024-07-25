import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://special.pve.qalight.ua/")
time.sleep(3)


driver.maximize_window ()
time.sleep(3)

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    inner_html = link.get_attribute("innerHTML")
    if inner_html and "МОЇ КУРСИ" in inner_html:
        link.click()
        break
time.sleep(10)
