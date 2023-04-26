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
    
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    login_btn = driver.find_element_by_id("btnLogin")
    username.send_keys("admin")
    password.send_keys("admin123")
    login_btn.click()
    yield driver
    
    driver.quit()

@pytest.mark.dependency(name="create_employee")
def test_create_employee(setup):
    
    pim_menu = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
    pim_menu.click()
    
    add_employee_menu = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
    add_employee_menu.click()
    
    first_name = setup.find_element_by_name("username")
    last_name = setup.find_element_by_name("passwoord")
    save_btn = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
    first_name.send_keys("John")
    last_name.send_keys("Doe")
    save_btn.click()
    
    WebDriverWait(setup, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']")))

@pytest.mark.dependency(depends=["create_employee"])
def test_update_job_details(setup):
    
    job_details_tab = setup.find_element_by_id("sidenav")
    job_details_tab.find_element_by_link_text("Job").click()
    
    job_title = setup.find_element_by_id("job_job_title")
    employment_status = setup.find_element_by_id("job_emp_status")
    job_category = setup.find_element_by_id("job_eeo_category")
    job_title.send_keys("Software Engineer")
    employment_status.send_keys("Full-Time Contract")
    job_category.send_keys("Professional")
    
    include_contract_details = setup.find_element_by_id("job_contract_details")
    include_contract_details.click()
    
    contract_start_date = setup.find_element_by_id("job_contract_start_date")
    contract_end_date = setup.find_element_by_xpath("job_contract_end_date")
    contract_type = setup.find_element_by_id("job_contract_type")
    contract_start_date.send_keys("01012022")
    contract_end_date.send_keys("12312022")
    contract_type.send_keys("Fixed Term")
    
    save_btn = setup.find_element_by_id("btnSave")
    save_btn.click()
    
    job_title_text = setup.find_element_by_id("job_job_title").get_attribute("value")
    employment_status_text = setup.find_element_by_id("job_emp_status").get_attribute("value")
    job_category_text = setup.find_element_by_id("job_eeo_category").get_attribute("value")
    contract_start_date_text = setup.find_element_by_id("job_contract_start_date").get_attribute("value")
    contract_end_date_text = setup.find_element_by_id("job_contract_end_date").get_attribute("value")
    contract_type_text = setup.find_element_by_id("job_contract_type").get_attribute("value")
