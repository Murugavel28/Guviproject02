import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver

def test_employee_personal_details(setup):
    driver = setup
    driver.get("https://orangehrm-demo-6x.orangehrmlive.com/")
    driver.maximize_window()
    assert "OrangeHRM" in driver.title

    # Login
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("Admin")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("admin123")
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()

    # Navigate to PIM
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()

    # Navigate to Employee List
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()

    # Click on Employee Name
    driver.find_element_by_link_text("oxd-autocomplete-text-input oxd-autocomplete-text-input--active").click()

    # Validate Tabs
    tabs = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration', 'Job', 'Salary', 'Tax Exemptions', 'Report-to', 'Qualifications', 'Memberships']
    for tab in tabs:
        assert driver.find_element_by_id(f'tab{tab.replace(" ", "")}').is_displayed()

    driver.close()
    driver.quit()

