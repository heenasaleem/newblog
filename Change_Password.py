import SignIn
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver

class MainPageLocators():

  old_password =  (By.ID, "id_old_password")
  new_password = (By.ID, "id_new_password1")
  New_password_confirmation = (By.ID, "id_new_password2")
  Save = (By.XPATH, "//button[@type='submit']")
  Login = (By.XPATH, "//button[@type='submit']")

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class ChangePassword_Page(BasePage):
        """Home page action methods come here."""
        def enter_oldPassword(self,search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.old_password)
            search_input.send_keys(search_query)

        def enter_NewPassword(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.new_password)
            search_input.send_keys(search_query)
        def confirm_NewPassword(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.New_password_confirmation)
            search_input.send_keys(search_query)
        def Click_SavePassword(self):
            search_input = self.driver.find_element(*MainPageLocators.Save)
            search_input.click()

class ChangePassword(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\alam\\Downloads\\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/blog/signin/")

    def test_Check_passwordChanges_Successfully(self):
       SignIn.Blog.test_Successful_Login(self)
       self.driver.find_element(By.XPATH, "//a[text()='Change password']").click()
       main_page = ChangePassword_Page(self.driver)
       main_page.enter_oldPassword("blog12345")
       main_page.enter_NewPassword("blog12345")
       main_page.confirm_NewPassword("blog12345")
       SignIn.LoginForm.timesleep(self)
       main_page.Click_SavePassword()
       SignIn.LoginForm.timesleep(self)
       assert(self.driver.find_element(By.XPATH, "//button[@type='submit']").is_displayed())


    def tearDown(self):
        self.driver.close()