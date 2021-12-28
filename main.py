# SELENIUM SETUP
from selenium import webdriver
from selenium.webdriver.common.by import By

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


driver = webdriver.Chrome(options=chrome_options)

########################################
########################################

# ENTER MEET
def enter_meet():
  print("please enter meet url")
  url = input()
  print(url)
  return url
  # driver.get(str(url))

#########################################
#########################################

# GET MEET
def get_meet():
  url = enter_meet()
  driver.get(str(url))

get_meet() 

#########################################
#########################################

# CREATE RESULTS HREF TAG
def create_results_url():
  url = enter_meet()
  results_url = url + "/results"
  print(results_url)
  return results_url

#########################################
#########################################

# GO TO RESULTS
def navigate_to_results():
  results_url = create_results_url()
  driver.get(str(results_url))

navigate_to_results()

#########################################
#########################################

# FIND RESULTS TABLE TO NAVIGATE TO INDIVIDUAL RESULTS LINKS
def find_results_table():
  results_table_element = driver.find_element(By.CLASS_NAME, 'meetResultsList')
  print(results_table_element.get_attribute('class'))

find_results_table()

#########################################
#########################################

time.sleep(3)

def find_individual_results_links():
  # individual_results_list = driver.find_elements(By.XPATH, "//table[contains(@class,'meetResultsList')]/tbody/tr/td/a]")
  individual_results_list = driver.find_elements(By.XPATH, "//table[@class='meetResultsList']/tbody/tr/td/a")
  for i in individual_results_list:
    driver.implicitly_wait(10)
    print(i.get_attribute('href'))

find_individual_results_links()

#########################################
#########################################




#########################################
#########################################


#########################################
#########################################



#########################################
#########################################



#########################################
#########################################




#########################################
#########################################