import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_lambdatest_google():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.get('https://www.google.com')
    chrome_driver.maximize_window()
    if not "Google" in chrome_driver.title:
        raise Exception("Could not load page")
    element = chrome_driver.find_element(By.NAME, "q")
    element.send_keys("LambdaTest")
    element.submit()
    # Check if the LambdaTest Home Page is open
    title = "Most Powerful Cross Browser Testing Tool Online | LambdaTest"
    lt_link = chrome_driver.find_element(By.XPATH,
        "//h3[.='LambdaTest: Most Powerful Cross Browser Testing Tool Online']")
    lt_link.click()
    sleep(5)
    assert title == chrome_driver.title
    sleep(2)
    chrome_driver.quit()


test_lambdatest_google()
