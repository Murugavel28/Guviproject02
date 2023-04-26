import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="path/to/chromedriver")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestUpdateEmployeeDetails:

    def test_update_employee_details(self, setup):
        # Login as Admin
        setup.get("https://opensource-demo.orangehrmlive.com/")
        setup.find_element(By.NAME, "username").send_keys("Admin")
        setup.find_element(By.NAME, "password").send_keys("admin123")
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()

        # Navigate to Employee List page
        setup.find_element(By.LINK_TEXT, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click()

        # Select employee to update details
        setup.find_element(By.XPATH, "//a[contains(text(),'John')]//parent::td//preceding-sibling::td/input").click()

        # Update Personal Details
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]').clear()
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys("Murugavel")
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]').clear()
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]88/div/div/div[2]/div[1]').send_keys("R")
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').clear()
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').send_keys("Karthik")
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').clear()
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("12345")
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/d').clear()
        setup.find_element(By.XPATH, '').send_keys("123456")
        Select(setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')).select_by_visible_text("Single")
        Select(setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]')).select_by_visible_text("Indian")
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').clear()
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys("1995-05-28")
        setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()

        # Verify updated details are present
        assert setup.find_element(By.XPATH, ('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')).get_attribute("value") == "John Updated"
        assert setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').get_attribute("value") == "M"
        assert setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]').get_attribute("value") == "Doe Updated"
        assert setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').get_attribute("value") == "12345"
        assert setup.find_element(By.XPATH, "personal_txtLicenNo").get_attribute("value") == "123456"
        assert setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]').get_attribute("value") == "Married"
        assert setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').get_attribute("value") == "6"
        assert setup.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]').get_attribute("value") == "1995-05-05"
