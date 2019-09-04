from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        email = bot.find_element_by_class_name("js-username-field")
        password = bot.find_element_by_class_name("js-password-field")
      
        email.send_keys(self.username)
        password.send_keys(self.password)

        password.send_keys(Keys.RETURN)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(5)

        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            tweets = bot.find_elements_by_class_name('r-1adg3ll')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            print(links)
        


bot = TBot("playwordssd","Dlaminilqn2")
bot.login()
bot.like_tweet("HandsOffAKA")
