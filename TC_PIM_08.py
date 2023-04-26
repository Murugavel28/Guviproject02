import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def setup():
    
    driver = webdriver.Chrome()
    
    driver.get("https://orangehrm3.com")
    
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    login_btn = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    username.send_keys("admin")
    password.send_keys("admin123")
    login_btn.click()
    yield driver
    
    driver.quit()

@pytest.mark.dependency(name="create_contact")
def test_create_contact(setup):
    
    pim_menu = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[5]/div/div[4]/div')
    pim_menu.click()
    
    add_employee_menu = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]')
    add_employee_menu.click()
    
    first_name = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]')
    last_name = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input')
    save_btn = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
    first_name.send_keys("John")
    last_name.send_keys("Doe")
    save_btn.click()
    
    WebDriverWait(setup, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']")))

@pytest.mark.dependency(depends=["create_contact"])
def test_update_dependent_contact(setup):
    
    dependents_tab = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[32]/div/div[3]/div')
    dependents_tab.find_element_by_link_text("Dependents").click()
    
    add_btn = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[33]/div/div[4]/div')
    add_btn.click()
    
    name = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[9]/div/div[4]/div')
    relationship = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
    date_of_birth = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div')
    name.send_keys("Jane Doe")
    relationship.send_keys("Spouse")
    date_of_birth.send_keys("01011980")
    date_of_birth.send_keys(Keys.RETURN)
    
    save_btn = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input')
    save_btn.click()
    
    dependents_table = setup.find_element_by_id("dependent_list")
    rows = dependents_table.find_elements_by_tag_name("tr")
    assert "Jane Doe" in rows[1].text
    assert "Spouse" in rows[1].text
    assert "01/01/1980" in rows[1].text
