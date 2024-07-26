import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




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

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID,"loginbtn")



username_field.send_keys("a.mysko17@gmail.com")
time.sleep(10)
password_field.send_keys("Durex1711!!")

login_button.click()
time.sleep(10)
