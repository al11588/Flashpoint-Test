import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

        # navigate to hub docker
        self.browser.get('https://hub.docker.com/')

        #1.Search related test case
    def testNumber1(self):
    	#search field
        searchfield = self.browser.find_element_by_xpath("//div/main/div/div[1]/div/nav/section/ul[2]/li/div/form/div/input").send_keys("Flashpoint")
        #searchfield return
        searchfieldenter = self.browser.find_element_by_xpath("//div/main/div/div[1]/div/nav/section/ul[2]/li/div/form/div/input").send_keys(Keys.RETURN)

        #2.Signup related test case
    def testNumber2(self):
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
    def testNumber3(self):
    	#login
    	login = self.browser.find_element_by_link_text("Sign in").click()
    	#username
    	usernamefield2 = self.browser.find_element_by_id("nw_username").send_keys("alvin")
    	#password
    	passwordfield2 = self.browser.find_element_by_id("nw_password").send_keys("lawson")
    	#submitbutton
    	submitbutton2 = self.browser.find_element_by_id("nw_submit").click()

    	#4. Clicks on explore, writes flashpoint on searchfield, presses back button, refreshes
    def testNumber4(self):
    	#clicks on explore
    	explore = self.browser.find_element_by_link_text("Explore").click()
    	#searchfield
    	searchfield2 = self.browser.find_element_by_css_selector("input.SearchBar__searchInput___34nC3").send_keys("Flashpoint")
    	#press back
    	back = self.browser.back()
    	#refreshes
    	refresh = self.browser.refresh()

    	#5. Maximizes window, refreshes, verifies copyright text, 
    def testNumber5(self):
    	#maximize window
    	maximizewindow = self.browser.maximize_window()
    	#refresh
    	refresh = self.browser.refresh()
    	#checks 2016 docker inc
    	checks = self.browser.find_element_by_class_name('Welcome__footerCopy___3AswA')
    	#refreshes twice
    	refresh = self.browser.refresh()
    	#clicks help
    	helpclick = self.browser.find_element_by_link_text("Help").click()






if __name__ == '__main__':
    unittest.main(verbosity=3) 