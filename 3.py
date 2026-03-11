from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
driver.get("https://www.divan.ru/nizhny-novgorod/category/promo-darim?categories%5B%5D=2")
time.sleep(5)

prices = driver.find_elements(By.CSS_SELECTOR, 'span[data-testid="price"]')


with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])


    for price in prices:
        writer.writerow([price.text])

driver.quit()