from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

URL = "https://twitter.com/i/flow/login"


class ScoreTweet:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(URL)

    def tweet_score(self, score, q_no, cred):
        time.sleep(5)
        # Sometimes X asks about the username.
        try:
            user = self.driver.find_element(By.NAME, value="text")
            user.send_keys(cred[0], Keys.ENTER)
        except NoSuchElementException:
            mail = self.driver.find_element(By.NAME, value='text')
            mail.send_keys(cred[1], Keys.ENTER)
        else:
            time.sleep(3)
            password = self.driver.find_element(By.NAME, value="password")
            password.send_keys(cred[2], Keys.ENTER)

        time.sleep(8)
        tweet = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                         '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                         '1]/div/div/div/div[2]/div['
                                                         '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                                         '1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey! I have just completed the Trivia general knowledge quiz.\n"
                        f"Here is my score: {score}/{q_no}\nCan you beat it?")
