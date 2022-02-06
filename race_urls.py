import csv
import time

# SELENIUM SETUP
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-hsm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# DECLARE DRIVER
driver = webdriver.Chrome(options=chrome_options)

# MAIN FUNCTION
def race_urls():
  print('begin cycle, obtaining urls')
  print('obtained urls, cycle closing')



def enter_initial_meet():
  print("please enter meet url")
  url = input()
  print(url)
  return url


def get_initial_meet():
  url = enter_initial_meet()
  driver.get(str(url))
  return url



def get_meet_list():
  meet_list = driver.find_elements(By.XPATH, "//ul[@class='meets']/li/a")
  meet_list_hrefs = []
  for i in meet_list:
    time.sleep(.5)
    print('added to raw', i.get_attribute('href'))
    meet_list_hrefs.append(i.get_attribute('href'))
  return meet_list_hrefs



def clean_meet_list(url):
  url = url
  meet_list = []
  meet_list.append(url)
  raw_meet_list_hrefs = get_meet_list()
  for meet in raw_meet_list_hrefs:
    time.sleep(.3)
    if url in meet:
      print('no good', meet)
    elif 'compare' in meet:
      print('no good', meet)
    else:
      meet_list.append(meet)
      print('added:', meet)
  print('cleaned hrefs:', meet_list)
  return meet_list
  
#########################################
#########################################

# CREATE RESULTS HREF TAG
def create_results_url(meet):
  url = meet
  results_url = url + "/results"
  print('results:', results_url)
  return results_url

#########################################
#########################################

# GO TO RESULTS
def navigate_to_results(meet):
  meet = meet
  results_url = create_results_url(meet)
  driver.get(str(results_url))



#########################################
#########################################

# DEFINE FUNCTION THAT FINDS AND CLICKS INTO EACH LINK
def find_individual_results_links():
  individual_results_list = driver.find_elements(By.XPATH, "//table[@class='meetResultsList']/tbody/tr/td/a")
  return individual_results_list
 

#########################################
#########################################

# OPENS NEW TAB FOR SCRAPING
def open_new_tab():
  time.sleep(.5)
  driver.execute_script("window.open('');")

#########################################
#########################################

# NAVIGATES TO NEW TAB 
def navigate_new_tab():
  time.sleep(.5)
  driver.switch_to.window(driver.window_handles[1])

#########################################
#########################################

# LOADS RACE URL INTO NEW WINDOW
def load_race_url(race):
  time.sleep(.5)
  race = race
  driver.get(str(race))
  