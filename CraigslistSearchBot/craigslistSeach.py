import sys, os
from os import link
from typing import Counter


from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import tkinter as tk
import numpy as np

import Face.interface as interface

wantFree = input("Want free? Y/N ")


whatWant = interface.interface()
browser = webdriver.Firefox()
fileRead = open('F:\Documents\projects\Craigsearchbot\craigsheet.csv', 'r', newline='')
fileWrite = open('F:\Documents\projects\Craigsearchbot\craigsheet.csv', 'w', newline='')
mywriter = csv.writer(fileWrite, delimiter=',')

if wantFree == "Y":
    
        browser.get('https://losangeles.craigslist.org/search/sfv/zip?')
        
        searchForm = browser.find_element_by_id("query")
        searchForm.click()
        
        for i in whatWant:
                        
                searchForm.send_keys(i)
                sendClick = browser.find_element_by_class_name("searchbtn")
                sendClick.click()

                ulSelector = browser.find_element_by_class_name("rows")
                liClass = ulSelector.find_elements_by_tag_name("li")
                with open('F:\Documents\projects\Craigsearchbot\craigsheet.csv', 'w', newline='') as file:
                        for links in liClass:
                                linkyLinks = links.find_element_by_xpath('./a').get_attribute('href')
                                print(linkyLinks)
                                
                                mywriter = csv.writer(file, delimiter=' ')
                                mywriter.writerows([linkyLinks])
                

else:

        browser.get('https://losangeles.craigslist.org/search/sfv/sss?')
        linkyLinks = []
        linkDictionary = []
        for i in whatWant:
                
                searchForm = browser.find_element_by_id("query")
                searchForm.click()
                        
                searchForm.send_keys(i)
                sendClick = browser.find_element_by_class_name("searchbtn")
                sendClick.click()

                ulSelector = browser.find_element_by_class_name("rows")
                liClass = ulSelector.find_elements_by_tag_name("li")
                for links in liClass:
                        
                        linkyLinks.append(links.find_element_by_xpath('./a').get_attribute('href'))
                                
                for i in range(len(linkyLinks)):
                        linkDictionary.append(linkyLinks[i])
                print(linkDictionary)
                mywriter.writerow([linkDictionary])
                browser.get('https://losangeles.craigslist.org/search/sfv/sss?')
                
                
                 
