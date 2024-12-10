import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Function to save cookies
def save_cookies(driver, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

# Function to load cookies
def load_cookies(driver, file_path):
    with open(file_path, "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

driver = webdriver.Chrome()

# Open LinkedIn login page
driver.get('https://www.linkedin.com/login')

time.sleep(30)

# Once logged in, save cookies to a file
with open("cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("Cookies saved successfully!")

# Close the browser session
driver.quit()

# load_cookies(driver, "cookies.pkl")

# # Enter credentials
# username = driver.find_element(By.ID, 'username')
# username.send_keys('kirill.tovpinets@icloud.com')

# password = driver.find_element(By.ID, 'password')
# password.send_keys('x!VT2O0i#gN&')

# Submit form
# password.send_keys(Keys.RETURN)
