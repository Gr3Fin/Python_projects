# --- Fill the Google Form ---

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import proces_data

URL = "Link to Google Forms"

# Open browser window
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(3)

data_set = proces_data.bed_list()

# Put scraped data into the form
for n in range(data_set.count()["info"]):
    field1 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field1.send_keys(data_set["info"].iloc[n])
    field2 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field2.send_keys(data_set["price"].iloc[n])
    field3 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field3.send_keys(data_set["url"].iloc[n])

    # Send data
    button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    button.click()

    # Reload the form
    time.sleep(1)
    reload = driver.find_element(By.TAG_NAME, value='a')
    reload.click()

# Close browser window
driver.close()
