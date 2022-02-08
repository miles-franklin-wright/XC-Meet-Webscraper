# CSV SETUP

from race_urls import race_urls
from race_scraper import scraper

# https://nj.milesplit.com/meets/446320-njsiaa-xc-meet-of-champions-2021

########################################
########################################

# SELENIUM SETUP
from selenium import webdriver


########################################
########################################

# ALLOW FOR WAIT TIMES
import time

########################################
########################################

# ALLOWS SELENIUM TO RUN IN REPLIT
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-hsm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')



########################################
########################################

# CREATES WEBDRIVER
driver = webdriver.Chrome(options=chrome_options)

#########################################
#########################################

def run_program():
  print('Do you want to obtain the intial urls?')
  run_race_urls = input('Enter Y/N')
  if run_race_urls == "Y":
    race_urls()
  else:
    print('moving on')
  time.sleep(2)
  print('Do you want to run the main scraper?')
  run_scraper = input('Enter Y/N')
  if run_scraper == "Y":
    scraper()
  else:
    print('ending program')


#########################################
#########################################

run_program()