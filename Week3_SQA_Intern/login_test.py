from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

try:
    print("Starting Automation Test for Login Validation...")
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2) # Wait for page to load
    
    # Automate TC_01: Valid Login
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CLASS_NAME, "radius").click()
    time.sleep(2)
    
    # Check if dashboard loaded successfully
    success_message = driver.find_element(By.ID, "flash").text
    if "secure area" in success_message:
        print("TC_01 PASS: Login successful and Dashboard loaded.")
    else:
        print("TC_01 FAIL: Dashboard not found.")

finally:
    driver.quit()
    print("Test Execution Completed.")