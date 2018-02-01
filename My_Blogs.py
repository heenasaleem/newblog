import SignIn
import Write_Blog
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
class MainPageLocators():

  Delete_Icon =  (By.XPATH, "//img[@class='img-del']")
  Edit_Icon = (By.XPATH, "//img[@class='img-edit']")
  Search_title=(By.XPATH, "//p[@class='card-text' and text()='good eve']")
  blogs_title =(By.XPATH, "//a[@class='nav-item nav-link nav_text']")
  SEARCH_Post = (By.XPATH, "//button[@type='submit']")

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class MyBlog_func(BasePage):
    """Home page action methods come here."""

    def search_delete_icon(self):
        """Triggers the search"""
        search_input = self.driver.find_element(*MainPageLocators.Delete_Icon)
        search_input.click()
    def search_edit_icon(self):
        """Triggers the search"""
        search_input = self.driver.find_element(*MainPageLocators.Edit_Icon)
        search_input.click()
    def assertion_title(self):
        search_input = self.driver.find_element(*MainPageLocators.Search_title)
        assert (search_input)

class MyBlogs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\alam\\Downloads\\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/blog/signin/")

    def test_deleteIcon(self):
       SignIn.Blog.test_Successful_Login(self)
       main_page = MyBlog_func(self.driver)
       self.driver.find_element(*MainPageLocators.blogs_title).click()
       SignIn.LoginForm.timesleep(self)
       main_page.search_delete_icon()
       SignIn.LoginForm.timesleep(self)
       main_page.assertion_title()

    def test_EditIcon_Working(self):
       SignIn.Blog.test_Successful_Login(self)
       main_page = MyBlog_func(self.driver)
       self.driver.find_element(*MainPageLocators.blogs_title).click()
       main_page.search_edit_icon()
       SignIn.LoginForm.timesleep(self)
       if self.driver.find_element(*MainPageLocators.SEARCH_Post).is_displayed():
           print("Test passed")
       else:
           print("Test failed")
    def test_navigation_afterEdit(self):
        SignIn.Blog.test_Successful_Login(self)
        main_page = MyBlog_func(self.driver)
        self.driver.find_element(*MainPageLocators.blogs_title).click()
        main_page.search_edit_icon()
        main_page1=Write_Blog.Write_BlogForm(self.driver)
        main_page1.search_title("navigation_test")
        main_page1.search_body("this is navigation test after editing blog")
        main_page1.click_PostButton()
        main_page1.assertion()


    def tearDown(self):
        self.driver.close()

