from selenium import webdriver
class Base():
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.implicitly_wait(5)
   