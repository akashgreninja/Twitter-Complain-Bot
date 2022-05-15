import time



from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


EMAIL_ID="Your Email Id"
PASSWORD="Password "
Username="Username "
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)


class InternetSpeedBot:
    def __init__(self):
        self.up=150,
        self.down=130,
        # self.twitter_login()



    def get_internet_speed(self):
        charlie=[]
        driver.get('https://www.speedtest.net/')

        G0 = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        G0.click()
        time.sleep(30)
        download=driver.find_element(By.CSS_SELECTOR,'.download-speed')
        # print(download.text)
        download_speed=float(download.text)
        charlie.append(download_speed)

        time.sleep(20)
        Upload=driver.find_element(By.CSS_SELECTOR,'.upload-speed')
        upload_speed=float(Upload.text)
        charlie.append(upload_speed)
        print(charlie)
        return charlie

    def twitter_login(self,up_speed,down_speed):
        driver.get('https://twitter.com/')
        time.sleep(3)
        try:
            sign_in=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
            sign_in.click()

        except:
            sign_in_2=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div[2]/div/div/div/div/div[2]/div/div[1]/a/div/span/span')
            sign_in_2.click()
        time.sleep(3)
        email=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(EMAIL_ID)
        time.sleep(3)
        Next=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        Next.click()
        time.sleep(3)
        try:
            safety=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            safety.send_keys(Username)
            Next_2=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
            Next_2.click()
            time.sleep(3)
            password=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(PASSWORD)

        except:
            password=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(PASSWORD)
        Log_in=driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        Log_in.click()
        time.sleep(3)
        Post=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

        Post.send_keys(f"hey @Jio this is your internet speed today Download {up_speed} and Upload {down_speed} and i am supposed to get 150/120 ")
        time.sleep(2)
        send = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send.click()
        time.sleep(2)
        driver.quit()





