# --- Fill the form in google ---

from selenium import webdriver
from data import Data
from selenium.webdriver.common.by import By
import time

URL = "https://forms.gle/KzEnUy1xy5YCC6Jv8"

# Keep Chrome browser window open after opening
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open Chrome at desired web page
driver = webdriver.Chrome(options=chrome_options)  # initializing an object Chrome
driver.get(URL)
time.sleep(3)

data_set = Data().find_data()

# Put scraped data into the form
for n in range(len(data_set[0])):
    field1 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field1.send_keys(data_set[0][n])
    field2 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field2.send_keys(data_set[1][n])
    field3 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field3.send_keys(data_set[2][n])

    # Send data
    button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    button.click()

    # Reload the form
    time.sleep(1)
    reload = driver.find_element(By.TAG_NAME, value='a')
    reload.click()

# driver.close()
