import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

class main:
    def search_google_and_check():
        chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        chrome_driver.get('https://www.google.com')
        chrome_driver.maximize_window()
        if not "Google" in chrome_driver.title:
            raise Exception("Could not load page")
        element = chrome_driver.find_element(By.NAME, "q")
        element.send_keys("Hepsiburada")
        element.submit()
        # Check if the LambdaTest Home Page is open
        title = "Türkiye'nin En Büyük Online Alışveriş Sitesi Hepsiburada.com"
        lt_link = chrome_driver.find_element(By.XPATH,
            "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3")
        lt_link.click()
        sleep(5)
        assert title == chrome_driver.title
        sleep(2)
        chrome_driver.quit()


main.search_google_and_check()
