from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        try:
            email = WebDriverWait(bot, 30).until(
                EC.presence_of_element_located((By.NAME, 'session[username_or_email]')))
            password = WebDriverWait(bot, 30).until(
                EC.presence_of_element_located((By.NAME, 'session[password]')))
            email.clear()
            password.clear()
            email.send_keys(self.username)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(10)
        finally:
            bot.quit()

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(3)

        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            # print(links)

            for link in links:
                bot.get('https://twitter.com'+link)

                try:
                    bot.find_element_by_class_name('HeartAnimation')
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)


ed = TwitterBot('elviskamweya@gmail.com', 'misharnold41')
ed.login()
