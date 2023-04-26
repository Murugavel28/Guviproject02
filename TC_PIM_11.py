import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestJobDetails:
    @pytest.fixture(scope="class")
    def browser(self):
        driver = webdriver.Chrome()  
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_activate_employment(self, browser):
        # Login as admin
        browser.get("https://<your_orangehrm_url>")
        username = browser.find_element(By.ID, "txtUsername")
        username.send_keys("<your_username>")
        password = browser.find_element(By.ID, "txtPassword")
        password.send_keys("<your_password>")
        login_button = browser.find_element(By.ID, "btnLogin")
        login_button.click()

        # Navigate to Job Details
        pim_menu = browser.find_element(By.ID, "oxd-main-menu-item")
        pim_menu.click()
        job_menu = browser.find_element(By.ID, "oxd-main-menu-item active")
        job_menu.click()
        employee_name = browser.find_element(By.CSS_SELECTOR, "a[href*='empNumber=']")
        employee_name.click()
        job_details_tab = browser.find_element(By.ID, "Type for hints...")
        job_details_tab.find_element(By.LINK_TEXT, "Job").click()

        # Click Activate Employment
        activate_employment_button = browser.find_element(By.ID, "btnActivate")
        activate_employment_button.click()

        # Validate Employee Job is Activated
        activate_employment_popup = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "employee_activate"))
        )
        activation_date = activate_employment_popup.find_element(By.ID, "activate_date")
        activation_date.send_keys("2023-04-25")
        activation_reason = activate_employment_popup.find_element(By.ID, "activate_comment")
        activation_reason.send_keys("Activation reason")
        save_button = activate_employment_popup.find_element(By.ID, "btnSave")
        save_button.click()

        # Validate Activation on Job Details page
        job_details_tab = browser.find_element(By.ID, "sidenav")
        job_details_tab.find_element(By.LINK_TEXT, "Job").click()
        employment_status = browser.find_element(By.ID, "emp_job_employment_status")
        assert employment_status.text == "Full-Time Contract"
