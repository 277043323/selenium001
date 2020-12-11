from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from automationcodejiang.Page.base_page import Base
from automationcodejiang.Page.index import Index


class Login(Base):

    def deng(self):
        sleep(3)
        self.find(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div/div[2]/form/div[1]/div/div/input').send_keys("18682229163")
        self.find(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div/div[2]/form/div[2]/div/div/input').send_keys('00000000')
        self.find(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[1]/div/div[2]/form/div[4]/div/div').click()
        # ele.send_keys(Keys.ENTER)
        return Index(self.driver)

