
import SignIn
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver

class MainPageLocators():

  Username_label =  (By.XPATH, "//h5[text()='ab_12']")
  username_icon = (By.XPATH, "//a[text()='ab_12']")


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class ProfilePage(BasePage):
        """Home page action methods come here."""
        def assertion(self):
            """Triggers the search"""
            userProfile = self.driver.find_element(*MainPageLocators.Username_label)
            userLoggedIn = self.driver.find_element(*MainPageLocators.username_icon)
            print(userProfile.text)
            if userProfile.text == userLoggedIn.text:
                print("Test case passed, the user logged in is the same as updated from profile")
            else:
                print("test case failed")

        def logOut(self):
            userLoggedIn = self.driver.find_element(*MainPageLocators.username_icon)
            userLoggedIn.click()
            print("Test case passed, User logged out successfully")

class Profile_vaidate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\alam\\Downloads\\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/blog/signin/")

    def test_LogIn_CheckProfile_LogOut(self):
       SignIn.Blog.test_Successful_Login(self)
       self.driver.find_element(By.XPATH, "//a[text()='My Profile']").click()
       main_page = ProfilePage(self.driver)
       SignIn.LoginForm.timesleep(self)
       main_page.assertion()
       SignIn.LoginForm.timesleep(self)
       main_page.logOut()

    def tearDown(self):
        self.driver.close()