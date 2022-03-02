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
    if driver.current_url == locators.adshopcart_url and driver.title == " Advantage Shopping":
    # if driver.current_url == locators.adshopcart_url and driver.title.endswith("Advantage Shopping"):
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


def create_new_user():
    driver.find_element(By.ID, "menuUser").click()
    sleep(2)
    assert driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT").is_displayed()
    sleep(2)
    driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT").click()
    # Enter fake data into Account Details, Personal Details and Address open fields
    driver.find_element(By.NAME, "usernameRegisterPage").send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.NAME, "emailRegisterPage").send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.NAME, "passwordRegisterPage").send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.NAME, "first_nameRegisterPage").send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.NAME, "last_nameRegisterPage").send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.NAME, "phone_numberRegisterPage").send_keys(locators.last_name)
    sleep(0.25)
    Select(driver.find_element(By.NAME, "countryListboxRegisterPage")).select_by_visible_text('Canada')
    sleep(0.25)
    driver.find_element(By.NAME, "cityRegisterPage").send_keys(locators.city)
    sleep(0.25)
    driver.find_element(By.NAME, "addressRegisterPage").send_keys(locators.address)
    sleep(0.25)
    driver.find_element(By.NAME, "state_/_province_/_regionRegisterPage").send_keys(locators.province)
    sleep(0.25)
    driver.find_element(By.NAME, "postal_codeRegisterPage").send_keys(locators.postal_code)
    sleep(0.25)
    # Unclick by 'Receive exclusive offers and promotions from Advantage' checkbox
    driver.find_element(By.NAME, "allowOffersPromotion").click()
    sleep(0.25)
    # Click by 'I agree...' checkbox
    driver.find_element(By.NAME, "i_agree").click()
    sleep(0.25)
    # Click by "Register" button
    driver.find_element(By.ID, "register_btnundefined").click()
    print(f'A New User has been registered. Username: {locators.new_username}, Password: {locators.new_password} '
          f'and Full Name: {locators.full_name}')
    sleep(2)


def check_user_created():
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    # Check that New User's Full name is displayed
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(1)
    if driver.find_element(By.XPATH, f'//*[@id="myAccountContainer"]/div[1]/div/div[1]/label[contains(., "{locators.full_name}")]').is_displayed():
        print(f'----A New User with a Full Name of {locators.full_name} is displayed. Test Passed.----')
    sleep(1)
    # Check that a New User has no orders placed
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
    sleep(1)
    if driver.find_element(By.XPATH, '//div[3]/div/div/label[contains(., " - No orders - ")]').is_displayed():
        print(f'----"-No Orders-" confirmation in My Orders is displayed. Test Passed.----')
    sleep(0.25)
    # Logout from Advantage Shopping Cart website
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(1)


def check_we_login_with_new_cred():
    driver.find_element(By.ID, "menuUser").click()
    sleep(2)
    driver.find_element(By.NAME, "username").send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.NAME, "password").send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, "sign_in_btnundefined").click()
    sleep(1)
    if driver.find_element(By.PARTIAL_LINK_TEXT, f"{locators.new_username}").is_displayed():
        print(f'----Login with new credentials is successful. Username: {locators.new_username} is displayed. Test Passed.----')


def delete_new_user():
    driver.find_element(By.ID, "menuUser").click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(0.25)
    if driver.find_element(By.XPATH, f'//*[@id="myAccountContainer"]/div[1]/div/div[1]/label[contains(., "{locators.full_name}")]').is_displayed():
        driver.find_element(By.XPATH, '//*[text() = "Delete Account"]').click()
        sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="deleteAccountPopup"]/div[3]/div[1]').click()
    sleep(7)
    # Check that a New User has been successfully deleted
    if driver.current_url == locators.adshopcart_url:
        print(f"----A New User with username {locators.new_username} got deleted. Test passed.----")
    else:
        print(f"A New User with username '{locators.new_username}' has not been deleted.")


def login_with_deleted_credentials():
    driver.find_element(By.ID, "menuUser").click()
    sleep(2)
    driver.find_element(By.NAME, "username").send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.NAME, "password").send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, "sign_in_btnundefined").click()
    sleep(0.25)
    if driver.find_element(By.XPATH, '//*[contains(., "Incorrect user name or password.")]').is_displayed():
        print(f"----'Incorrect user name or password.' error label is displayed. Test Passed.----")
    else:
        print("'Incorrect user name or password.' error label is NOT displayed. Check your code.")


def check_homepage():
    driver.get(locators.adshopcart_url)
    sleep(0.5)
    # Check that SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE texts are displayed.
    if driver.find_element(By.ID, 'speakersTxt').is_displayed():
        print("----SPEAKERS text is displayed. Test passed.----")
    else:
        print("SPEAKERS text is not visible.Check your code!")
        sleep(0.25)
    if driver.find_element(By.ID, 'tabletsTxt').is_displayed():
        print("----TABLETS text is displayed. Test passed.----")
    else:
        print("TABLETS text is not visible.Check your code!")
        sleep(0.25)
    if driver.find_element(By.ID, 'laptopsTxt').is_displayed():
        print("----LAPTOPS text is displayed. Test passed.----")
    else:
        print("LAPTOPS text is not visible.Check your code!")
    sleep(0.25)
    if driver.find_element(By.ID, 'miceTxt').is_displayed():
        print("----MICE text is displayed. Test passed.----")
    else:
        print("MICE text is not visible.Check your code!")
    sleep(0.25)
    # Check that SPECIAL OFFER, POPULAR ITEMS and CONTACT US links at the top nav menu are clickable
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    if driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').is_displayed():
        print("----SPECIAL OFFER link is displayed. Test passed.----")
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    if driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').is_displayed():
        print("----POPULAR ITEMS link is displayed. Test passed.----")
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    if driver.find_element(By.LINK_TEXT, 'CONTACT US').is_displayed():
        print("----CONTACT US link is displayed. Test passed.----")
        sleep(1)
    # Check main logo is displayed.
    if driver.find_element(By.XPATH, '//*[contains(., "dvantage")]').is_displayed() and \
            driver.find_element(By.XPATH, '//*[contains(., "DEMO")]').is_displayed():
        print("----Main Logo is displayed. Test passed.----")


def fill_out_contact_us_form():
    driver.find_element(By.NAME, "categoryListboxContactUs").click()
    sleep(0.25)
    if driver.find_element(By.NAME, "categoryListboxContactUs").is_displayed():
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text("Laptops")
    sleep(1)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text("HP Chromebook 14 G1(ENERGY STAR)")
    sleep(1)
    driver.find_element(By.NAME, "emailContactUs").send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.NAME, "subjectTextareaContactUs").send_keys('Test. Laptops')
    sleep(0.25)
    if driver.find_element(By.XPATH, '//button[contains(., "SEND")]').is_displayed():
        print("----CONTACT US form is working properly. Test passed.----")
    driver.find_element(By.XPATH, '//button[contains(., "SEND")]').click()
    sleep(1)
    # Check CONTINUE SHOPPING button is displayed and clickable
    if driver.find_element(By.LINK_TEXT, "CONTINUE SHOPPING").is_displayed():
        print("----CONTINUE SHOPPING button is displayed. Test passed.-----")
    driver.find_element(By.LINK_TEXT, "CONTINUE SHOPPING").click()
    if driver.current_url == locators.adshopcart_url:
        print(f"----CONTINUE SHOPPING button has been clicked. Test passed.----")
    else:
        print(f"CONTINUE SHOPPING button has NOT been clicked. Check your code")










