import os

from selenium import webdriver

chromedriver = "/Users/alvinlawson/Desktop/Alvin-Lawson---Flashpoint-Test/chromedriver"

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)

driver.get("https://hub.docker.com/")


#1.search related test case

#2.signup related test case

#3.one login related test case 