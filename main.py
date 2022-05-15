import time

import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from InternetSpeedBot import InternetSpeedBot


up_val=150
down_val=120


#



speed=InternetSpeedBot()
ham=speed.get_internet_speed()
up_speed=ham[0]
down_speed=ham[1]


if ham[0] < float(up_val) or ham[1]<float(down_val):
    twitter = InternetSpeedBot()
    hash = twitter.twitter_login(up_speed,down_speed)



