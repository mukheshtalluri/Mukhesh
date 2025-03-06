import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Creating web driver instance
driver = webdriver.Chrome()
driver.maximize_window()
active_element = driver.switch_to.active_element
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", active_element)


# Launch the application
driver.get('https://testautomationpractice.blogspot.com/')

# Enter the details
driver.find_element(By.ID, 'name').send_keys('Mukhesh')
driver.find_element(By.ID, 'email').send_keys('mukhesh.t@gmail.com')
driver.find_element(By.ID, 'phone').send_keys('+91 1234567890')
driver.find_element(By.ID, 'textarea').send_keys('# 5-157, Hoodi main road Bangalore.')

# Click on radio button
driver.find_element(By.ID, 'female').click()

# Check the multiple checkboxes
check_boxs = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
for check_box in check_boxs:
    if check_box.get_attribute('id') in ['sunday', 'friday']:
        check_box.click()

# Handle select drop down
dropdown = driver.find_element(By.ID, 'country')
select = Select(dropdown)
select.select_by_visible_text('India')

# Handle scroll bars
element = driver.find_element(By.XPATH, "//option[@value =  'white']")
ActionChains(driver).move_to_element(element).perform()
element.click()

# Date picker - 1 using send keys
driver.find_element(By.ID, 'datepicker').send_keys('03/05/1995')

# Date picker - 2 using select class
driver.find_element(By.ID, 'txtDate').click()
dropdown_month = driver.find_element(By.CLASS_NAME, 'ui-datepicker-month')
select = Select(dropdown_month)
select.select_by_visible_text('Mar')
dropdown_year = driver.find_element(By.CLASS_NAME,'ui-datepicker-year' )
select = Select(dropdown_year)
select.select_by_index(1)
driver.find_element(By.XPATH, "//a[text() = '5']").click()

# Date picker - 3
start_date = driver.find_element(By.ID, 'start-date')
start_date.send_keys('03-05-1995')
start_date = driver.find_element(By.ID, 'end-date')
start_date.send_keys('03-05-2025')
driver.find_element(By.XPATH, "//button[text() = 'Submit']").click()

# Upload file
driver.find_element(By.ID, 'singleFileInput').send_keys('D:\Text1.txt')
driver.find_element(By.ID, 'multipleFilesInput').send_keys('D:\Text1.txt \n D:\Text2.txt')

# Static wait
time.sleep(10)
