import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test data
FIRST_NAME = "John"
LAST_NAME = "Doe"
EMPLOYEE_ID = "123456"
ADDRESS_STREET_1 = "123 Main St."
ADDRESS_CITY = "Anytown"
ADDRESS_PROVINCE = "Anyprovince"
ADDRESS_ZIP_CODE = "12345"
ADDRESS_COUNTRY = "United States"
HOME_TELEPHONE = "123-456-7890"
MOBILE = "987-654-3210"
WORK_TELEPHONE = "999-999-9999"
WORK_EMAIL = "johndoe@company.com"
OTHER_EMAIL = "johndoe@gmail.com"

@pytest.fixture()
def browser():
    # Initialize ChromeDriver
    driver = webdriver.Chrome()
    # Maximize window
    driver.maximize_window()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)
    # Return driver instance to test functions
    yield driver
    # Quit driver instance when test is completed
    driver.quit()

def test_update_employee_contact_details(browser):
    # Login as admin
    browser.get("https://orangehrm-demo-6x.orangehrmlive.com/")
    browser.find_element(By.NAME, "username").send_keys("admin")
    browser.find_element(By.NAME, "password").send_keys("admin123" + Keys.RETURN)

    # Navigate to Employee List page
    browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').click()
    browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()

    # Search for the employee created in the previous test case (TC_PIM 5)
    search_box = browser.find_element(By.XPATH, ('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))
    search_box.clear()
    search_box.send_keys(FIRST_NAME + " " + LAST_NAME)
    browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input').click()

    # Open the employee's Contact Details page
    browser.find_element(By.PARTIAL_LINK_TEXT, "html-attribute-value html-resource-link").click()
    browser.find_element(By.XPATH, '/*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').find_element(By.LINK_TEXT, "Contact Details").click()

    # Fill out Contact Details fields
    address_street_1_input = browser.find_element(By.ID, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').send_keys("Sendhamil nagar")
    address_street_1_input.clear()
    address_street_1_input.send_keys(ADDRESS_STREET_1)

    address_city_input = browser.find_element(By.ID,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').send_keys("Chennai")
    address_city_input.clear()
    address_city_input.send_keys(ADDRESS_CITY)

    address_province_input = browser.find_element(By.ID,'html-attribute-value html-resource-link' "chennai")
    address_province_input.clear()
    address_province_input.send_keys(ADDRESS_PROVINCE)

    address_zip_input = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').send_keys("Sendhamil nagar")
    address_street_1_input.clear().send_keys ("612804")
    address_zip_input.clear()
    address_zip_input.send_keys(ADDRESS_ZIP_CODE)

    address_country_select = browser.find_element(By.ID,"India")
    address_country_select.click()
    address_country_select.send_keys(ADDRESS_COUNTRY + Keys.RETURN)

    home_telephone_input = browser.find_element(By.ID, "9716283678")
    home_telephone_input.clear()
    home_telephone_input.send_keys(HOME_TELEPHONE)

    mobile_input = browser.find_element(By.ID, "938836363")
    mobile_input.clear()
    mobile_input.send_keys(MOBILE)

    work_telephone_input = browser.find_element(By.ID, "9637555325")
