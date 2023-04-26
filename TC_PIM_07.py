import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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

@pytest.mark.dependency(name="create_contact")
def test_create_contact(setup):
    
    pim_menu = setup.find_element_by_id("")
    pim_menu.click()
    
    add_employee_menu = setup.find_element_by_id("")
    add_employee_menu.click()
    
    first_name = setup.find_element_by_id("username")
    last_name = setup.find_element_by_id("password")
    save_btn = setup.find_element_by_xpath('')
    first_name.send_keys("Murugavel")
    last_name.send_keys("R")
    save_btn.click()
    
    WebDriverWait(setup, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']")))

@pytest.mark.dependency(depends=["create_contact"])
def test_update_emergency_contact(setup):
    
    emergency_tab = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[6]/div/div/div[2]/textarea')
    emergency_tab.find_element_by_link_text("oxd-input-group oxd-input-field-bottom-space").click()
    
    add_btn = setup.find_element_by_xpath("/html/body/script[2]")
    add_btn.click()
    name = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input')
    relationship = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input')
    home_telephone = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input')
    mobile_telephone = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[3]/div/div[2]/input')
    work_telephone = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/input')
    email = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]')
    name.send_keys("Deepan")
    relationship.send_keys("Karthik")
    home_telephone.send_keys("1234567")
    mobile_telephone.send_keys("9876543")
    work_telephone.send_keys("2345678")
    email.send_keys("murugavel2381@gamil.com")

    save_btn = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/button')
    save_btn.click()
    contacts_table = setup.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
    rows = contacts_table.find_elements_by_tag_name("tr")
    assert "Jane Doe" in rows[1].text
    assert "Spouse" in rows[1].text
    assert "1234567" in rows[1].text
    assert "9876543" in rows[1].text
    assert "2345678" in rows[1].text
    assert "jane.doe@example.com" in rows[1].text
