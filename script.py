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

print('Get To Linkedin')
driver.get("https://www.linkedin.com/feed")


# # # Enter credentials
# username = driver.find_element(By.ID, 'username')
# username.send_keys('kirill.tovpinets@icloud.com')

# password = driver.find_element(By.ID, 'password')
# password.send_keys('x!VT2O0i#gN&')

# # Submit form
# password.send_keys(Keys.RETURN)

time.sleep(3)

# # Once logged in, save cookies to a file
# with open("cookies.pkl", "wb") as f:
#     pickle.dump(driver.get_cookies(), f)

# print("Cookies saved successfully!")

search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
print('Put keyword in search box...')
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
print('Filtering jobs by eash apply...')
easy_apply_filter = driver.find_element(By.XPATH, "//a[contains(., 'Easy apply')]")

easy_apply_filter.click()

time.sleep(3)

print('Iterating over jobs...')
jobs = driver.find_elements(By.XPATH, "//main[contains(@class,'scaffold-layout__list-detail')]//ul//li[contains(@class,'scaffold-layout__list-item')]")
for job in jobs:
  job_title = job.find_element(By.CSS_SELECTOR, "a.job-card-list__title--link")
  print('clicking on job...', job_title.text)
  job.click()
  time.sleep(5)
  job_details = driver.find_element(By.XPATH, "//div[@class='jobs-search__job-details--wrapper']")
  try:
      apply_button = job_details.find_element(By.XPATH, ".//button[contains(@class,'jobs-apply-button')]")
      print('clicking on apply button...')
      apply_button.click()
      time.sleep(10)
  except Exception as e:
      print("Can't apply. Probably already applied")
      continue

  modal_dialog = driver.find_element(By.XPATH, "//div[@data-test-modal-id='easy-apply-modal']")
  next_button = modal_dialog.find_element(By.XPATH, ".//button[@data-easy-apply-next-button]")

  while(next_button):
    try:
      next_button.click()
      time.sleep(5)
      next_button = modal_dialog.find_element(By.XPATH, ".//button[@data-easy-apply-next-button]")
    except Exception as e:
      print('No more next buttons')
      break

  preview_button = modal_dialog.find_element(By.XPATH, ".//button[@data-live-test-easy-apply-review-button]")
  preview_button.click()
  time.sleep(5)

  submit_button = modal_dialog.find_element(By.XPATH, ".//button[@data-live-test-easy-apply-submit-button]")
  submit_button.click()
  time.sleep(5)

  success_dialog =  driver.find_element(By.XPATH, "//div[@aria-labelledby='post-apply-modal']")
  close_button = success_dialog.find_element(By.XPATH, ".//button[@data-test-modal-close-btn]")
  close_button.click()
  time.sleep(5)

