from  .Base import Base

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class Shi(Base):
    def __init__(self, url):
        Base.__init__(self, url)
        list = self.driver.find_elements_by_css_selector('.typecont span a')
        for item in list:
            self.toDetail(item)

    def toDetail(self,el):
        print("============================")
        el.click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

        title = self.driver.find_element_by_css_selector('.cont h1').text
        print(title)

        source = self.driver.find_element_by_css_selector('.source').text
        print(source)

        self.driver.find_element_by_xpath('//*[@alt="译文"]').click()

        WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.contson p')))
        html = self.driver.find_element_by_css_selector('.contson ').get_attribute('innerHTML')
        print(html)
        self.driver.close()

        self.driver.switch_to_window(handles[0]) 
           
        