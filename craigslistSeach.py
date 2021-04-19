import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common import service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv



wantFree = input("Want free? Y/N ")
whatWant = input("What you want? ")
browser = webdriver.Firefox()

if wantFree == "Y":
    
        browser.get('https://losangeles.craigslist.org/search/sfv/zip?')
        
        searchForm = browser.find_element_by_id("query")
        searchForm.click()
        
        searchForm.send_keys(whatWant)
        sendClick = browser.find_element_by_class_name("searchbtn")
        sendClick.click()
    
else:
    
        browser.get('https://losangeles.craigslist.org/search/sfv/sss?')

        searchForm = browser.find_element_by_id("query")
        searchForm.click()
        
        searchForm.send_keys(whatWant)
        sendClick = browser.find_element_by_class_name("searchbtn")
        sendClick.click()

    
https://docs.google.com/spreadsheets/d/1YYoTUyEtcjl9GmSHc3pOcPs8myI8n3pzB0AggDCIJ2I/edit?usp=sharing