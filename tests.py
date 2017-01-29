import os

from selenium import webdriver

chromedriver = "/Users/alvinlawson/Desktop/Alvin-Lawson---Flashpoint-Test/chromedriver"

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)

driver.get("https://hub.docker.com/")






#DockerID xpath: //div/main/div/div[1]/header/div/div[2]/div/form/div[1]/div/input

#Emailaddress xpath: //header[@class='Welcome__header___2oKOq']/div/div[2]/div/form/div[2]/div/input

#password xpath: //header[@class='Welcome__header___2oKOq']/div/div[2]/div/form/div[3]/div/input

#signup button xpath: //header[@class='Welcome__header___2oKOq']//button[.='Sign Up']

#search bar xpath: //input[@class='SearchBar__searchInput___34nC3']

#1.search related test case

#2.signup related test case

#3.one login related test case 

