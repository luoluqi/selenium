from  .Base import Base
from ..util.Wechat import Wechat

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class Shi(Base):
    wechat = Wechat()
    bookId = ''
    categoryId = ''
    def __init__(self, url, categoryId):
        Base.__init__(self, url)
        self.categoryId = categoryId

    def isElementExist(self,selector):
        try:
            ele = self.driver.find_element_by_css_selector(selector)
            return True
        except:
            return False
        
       
    def start(self):
        list = self.driver.find_elements_by_css_selector('.typecont span a')

        self.getBook(self.categoryId)

        # self.getChater(list[0])
        for item in list:
            item.click()
            handles = self.driver.window_handles
            if (len(handles) == 1):
                continue
            self.driver.switch_to.window(handles[1])
            try:
                self.getChater()
            except:
                pass
            
            self.driver.close()
            self.driver.switch_to_window(handles[0]) 

    def getBook(self, categoryId):
        name = self.driver.find_element_by_css_selector('.title h1').text
      

        self.bookId = self.wechat.addBook(name=name, categoryId=name, author='', desc='', order=1)

    def getChater(self):    
        # 名称
        name = self.driver.find_element_by_css_selector('.cont h1').text
       
        # 作者来源
        author = self.driver.find_element_by_css_selector('.source').text
       
        # 原文
        if (self.isElementExist("#sonsyuanwen [alt='译文']")):

            el = self.driver.find_element_by_css_selector("#sonsyuanwen [alt='译文']")
            if (el.is_displayed()):
                el.click()
                WebDriverWait(self.driver, 30, 0.2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.contson p')))
        else:
            pass
        yuanWen = self.driver.find_element_by_css_selector('.contson ').get_attribute('innerHTML')
        
       
        # 译文
        if (self.isElementExist("div[id^='fanyi'] a:last-child")):
            aEl = self.driver.find_element_by_css_selector("div[id^='fanyi'] a:last-child")
            aEl.click()
            el = WebDriverWait(self.driver, 30, 0.2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^='fanyiquan'] .contyishang")))
            
        else:
            el = self.driver.find_elements_by_css_selector(".contyishang")[0]
          
        yiWen = el.get_attribute('outerHTML')

        # 赏析
        self.driver.find_element_by_css_selector("div[id^='shangxi'] a:last-child").click()
        el = WebDriverWait(self.driver, 30, 0.2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^='shangxiquan'] .contyishang")))
        shangXi = el.get_attribute('outerHTML')
       
        # 写作手法
        # self.driver.find_element_by_css_selector('#shangxi3  a:last-child').click()
        # el = WebDriverWait(self.driver, 30, 0.2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#shangxiquan3 .contyishang')))
        # xieZuo = el.get_attribute('outerHTML')
       

        original = '''
            <div style="padding:0px 10px;">
                <h1 style="margin:20px 0">{name}</h1>
                <div style="margin:20px 0;color: #b12222;">{author}</div>
                <div style="margin:20px 0">{yuanWen}</div>
               
                <div style="margin:20px 0">{yiWen}</div>
               
                <div style="margin:20px 0">{shangXi}</div>
            </div>
        '''
        original = original.format(name=name, author=author, yuanWen=yuanWen, yiWen=yiWen,\
            shangXi=shangXi)
        self.wechat.addChapter(bookId=self.bookId, name=name, original=original,translation='',order=1)

        
           
        