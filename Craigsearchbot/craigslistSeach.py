from os import link

from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import tkinter as tk

from Craigsearchbot.interface import interface



wantFree = input("Want free? Y/N ")
interface()
whatWant = input("What you want? ")
browser = webdriver.Firefox()

if wantFree == "Y":
    
        browser.get('https://losangeles.craigslist.org/search/sfv/zip?')
        
        searchForm = browser.find_element_by_id("query")
        searchForm.click()
        
        searchForm.send_keys(whatWant)
        sendClick = browser.find_element_by_class_name("searchbtn")
        sendClick.click()

        ulSelector = browser.find_element_by_class_name("rows")
        liClass = ulSelector.find_elements_by_tag_name("li")
        with open('F:\Documents\projects\Craigsearchbot\craigsheet.csv', 'w', newline='') as file:
                for links in liClass:
                        linkyLinks = [links.find_element_by_xpath('./a').get_attribute('href')]
                        print(linkyLinks)
                        
                        mywriter = csv.writer(file, delimiter=' ')
                        mywriter.writerows([linkyLinks])
        

else:
    
        browser.get('https://losangeles.craigslist.org/search/sfv/sss?')

        searchForm = browser.find_element_by_id("query")
        searchForm.click()
        
        searchForm.send_keys(whatWant)
        sendClick = browser.find_element_by_class_name("searchbtn")
        sendClick.click()

        ulSelector = browser.find_element_by_class_name("rows")
        liClass = ulSelector.find_elements_by_tag_name("li")
        with open('F:\Documents\projects\Craigsearchbot\craigsheet.csv', 'w', newline='') as file:
                for links in liClass:
                        linkyLinks = [links.find_element_by_xpath('./a').get_attribute('href')]
                        print(linkyLinks)
                        
                        mywriter = csv.writer(file, delimiter=' ')
                        mywriter.writerows([linkyLinks])