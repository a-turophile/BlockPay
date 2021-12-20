from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8080')

time.sleep(10)
elements = browser.find_elements_by_id('mystupidbutton')
elements.click()
browser.find_element_by_css_selector("btn btn-primary btn-lg").click()
