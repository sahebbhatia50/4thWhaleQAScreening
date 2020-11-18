import pytest
from selenium import webdriver
import selenium
from testscripts.configuration import setup
from pageobjects.LoginPage import Login
from selenium.webdriver.common.action_chains import ActionChains
from utilities.readProperties import ReadConfig

class Test_Valid_Login:
    baseURL = ReadConfig.getApplicationURL() # Used config.ini and ReadProperties file so that it can read and take the common data from those files without hardcoding it.
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

#this method validates the title of the application
    def test_title(self,setup):
        self.driver = setup                                       #Made use of python fixture to prevent writing Reusable steps again and again
        self.driver.get(self.baseURL)                             #lOGGING Into THE APPLICATION BASED ON THE url
        self.driver.title                                         #Getting the title from the PAGE
        #Assertion to validate if logged in into the correct URL
        if self.driver.title == "Rabbits Adult Site Reviews":
            assert True
        else:
            assert False

# this explains the valid Successfull login and logout to the application
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()              #Maximizing the Browser Window
        self.lp=Login(self.driver)                 #Creating an object of Login class
        self.lp.click_enter()                      #Clicking on the Enter application button
        self.lp.driver.implicitly_wait(15)         #Giving a wait time for the application to load
        self.lp.click_user()                       #Clicking on the user icon
        self.lp.click_loginicon()                  #Clicking on the LOG IN button
        self.lp.driver.implicitly_wait(5)          #Giving a wait time for the application to load
        self.lp.enter_username(self.username)      #Entering username which is a valid username
        self.lp.enter_password(self.password)      #Entering password which is a valid password
        self.lp.click_submit()                     #Clicking on the Submit button
        self.lp.driver.implicitly_wait(2)          #Giving a wait time for the Home Page to load
        self.lp.click_logout()                     #Clicking on the Log Out button



