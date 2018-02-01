import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class MainPageLocators():

    """A class for main page locators. All main page locators should come here"""
    SEARCH_username = (By.ID, "id_username")
    SEARCH_firstname = (By.ID, "id_first_name")
    SEARCH_lastname = (By.ID, "id_last_name")
    SEARCH_email = (By.ID, "id_email")
    SEARCH_password = (By.ID, "id_password")
    SEARCH_ConfirmPassword = (By.ID, "id_confirm_password")
    SEARCH_SignUp = (By.XPATH, "//button[@type='submit']")
    SEARCH_SignUp_Link = (By.LINK_TEXT,"Not a user? Signup here..")
    SEARCH_Reset = (By.XPATH, "//button[@type='reset']")
    SEARCH_Logo = (By.LINK_TEXT,"Not a user? Signup here..")
    SEARCH_ErrorMessage =  (By.XPATH, "//div[@id='alert_msg']")
    SEARCH_RequiredMessage =(By.XPATH,"//div[@id='alert_msg']")

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class Sign_Up_Form(BasePage):
        """Home page action methods come here."""

        def search_username(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_username)
            search_input.send_keys(search_query)
        def search_firstName(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_firstname)
            search_input.send_keys(search_query)
        def search_LastName(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_lastname)
            search_input.send_keys(search_query)

        def search_Email(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_email)
            search_input.send_keys(search_query)

        def search_password(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_password)
            search_input.send_keys(search_query)

        def search_confirm_password(self, search_query):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_ConfirmPassword)
            search_input.send_keys(search_query)

        def signUp_button(self):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_SignUp)
            search_input.click()

        def signUp_link(self):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_SignUp_Link)
            search_input.click()

        def Reset_button(self):
            """Triggers the search"""
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_Reset)
            search_input.click()

        def assertion_logo(self):
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_Logo)
            assert(search_input)
            print("Successful_SignUp -- Test case passed")
            print(search_input.text)

        def assertion_WarningMessage(self):

            if (self.driver.find_element(*MainPageLocators.SEARCH_ErrorMessage).is_displayed()):
                print ("AlertMessageDisplays_InValid_username--Test case passed")
                print(self.driver.find_element(*MainPageLocators.SEARCH_ErrorMessage).text)
            else:
                print("error message not displayed")

        def assertion_requiredField(self):

            if (self.driver.find_element(*MainPageLocators.SEARCH_RequiredMessage).is_displayed()):
                print("Test case passed")
                print(self.driver.find_element(*MainPageLocators.SEARCH_RequiredMessage).text)
            else:
                print("alert for required field message not displayed")
        def reset(self):
            search_input = self.driver.find_element(*MainPageLocators.SEARCH_Reset)
            search_input.click()
            if (self.driver.find_element(*MainPageLocators.SEARCH_username)=="" and self.driver.find_element(*MainPageLocators.SEARCH_firstname)==""
            and self.driver.find_element(*MainPageLocators.SEARCH_lastname)=="" and self.driver.find_element(*MainPageLocators.SEARCH_email)==""
            and self.driver.find_element(*MainPageLocators.SEARCH_password)=="" and self.driver.find_element(*MainPageLocators.SEARCH_ConfirmPassword)==""):
                print ("ClearFields_Reset -- test case passed")
            else:
                print ("ClearFields_Reset--test case failed")


        def timesleep(self):
            time.sleep(10)


class Blog_SignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\alam\\Downloads\\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/blog/signin/")



    def tearDown(self):
        self.driver.close()

    def test_Successful_SignUp(self):   #done
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User_3")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("user3@gmail.com")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("blog12345")
        main_page.signUp_button()
        main_page.timesleep()
        main_page.assertion_logo()

    def test_AlertMessageDisplays_InValid_username(self): #done
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("vjshagy974857?><:{}$% # ^^&&$$")
        main_page.signUp_button()
        main_page.assertion_WarningMessage()

    def test_MessageDisplays_RequiredField_Username(self):
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("test4@gmail.com")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("blog12345")
        main_page.signUp_button()
        main_page.timesleep()
        main_page.assertion_requiredField()

    def test_Same_Username(self):
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("test4@gmail.com")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("blog12345")
        main_page.signUp_button()
        main_page.timesleep()
        main_page.assertion_requiredField()

    def test_Same_Email(self):
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User_5")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("abc@gmail.com")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("blog12345")
        main_page.signUp_button()
        main_page.timesleep()
        main_page.assertion_requiredField()

    def test_MessageDisplays_RequiredField_password(self):
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User_5")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("test6@gmail.com")
        main_page.search_password("")
        main_page.search_confirm_password("blog12345")
        main_page.signUp_button()
        main_page.timesleep()
        main_page.assertion_requiredField()

    def test_MessageDisplays_RequiredField_FirstName(self): #done
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User_5")
        main_page.search_firstName("")
        main_page.search_LastName("Test")
        main_page.search_Email("test6@gmail.com")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("blog12345")
        main_page.signUp_button()
        main_page.timesleep()
        main_page.assertion_requiredField()
    def test_MessageDisplays_RequiredField_LastName(self): #done
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User_5")
        main_page.search_firstName("User1")
        main_page.search_LastName("")
        main_page.search_Email("test6@gmail.com")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("blog12345")
        main_page.signUp_button()
        main_page.timesleep()
        main_page.assertion_requiredField()
    def test_MessageDisplays_RequiredField_Email(self): #done
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User_5")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("blog12345")
        main_page.signUp_button()
        main_page.timesleep()
        main_page.assertion_requiredField()
    #bug
    def test_MessageDisplays_RequiredField_ConfirmPassword(self):
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User_5")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("test6@gmail.com")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("")
        main_page.signUp_button()
        main_page.timesleep()
        if self.driver.find_element_by_xpath("//*[@id='id_confirm_password']//following::div[1]").is_displayed():
            print("Test case passed")
        else:
            print("Test case failed")

    def test_Passwords_DoNotMatch(self):
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User_5")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("test6@gmail.com")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("nhgjsiy34")
        main_page.signUp_button()
        main_page.assertion_requiredField()
        main_page.timesleep()

    def test_Password_Atleast8Chars(self):
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("Test_User_5")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("test6@gmail.com")
        main_page.search_password("blo")
        main_page.search_confirm_password("blo")
        main_page.signUp_button()
        main_page.assertion_requiredField()
        main_page.timesleep()

    #bug
    def test_ClearFields_Reset(self):
        main_page = Sign_Up_Form(self.driver)
        self.driver.implicitly_wait(20)
        main_page.signUp_link()
        main_page.search_username("129")
        main_page.search_firstName("User1")
        main_page.search_LastName("Test")
        main_page.search_Email("test27@gmail.com")
        main_page.search_password("blog12345")
        main_page.search_confirm_password("blog12345")
        main_page.reset()



