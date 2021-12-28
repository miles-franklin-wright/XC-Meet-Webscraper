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

#RUNS FUNCTION TO OPEN WEBDRIVER TO MEET 
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

#########################################
#########################################

# RUNS FUNCTION TO GO TO RESULTS
navigate_to_results()

#########################################
#########################################

# FIND RESULTS TABLE TO NAVIGATE TO INDIVIDUAL RESULTS LINKS
def find_results_table():
  results_table_element = driver.find_element(By.CLASS_NAME, 'meetResultsList')
  print(results_table_element.get_attribute('class'))

#########################################
#########################################

# RUNS FUNCTION TO FIND THE TABLE
find_results_table()

#########################################
#########################################

# GIVES A REST TIME BETWEEN FUNCTION CALLS
time.sleep(3)

#########################################
#########################################

# DEFINE FUNCTION THAT FINDS AND CLICKS INTO EACH LINK
def find_individual_results_links():
  individual_results_list = driver.find_elements(By.XPATH, "//table[@class='meetResultsList']/tbody/tr/td/a")
  return individual_results_list
  # for i in individual_results_list:
  #   driver.implicitly_wait(10)
  #   print(i.get_attribute('href'))

#########################################
#########################################

# OPENS NEW TAB FOR SCRAPING
def open_new_tab():
  driver.execute_script("window.open('');")

#########################################
#########################################

# NAVIGATES TO NEW TAB 

#########################################
#########################################



#########################################
#########################################

# PRIMARY SCRAPING FUNCTION
def scrape():
  time.sleep(10)
  print('RACE SCRAPED')

#########################################
#########################################

# CLICKS INTO EACH INDIVIDUAL MEET RESULT
def cycle_individual_results_list():
  time.sleep(3)
  individual_results_list = find_individual_results_links()
  for i in individual_results_list:
    driver.implicitly_wait(10)
    print(i.get_attribute('href'))
    # call function that contains create new window, get href of meet, scrape the data, revert to previous tab
    # calls function that removes new window when scraping action is completed
    

#########################################
#########################################


# RUNS FUNCTION THAT CYCLES THROUGH EACH INDIVIDUAL RACE
cycle_individual_results_list()

#########################################
#########################################



#########################################
#########################################



#########################################
#########################################




#########################################
#########################################