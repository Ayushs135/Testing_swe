from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager 
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

print("\n=== Starting Selenium Tests ===")

driver.get("file:///C:/Users/ayush/OneDrive/Desktop/vs/software/index.html")
driver.maximize_window()

# TC1: Valid login
try:
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "loginButton")
    email.clear()
    password.clear()
    email.send_keys("admin@example.com")
    password.send_keys("admin123")
    login_btn.click()
    time.sleep(1)

    if "dashboard.html" in driver.current_url:
        print("✅ TC1: PASS — Valid login successful")
    else:
        print("❌ TC1: FAIL — Valid login failed")
except Exception as e:
    print("❌ TC1: ERROR —", e)

# TC2: Invalid login
driver.get("file:///C:/Users/ayush/OneDrive/Desktop/vs/software/index.html")
try:
    driver.find_element(By.ID, "email").send_keys("admin@example.com")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "loginButton").click()
    time.sleep(1)

    error_text = driver.find_element(By.ID, "errorMsg").text
    if "Invalid credentials" in error_text:
        print("✅ TC2: PASS — Proper error displayed")
    else:
        print("❌ TC2: FAIL — Error message not shown")
except Exception as e:
    print("❌ TC2: ERROR —", e)

# TC3: Empty field validation
driver.get("file:///C:/Users/ayush/OneDrive/Desktop/vs/software/index.html")
try:
    driver.find_element(By.ID, "loginButton").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "errorMsg").text
    if "Fields cannot be empty" in msg:
        print("✅ TC3: PASS — Empty field validation working")
    else:
        print("❌ TC3: FAIL — Empty field validation missing")
except Exception as e:
    print("❌ TC3: ERROR —", e)

# TC4: Logout button
driver.get("file:///C:/Users/ayush/OneDrive/Desktop/vs/software/index.html")
try:
    driver.find_element(By.ID, "email").send_keys("admin@example.com")
    driver.find_element(By.ID, "password").send_keys("admin123")
    driver.find_element(By.ID, "loginButton").click()
    time.sleep(1)

    logout = driver.find_element(By.ID, "logoutButton")
    logout.click()
    time.sleep(1)

    if "index.html" in driver.current_url:
        print("✅ TC4: PASS — Logout successful")
    else:
        print("❌ TC4: FAIL — Logout did not redirect properly")
except Exception as e:
    print("❌ TC6: ERROR —", e)

time.sleep(5)
# TC5: Invalid email format
driver.get("file:///C:/Users/ayush/OneDrive/Desktop/vs/software/index.html")
try:
    email_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "loginButton")

    email_field.send_keys("invalidemail")
    password_field.send_keys("admin123")
    login_btn.click()
    time.sleep(1)

    if "index.html" in driver.current_url:
        print("✅ TC5: PASS — Invalid email format blocked by browser")
    else:
        print("❌ TC5: FAIL — Invalid email format not validated")
except Exception as e:
    print("❌ TC11: ERROR —", e)

print("\n=== Test Execution Complete ===")
driver.quit()
