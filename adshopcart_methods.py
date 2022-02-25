import sys
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import adshopcart_locators as locators
from selenium.webdriver.common.keys import Keys

s = Service(executable_path=r"D:\Users\CCTB_STU002\PycharmProjects\python_cctb\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Fixture method - to open web browser
def setUp():
    if driver is not None:
        print(f"-----------------------------------------")
        print(f"Test Started at: {datetime.datetime.now()}")
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Advantage Shopping Cart website
    driver.get(locators.adshopcart_url)

    # Checking that we are on the correct URL address and we are seeing correct title
    # if driver.current_url == locators.adshopcart_url and driver.title.endswith("Advantage Shopping"):
    if driver.current_url == locators.adshopcart_url and driver.title.endswith("Advantage Shopping"):
        print(f"We are at the Advantage Shopping Cart homepage -- {driver.current_url}")
        print(f"We\'re seeing title message -- {driver.title}")
    else:
        print(f"We\'re not at the Advantage Shopping Cart homepage. Check your code!")
        driver.close()
        driver.quit()

# Fixture method -  to close web browser
def tearDown():
    if driver is not None:
        print(f"--------------------------------------------")
        print(f"Test Completed at: {datetime.datetime.now()}")
        driver.close()
        driver.quit()

setUp()
tearDown()


