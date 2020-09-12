from src.entity.Mp3 import Mp3
from selenium import webdriver
import urllib.parse
import re

m = Mp3('https://www.ysts8.vip/Yshtml/Ys974.html', r'E:\天龙八部')
m.start()

# str = 'http://177d.5txs.net:8000/%E6%AD%A6%E4%BE%A0%E5%B0%8F%E8%AF%B4/%E7%AC%91%E5%82%B2%E6%B1%9F%E6%B9%96190%E9%9B%86_%E9%87%91%E5%B3%B0/%E7%AC%91%E5%82%B2%E6%B1%9F%E6%B9%96021.mp3?1012490266025x1599925811x1012496396685-4ff5d55cb8596f568e9c768a8ee7017a+dcaRQR192+'

# str=urllib.parse.unquote(str)
# matchObj = re.match( r'.*\/(.*\.mp3).*', str, re.M|re.I)
# print(str)
# print( matchObj.group(1))

