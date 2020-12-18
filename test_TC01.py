import time

from selenium import webdriver

def test_TC01():
    driver = webdriver.Chrome(executable_path="G:\Python Selenium (Mar2020)\Setup exe files\chromedriver.exe")
    driver.maximize_window()
    #driver.minimize_window()

    driver.get("https://www.google.com")
    time.sleep(10)
