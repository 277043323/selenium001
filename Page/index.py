from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from automationcodejiang.Page.base_page import Base
from automationcodejiang.Page.scratch import Scratch


class Index(Base):
    def couser(self):
        self.find(By.CSS_SELECTOR,'.menu-list li:nth-child(2)').click()
        self.find(By.CSS_SELECTOR,'.menu-list li:nth-child(3)').click()
        print(self.driver.window_handles)
        return Scratch(self.driver)