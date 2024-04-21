# --- Fill the Google Form ---

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import proces_data

URL = "https://forms.gle/ywJqnXXmXKYSwFaT6"

# Open browser window
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(3)

data_set = proces_data.bike_list()

# Put scraped data into the form
for n in data_set.index:
    field1 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field1.send_keys(data_set["info"][n])
    field2 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field2.send_keys(data_set["price"][n].astype(str))
    field3 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field3.send_keys(data_set["others"][n])
    field4 = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field4.send_keys(data_set["url"][n])

    # Send data
    button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    button.click()

    # Reload the form
    time.sleep(1)
    reload = driver.find_element(By.TAG_NAME, value='a')
    reload.click()

# Close browser window
driver.close()
