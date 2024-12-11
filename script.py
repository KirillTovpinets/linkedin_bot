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

load_cookies(driver, "cookies.pkl")

driver.get("https://www.linkedin.com/feed")


# # # Enter credentials
# username = driver.find_element(By.ID, 'username')
# username.send_keys('kirill.tovpinets@icloud.com')

# password = driver.find_element(By.ID, 'password')
# password.send_keys('x!VT2O0i#gN&')

# # Submit form
# password.send_keys(Keys.RETURN)

time.sleep(10)

# # Once logged in, save cookies to a file
# with open("cookies.pkl", "wb") as f:
#     pickle.dump(driver.get_cookies(), f)

# print("Cookies saved successfully!")

search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
try:
    search_box.send_keys("Python Developer")
    search_box.send_keys(Keys.RETURN)
except Exception as e:
    toggler = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__collapsed-search-button')
    toggler.click()

    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_box.send_keys("Python Developer")
    search_box.send_keys(Keys.RETURN)

time.sleep(5)
easy_apply_filter = driver.find_element(By.XPATH, "//a[contains(., 'Easy apply')]")

easy_apply_filter.click()

time.sleep(10)

jobs = driver.find_elements(By.XPATH, "//ul//li[@class='ember-view']")

for job in jobs:
    job.click()
    time.sleep(5)
    try:
        apply_button = driver.find_element(By.XPATH, "//button[@class='jobs-apply-button']")
        apply_button.click()
        time.sleep(5)
    except Exception as e:
        print("Can't apply")

    next_button = driver.find_element(By.XPATH, "//button[@data-easy-apply-next-button]")
    next_button.click()
    time.sleep(5)

    next_button.click()
    time.sleep(5)

    next_button.click()
    time.sleep(5)

    preview_button = driver.find_element(By.XPATH, "//button[@data-live-test-easy-apply-review-button]")
    preview_button.click()
    time.sleep(5)

    submit_button = driver.find_element(By.XPATH, "//button[@data-live-test-easy-apply-review-button]")
    submit_button.click()
    time.sleep(5)

