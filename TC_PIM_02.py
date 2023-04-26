import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestAdminPage:
    
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://orangehrm-demo-6x.orangehrmlive.com/")
        self.driver.find_element_by_name("username").send_keys("Admin")
        self.driver.find_element_by_name("password").send_keys("admin123")
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        yield
        self.driver.quit()
        
    @pytest.mark.parametrize("menu_option", [
        "Dashboard", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Directory", "Maintenance", "Buzz"
    ])
    def test_menu_options(self, setup, menu_option):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
        assert self.driver.find_element_by_id("menu_admin_UserManagement").is_displayed()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()
        assert self.driver.find_element_by_id(f"menu_admin_{menu_option}").is_displayed()

    def test_user_management_fields(self, setup):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[1]').click()
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div').is_displayed()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input').click()
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i').is_displayed()
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div').click()
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div').is_displayed()
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i').is_displayed()
        user_type_dropdown = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        user_type_dropdown.click()
        assert self.driver.find_element_by_xpath("//option[text()='Admin']").is_displayed()
        status_dropdown = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]')
        status_dropdown.click()
        assert self.driver.find_element_by_xpath("//option[text()='Enabled']").is_displayed()
        assert self.driver.find_element_by_xpath("//option[text()='Disabled']").is_displayed()
