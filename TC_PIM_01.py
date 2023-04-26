from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time

class TestAdminPage:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield
        self.driver.close()
    
    def test_admin_page_menus(self, setup):
        expected_menus = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Buzz']
        actual_menus = [menu.text for menu in self.driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')]
        assert actual_menus == expected_menus
    
    def test_search_box(self, setup):
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').is_displayed()
        search_texts = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Buzz']
        for search_text in search_texts:
            search_box = self.driver.find_element_by_id('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
            search_box.clear()
            search_box.send_keys(search_text.lower())
            search_box.send_keys(Keys.RETURN)
            search_results = [result.text for result in self.driver.find_elements_by_xpath("//table[@id='resultTable']//td[2]")]
            assert search_text in search_results
            search_box.clear()
            search_box.send_keys(search_text.upper())
            search_box.send_keys(Keys.RETURN)
            
            search_results = [result.text for result in self.driver.find_elements_by_xpath("//table[@id='resultTable']//td[2]")]
            assert search_text in search_results