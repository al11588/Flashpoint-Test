import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

        # navigate to hub docker
        self.browser.get('https://hub.docker.com/')

        #1.Search related test case
    def testSearch(self):
    	#search field
        searchfield = self.browser.find_element_by_xpath("//div/main/div/div[1]/div/nav/section/ul[2]/li/div/form/div/input").send_keys("Flashpoint")
        #searchfield return
        searchfieldenter = self.browser.find_element_by_xpath("//div/main/div/div[1]/div/nav/section/ul[2]/li/div/form/div/input").send_keys(Keys.RETURN)

        #2.Signup related test case
    def testSignup(self):
    	#docker ID field
    	dockeridfield = self.browser.find_element_by_xpath("//div/main/div/div[1]/header/div/div[2]/div/form/div[1]/div/input").send_keys("alvindockerid")
    	#email field
    	emailfield = self.browser.find_element_by_xpath("//header[@class='Welcome__header___2oKOq']/div/div[2]/div/form/div[2]/div/input").send_keys("alvinpassword@gmail.com")
    	#password field
    	passwordfield = self.browser.find_element_by_xpath("//header[@class='Welcome__header___2oKOq']/div/div[2]/div/form/div[3]/div/input").send_keys("alvinpassword@gmail.com")
    	#signup button
    	signupbutton = self.browser.find_element_by_xpath("//header[@class='Welcome__header___2oKOq']//button[.='Sign Up']") #signup button
        signupbutton.click()# signup button is clicked

        #3.One login related test case
    def testThisOneLogin(self):
    	#login
    	login = self.browser.find_element_by_link_text("Sign in").click()
    	#username
    	usernamefield2 = self.browser.find_element_by_id("nw_username").send_keys("alvin")
    	#password
    	passwordfield2 = self.browser.find_element_by_id("nw_password").send_keys("lawson")
    	#submitbutton
    	submitbutton2 = self.browser.find_element_by_id("nw_submit").click()


if __name__ == '__main__':
    unittest.main(verbosity=3)

#DockerID xpath: //div/main/div/div[1]/header/div/div[2]/div/form/div[1]/div/input

#Emailaddress xpath: //header[@class='Welcome__header___2oKOq']/div/div[2]/div/form/div[2]/div/input

#password xpath: //header[@class='Welcome__header___2oKOq']/div/div[2]/div/form/div[3]/div/input

#signup button xpath: //header[@class='Welcome__header___2oKOq']//button[.='Sign Up']

#search bar xpath: //input[@class='SearchBar__searchInput___34nC3']

#1.search related test case

#2.signup related test case

#3.one login related test case 