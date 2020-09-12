from  .Base import Base
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import requests
import urllib.parse
import re

class Mp3(Base):
    count = 0
    index = 0
    url = ''
    def __init__(self, url, path):
        self.url = url
        self.path = path

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)
       
            
        
       
    def start(self): 
        alist = self.driver.find_elements_by_css_selector('.ny_l li a')
        hrefList = []
        for a in alist:
            href = a.get_attribute('href')
            hrefList.append(href)
        for href in hrefList:
            self.getMp3(href)
            

    def getMp3(self, href):
      
        self.driver.get(href)
        iframe = self.driver.find_elements_by_tag_name("iframe")[0]
        
        self.driver.switch_to.frame(iframe)
        audio = WebDriverWait(self.driver, 30, 0.2).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'audio')))
        # audio = self.driver.find_element_by_css_selector('audio')
        src = ''
        while True:
            src = audio.get_attribute('src')
            print('-----------')
            if src:
                break
            
            sleep(0.2)
        print('src====',src)
        self.download(src)
        self.driver.switch_to.default_content()
        sleep(5)


    def download(self, src):
        src = urllib.parse.unquote(src)
        matchObj = re.match( r'.*\/(.*\.mp3).*', src, re.M|re.I)
       
        name = matchObj.group(1)

        response = requests.get(src).content
        # 以二进制的形式写入文件中
        f = open(self.path + r'\{}'.format(name), 'wb')
        f.write(response)
        f.close()


