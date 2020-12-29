import selenium
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'/Users/averymccarthy/Documents/GitHub/projects/geckodriver.exe')

driver.get("https://selenium.dev")
