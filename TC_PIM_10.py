import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestEmployeeJobDetails:
    
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()
    
    def test_employee_job_termination(self, setup):
        # Login as Admin and navigate to Job Details page
        self.driver.get("https://orangehrm.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123" + Keys.RETURN)
        self.driver.find_element(By.ID, "menu_pim_viewPimModule").click()
        self.driver.find_element(By.ID, "menu_pim_viewEmployeeList").click()
        self.driver.find_element(By.LINK_TEXT, "John").click()
        self.driver.find_element(By.ID, "sidenav").find_element(By.LINK_TEXT, "Job").click()
        
        # Terminate employment
        self.driver.find_element(By.ID, "btnTerminateEmployment").click()
        self.driver.find_element(By.ID, "terminationDate").send_keys("2023-04-25")
        self.driver.find_element(By.ID, "terminationReason").send_keys("End of Contract")
        self.driver.find_element(By.ID, "btnSave").click()
        
        # Validate termination date
        termination_date = self.driver.find_element(By.ID, "terminationDate_display_field").text
        assert termination_date == "2023-04-25", "Termination date not matching"
        
        # Validate Activate Employment button visibility
        activate_button = self.driver.find_element(By.ID, "btnReinstate")
        assert activate_button.is_displayed(), "Activate Employment button not visible"
