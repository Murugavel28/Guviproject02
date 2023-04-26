import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestEmployeeSalary:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

    def test_employee_salary(self, setup):
        # Login as admin
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123" + Keys.ENTER)

        # Go to Salary Details
        self.driver.find_element(By.ID, "menu_pim_viewMyDetails").click()
        self.driver.find_element(By.ID, "sidenav").find_element(By.LINK_TEXT, "Salary").click()

        # Add new Salary Component Details
        self.driver.find_element(By.ID, "addSalary").click()
        self.driver.find_element(By.ID, "salary_salary_component").send_keys("Bonus")
        self.driver.find_element(By.ID, "salary_currency_id").click()
        self.driver.find_element(By.XPATH, "//li[text()='United States Dollar']").click()
        self.driver.find_element(By.ID, "salary_basic_salary").send_keys("5000")
        self.driver.find_element(By.ID, "salary_comment").send_keys("Year-end bonus")
        self.driver.find_element(By.ID, "btnSalarySave").click()

        # Toggle Direct Deposit Details
        self.driver.find_element(By.ID, "showDirectDeposit").click()
        assert self.driver.find_element(By.ID, "directdeposit_account").is_displayed()

        # Fill out Direct Deposit Details and Save
        self.driver.find_element(By.ID, "directdeposit_account").send_keys("123456789")
        self.driver.find_element(By.ID, "directdeposit_amount").send_keys("3500")
        self.driver.find_element(By.ID, "btnDirectDepositSave").click()

        # Validate all fields are filled up properly
        assert self.driver.find_element(By.ID, "directdeposit_account").get_attribute("value") == "123456789"
        assert self.driver.find_element(By.ID, "directdeposit_amount").get_attribute("value") == "3500"

        # Validate Salary and Deposit are visible
        assert "Salary Components" in self.driver.page_source
        assert "Direct Deposit" in self.driver.page_source
