from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from automationcodejiang.Page.base_page import Base


class Scratch(Base):
    def action(self):
        self.swith(-1)
        sleep(5)
        self.find(By.CSS_SELECTOR,'.scratchCategoryMenuRow:nth-child(1)').click()
        #/html/body/div[1]/div/div[5]/div/div[2]/div/div[1]/div/div/div/div[1]/div/div[3]