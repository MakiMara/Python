import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DemoFindElementByName():
      def locate_by_name(self) :
          driver=webdriver.Chrome("/Users/marijanavukovic/Desktop/SeleniumTest/chromedriver 2")
          driver.get("https://staging-ecatch-dashboard.mndnw.sh/sign-in")
          driver.maximize_window()
          print(driver.title)
          driver.find_element(By.NAME, "email").send_keys("marijana@midnow.io")
          driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Mara199!")
          time.sleep(4)
findbyname = DemoFindElementByName()
findbyname.locate_by_name()

#find element by Xpath

# / - step by step comes or //
"""
nodename	Selects all nodes with the name "nodename"
/	Selects from the root node
//	Selects nodes in the document from the current node that match the selection no matter where they are
.	Selects the current node
..	Selects the parent of the current node
@	Selects attributes
/bookstore/book[1]	Selects the first book element that is the child of the bookstore element.
Note: In IE 5,6,7,8,9 first node is[0], but according to W3C, it is [1]. To solve this problem in IE, set the SelectionLanguage to XPath:

In JavaScript: xml.setProperty("SelectionLanguage","XPath");
/bookstore/book[last()]	Selects the last book element that is the child of the bookstore element
/bookstore/book[last()-1]	Selects the last but one book element that is the child of the bookstore element
/bookstore/book[position()<3]	Selects the first two book elements that are children of the bookstore element
//title[@lang]	Selects all the title elements that have an attribute named lang
//title[@lang='en']	Selects all the title elements that have a "lang" attribute with a value of "en"
/bookstore/book[price>35.00]	Selects all the book elements of the bookstore element that have a price element with a value greater than 35.00
/bookstore/book[price>35.00]/title	Selects all the title elements of the book elements of the bookstore element that have a price element with a value greater than 35.00

"""
#find element by link text


