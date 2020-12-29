import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox

driver = Firefox()

driver.get("https://selenium.dev")
