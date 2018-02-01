import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MainPageLocators():
    """A class for main page locators. All main page locators should come here"""
    SEARCH_username = (By.ID, "your_name")
    SEARCH_password = (By.ID, "pass")
    SEARCH_Loginbutton = (By.XPATH, "//button[@type='submit']")
    SEARCH_Logo = (By.XPATH, "//a[@class='nav-item nav-link nav_text']")
    SEARCH_ErrorMessage =  (By.XPATH, "//div[@id='alert_msg']")
    SEARCH_RequiredMessage =(By.CLASS_NAME,"errorlist")

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class LoginForm(BasePage):
        """Home page action methods come here."""

        def search_username(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_username)
            search_input.send_keys(search_query)

        def search_password(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_password)
            search_input.send_keys(search_query)

        def click_button(self):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_Loginbutton)
            search_input.click()
        def assertion_logo(self):
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_Logo)
            assert(search_input)
            print(search_input.text)
        def assertion_errorMessage(self):
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_ErrorMessage)
            assert(search_input)
            print(search_input.text)
        def assertion_requiredField(self):
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_RequiredMessage)
            print(search_input.text)

        def timesleep(self):
            time.sleep(20)


class Blog(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\alam\\Downloads\\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/blog/signin/")


    def test_Successful_Login(self):
        main_page = LoginForm(self.driver)
        self.driver.implicitly_wait(20)
        main_page.search_username("ab_12")
        main_page.search_password("blog12345")
        main_page.click_button()
        main_page.timesleep()
        main_page.assertion_logo()

    def test_ErrorMessageDisplays_InValid_username(self):
        main_page = LoginForm(self.driver)
        self.driver.implicitly_wait(20)
        main_page.search_username("ab_13")
        main_page.search_password("blog12345")
        main_page.click_button()
        main_page.assertion_errorMessage()
        if ((self.driver.find_element(*MainPageLocators.SEARCH_username).text)=="" and (self.driver.find_element(*MainPageLocators.SEARCH_password).text)==""):
            print ("Test case passed")

    def test_ErrorMessageDisplays_InValid_password(self):
        main_page = LoginForm(self.driver)
        self.driver.implicitly_wait(20)
        main_page.search_username("ab_12")
        main_page.search_password("blog1")
        main_page.click_button()
        main_page.assertion_errorMessage()
        if ((self.driver.find_element(*MainPageLocators.SEARCH_username).text)=="" and (self.driver.find_element(*MainPageLocators.SEARCH_password).text)==""):
            print ("Test case passed")

    def test_MessageDisplays_RequiredField(self):
        main_page = LoginForm(self.driver)
        self.driver.implicitly_wait(20)
        main_page.search_username("")
        main_page.search_password("")
        main_page.click_button()
        main_page.assertion_requiredField()
    #bug 1
    def test_RequiredField_Errormessage_Both(self):
        main_page = LoginForm(self.driver)
        self.driver.implicitly_wait(20)
        main_page.search_username("")
        main_page.search_password("")
        main_page.click_button()
        if self.driver.find_element(*MainPageLocators.SEARCH_ErrorMessage).is_displayed():
            print("Test case failed, Error message should not be displayed here")

    def test_MessageDisplays_RequiredField_username(self):
        main_page = LoginForm(self.driver)
        self.driver.implicitly_wait(20)
        main_page.search_username("")
        main_page.search_password("blog12345")
        main_page.click_button()
        main_page.assertion_requiredField()
    # bug 2
    def test_MessageDisplays_RequiredField_password(self):
        main_page = LoginForm(self.driver)
        self.driver.implicitly_wait(20)
        main_page.search_username("ab_12")
        main_page.search_password("")
        main_page.click_button()
        main_page.assertion_requiredField()
    def test_ClearFields_forInvalidLogin(self):
        main_page = LoginForm(self.driver)
        self.driver.implicitly_wait(20)
        main_page.search_username("ab_12")
        main_page.search_password("blog1")
        main_page.click_button()
        main_page.assertion_errorMessage()
        if ((self.driver.find_element(*MainPageLocators.SEARCH_username).text)=="" and (self.driver.find_element(*MainPageLocators.SEARCH_password).text)==""):
            print ("Test case passed")

    def tearDown(self):
        self.driver.close()




