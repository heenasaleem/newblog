import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import autoit


import time
import SignIn

class MainPageLocators():
    """A class for main page locators. All main page locators should come here"""
    SEARCH_Title = (By.ID, "id_title")
    SEARCH_Body = (By.ID, "id_body")
    SEARCH_Post = (By.XPATH, "//button[@type='submit']")
    SEARCH_searchfield = (By.XPATH, "//input[@type='search']")
    Upload_Link= (By.XPATH, "//a[text()='upload file']")
    Browse_button=(By.XPATH, "//input[@id='id_file']")
    Upload_button = (By.XPATH, "//button[@type='submit']")

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class Write_BlogForm(BasePage):
        """Home page action methods come here."""
        def search_title(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_Title)
            search_input.send_keys(search_query)
        def search_body(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_Body)
            search_input.send_keys(search_query)
        def click_PostButton(self):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_Post)
            search_input.click()
        def assertion(self):
            """Triggers the search"""
            if self.driver.find_element(*MainPageLocators.SEARCH_searchfield).is_displayed():
                print(self.driver.find_element(*MainPageLocators.SEARCH_searchfield).text)
                print("Test case passed")
            else:
                print("Test case failed")
        def click_UploadLink(self):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.Upload_Link)
            search_input.click()
        def click_Browse(self):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.Browse_button)
            search_input.send_keys("C:\\Users\\alam\\Desktop\\File1.xlsx")
        def click_Browse_Invalid(self):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.Browse_button)
            search_input.send_keys("C:\\Users\\alam\\Desktop\\File1.txt")
        def click_Upload_button(self):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.Upload_button)
            search_input.click()


class Write_Blog_1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\alam\\Downloads\\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/blog/signin/")
    def tearDown(self):
        self.driver.close()
    def test_WriteBlog(self):
        SignIn.Blog.test_Successful_Login(self)
        main_page = Write_BlogForm(self.driver)
        main_page.search_title("test_blog_1")
        main_page.search_body("This is my new Blog")
        main_page.click_PostButton()
        main_page.assertion()
    def test_WriteBlog_titleBlank(self):
        SignIn.Blog.test_Successful_Login(self)
        main_page = Write_BlogForm(self.driver)
        main_page.search_title("")
        main_page.search_body("This is my new Blog")
        main_page.click_PostButton()
        main_page.assertion()
    def test_WriteBlog_Bodyblank(self):
        SignIn.Blog.test_Successful_Login(self)
        main_page = Write_BlogForm(self.driver)
        main_page.search_title("Test Blog")
        main_page.search_body("")
        main_page.click_PostButton()
        main_page.assertion()
    def test_WriteBlog_blankValues(self):
        SignIn.Blog.test_Successful_Login(self)
        main_page = Write_BlogForm(self.driver)
        main_page.search_title("")
        main_page.search_body("")
        main_page.click_PostButton()
        main_page.assertion()
    def test_Upload_Link_validFormat(self):
        SignIn.Blog.test_Successful_Login(self)
        main_page = Write_BlogForm(self.driver)
        main_page.click_UploadLink()
        SignIn.LoginForm.timesleep(self)
        main_page.click_Browse()
        main_page.click_Upload_button()
        SignIn.LoginForm.timesleep(self)
        main_page.assertion()

    def test_Upload_Link_InvalidFormat(self):
        SignIn.Blog.test_Successful_Login(self)
        main_page = Write_BlogForm(self.driver)
        main_page.click_UploadLink()
        SignIn.LoginForm.timesleep(self)
        main_page.click_Browse_Invalid()
        main_page.click_Upload_button()
        SignIn.LoginForm.timesleep(self)
        main_page.assertion()






