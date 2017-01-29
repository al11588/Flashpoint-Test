import unittest
from selenium import webdriver

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://hub.docker.com/')

    def testSearch(self):
        elem = self.browser.find_element_by_xpath("//header[@class='Welcome__header___2oKOq']//button[.='Sign Up']")
        elem.click()
        #elem.send_keys('selenium')


if __name__ == '__main__':
    unittest.main(verbosity=2)
