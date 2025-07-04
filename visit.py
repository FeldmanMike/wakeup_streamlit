from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://dc311eta.streamlit.app/"

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get(URL)
print("Page opened, attempting to wake up app...")

time.sleep(5)  # Let page partially load

try:
    button = driver.find_element(By.XPATH, "//button[contains(., 'Yes, get this app back up!')]")
    button.click()
    print("Clicked wake-up button.")
except Exception as e:
    print(f"No wake-up button found or already awake: {e}")

time.sleep(10)  # Optional: let the app fully spin up

driver.quit()
print("Visit complete.")
