import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestTaxExemptions:
    
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_tax_exemptions(self, test_setup):
        driver.get("https://orangehrm-demo-6x.orangehrmlive.com/")
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.ID, "btnLogin").click()

        # Navigate to Tax Exemptions page
        driver.find_element(By.ID, "Type for hints...").click()
        driver.find_element(By.ID, "oxd-select-text-input").find_element(By.LINK_TEXT, "Tax Exemptions").click()
        driver.find_element(By.ID, "oxd-select-text-input1").click()

        # Fill out Tax Exemptions details
        driver.find_element(By.ID, "taxauth").send_keys("IRS")
        driver.find_element(By.ID, "taxemp").send_keys("1234")
        driver.find_element(By.ID, "taxexpdate").send_keys("2024-12-31")

        # Toggle Direct Deposit Details and fill out mandatory fields
        driver.find_element(By.ID, "addDirectDepositCheckbox").click()
        driver.find_element(By.ID, "bankName").send_keys("Bank of America")
        driver.find_element(By.ID, "accountNumber").send_keys("1234567890")
        driver.find_element(By.ID, "confirmAccountNumber").send_keys("1234567890")
        driver.find_element(By.ID, "routingNumber").send_keys("111000025")
        driver.find_element(By.ID, "saveTaxExemptionBtn").click()

        # Validate all fields are filled up properly
        tax_exemption_table = driver.find_element(By.ID, "taxExemptionListTable")
        assert "IRS" in tax_exemption_table.text
        assert "1234" in tax_exemption_table.text
        assert "12/31/2024" in tax_exemption_table.text
        assert "Bank of America" in tax_exemption_table.text
        assert "1234567890" in tax_exemption_table.text
