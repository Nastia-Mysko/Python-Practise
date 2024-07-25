import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome()  # Використання правильного способу імпорту драйвера
    driver.get(url="https://qalight.ua")
    time.sleep(3)

    # Знаходження поля пошуку та введення запиту
    search = driver.find_element(by=By.ID, value='search')
    search.click()
    search.send_keys("Тест")
    time.sleep(3)
    search.send_keys(Keys.RETURN)
    time.sleep(3)

    # Знаходження та натискання на посилання "Словник тестувальника"
    link = driver.find_element(by=By.LINK_TEXT, value="Автоматизація тестування за допомогою Selenium WebDriver (Python)")
    link.click()
    time.sleep(3)

    # Знаходження та натискання на посилання "Контакти"
    contacts_link = driver.find_element(by=By.LINK_TEXT, value="Контакти")
    contacts_link.click()
    time.sleep(3)

    # Знаходження поля для введення імені та введення тестового значення
    name_field = driver.find_element(by=By.NAME, value="name-field")
    name_field.click()
    name_field.send_keys("Тест")
    time.sleep(5)

    print("1")

if __name__ == "__main__":  # Використання правильного порівняння імені модуля
    main()
