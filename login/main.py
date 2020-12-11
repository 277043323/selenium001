

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from automationcodejiang.Page.base_page import Base
from automationcodejiang.login.login import Login


class test(Base):
    url='https://www.codejiang.com'

    def Main(self):
        self.find(By.CSS_SELECTOR,'.no-login').click()
        self.find(By.CSS_SELECTOR,'.login-type>div:nth-child(1)').click()
        return Login(self.driver)