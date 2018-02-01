from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest



class Download_file(unittest.TestCase):
  download_dir = "C:\\Blog_Downloads"
  chrome_options = webdriver.ChromeOptions()
  preferences = {"download.default_directory": download_dir ,
               "directory_upgrade": True,
               "safebrowsing.enabled": True }
  chrome_options.add_experimental_option("prefs", preferences)
  driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:\\Users\\alam\\Downloads\\chromedriver.exe')
  driver.get("http://127.0.0.1:8000/blog/signin/")
  driver.find_element(By.ID, "your_name").send_keys("ab_12")
  driver.find_element(By.ID, "pass").send_keys("blog12345")
  driver.find_element(By.XPATH, "//button[@type='submit']").click()

  driver.find_element(By.XPATH, "//a[@class='nav-item nav-link nav_text']").click()
  driver.find_element(By.LINK_TEXT,"Download").click()
  time.sleep(20)
  print("Test case passed , Download completed successfully")
  driver.quit()