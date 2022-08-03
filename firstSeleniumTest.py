import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DemoFindElementByName():
      def locate_by_name(self) -> object:
          driver=webdriver.Chrome("/Users/marijanavukovic/Desktop/SeleniumTest/chromedriver 2")
          driver.get("https://staging-ecatch-dashboard.mndnw.sh/sign-in")
          driver.maximize_window()
          print(driver.title)
          driver.find_element(By.NAME, "email").send_keys("marijana@midnow.io")
          time.sleep(4)
findbyname = DemoFindElementByName()
findbyname.locate_by_name()
