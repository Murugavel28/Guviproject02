import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


TEST_CASE_ID = "TC_PIM_03"


URL = "http://<your_url>"


USERNAME = "Admin"
PASSWORD = "admin123"


FIRST_NAME = "John"
LAST_NAME = "Doe"
EMP_ID = "EMP123"
USERNAME_NEW_EMPLOYEE = "johndoe123"
PASSWORD_NEW_EMPLOYEE = "password123"


@pytest.mark.parametrize("first_name, last_name, emp_id, username_new_employee, password_new_employee", [(FIRST_NAME, LAST_NAME, EMP_ID, USERNAME_NEW_EMPLOYEE, PASSWORD_NEW_EMPLOYEE)])
def test_create_new_employee_pim(first_name, last_name, emp_id, username_new_employee, password_new_employee):
    
    driver = webdriver.Chrome()


    driver.maximize_window()

    
    driver.get(URL)

    
    username_field = driver.find_element_by_name("username")
    password_field = driver.find_element_by_name("password")

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    
    login_button = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
    login_button.click()

    
    pim_button = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
    pim_button.click()

    
    add_button = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
    add_button.click()

    
    first_name_field = driver.find_element_by_id("Murugavel")
    last_name_field = driver.find_element_by_id("R")
    emp_id_field = driver.find_element_by_id("52056")
    username_new_employee_field = driver.find_element_by_id("user_name")
    password_new_employee_field = driver.find_element_by_id("user_password")
    confirm_password_new_employee_field = driver.find_element_by_id("re_password")

    first_name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)
    emp_id_field.send_keys(emp_id)
    username_new_employee_field.send_keys(username_new_employee)
    password_new_employee_field.send_keys(password_new_employee)
    confirm_password_new_employee_field.send_keys(password_new_employee)

    
    enabled_button = driver.find_element_by_id("status")
    enabled_button.click()

    
    save_button = driver.find_element_by_id("btnSave")
    save_button.click()

    
    success_message = driver.find_element_by_xpath("//div[@class='message success fadable']")
    assert success_message.is_displayed()


    driver.quit()
