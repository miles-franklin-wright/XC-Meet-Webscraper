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

########################################
########################################

# CREATES WEBDRIVER
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

#########################################
#########################################

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
 

#########################################
#########################################

# OPENS NEW TAB FOR SCRAPING
def open_new_tab():
  driver.execute_script("window.open('');")

#########################################
#########################################

# NAVIGATES TO NEW TAB 
def navigate_new_tab():
  driver.switch_to.window(driver.window_handles[1])

#########################################
#########################################

# LOADS RACE URL INTO NEW WINDOW
def load_race_url(race):
  race = race
  driver.get(str(race))





#########################################
#########################################
# start main scraper functions
#########################################
#########################################

def scrape_meet_name():
  meet_name = driver.find_element(By.CLASS_NAME, 'meetName')
  print(meet_name.text)
  return meet_name.text

#########################################
#########################################

def scrape_meet_date():
  meet_date = driver.find_element(By.XPATH, "//div[@class='date']/time")
  print(meet_date.text)
  return meet_date

#########################################
#########################################

def scrape_meet_location():
  meet_location = driver.find_element(By.XPATH, "//div[@class='venueName']/a")
  print(meet_location.text)
  return meet_location

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
# end main scraper functions 
#########################################
#########################################

# PRIMARY SCRAPING FUNCTION
def scrape():
  time.sleep(3)
  scrape_meet_name()
  time.sleep(3)
  scrape_meet_date()
  time.sleep(3)
  scrape_meet_location()
  time.sleep(2)
  print('RACE SCRAPED')
  time.sleep(10)
  close_race_url()
  time.sleep(5)
  navigate_results_page_return()

#########################################
#########################################

# CLOSES INDIVIDUAL RACE URL
def close_race_url():
  driver.close()

#########################################
#########################################


# SWITCHES TO OLD (RESULT PAGE) URL
def navigate_results_page_return():
  driver.switch_to.window(driver.window_handles[0])


#########################################
#########################################

# ##### OLD; BUT MAY REIMPLEMENT. WE'LL SEE


# RUNS THE CYCLE OF OPENING, SCRAPING, AND NAVIGATING BACK TO THE ORIGINAL PLACE
# def race_cycle(race):
#   race = race
#   time.sleep(2)
#   open_new_tab()
#   time.sleep(2)
#   navigate_new_tab()
#   time.sleep(2)
#   load_race_url(race)
#   time.sleep(8)
#   scrape()
#   time.sleep(2)
#   navigate_results_page_return()

#########################################
#########################################

# CLICKS INTO EACH INDIVIDUAL MEET RESULT
def cycle_individual_results_list():
  time.sleep(3)
  individual_results_list = find_individual_results_links()
  for i in individual_results_list:
    driver.implicitly_wait(10)
    print(i.get_attribute('href'))
    race = str(i.get_attribute('href'))
    time.sleep(2)
    open_new_tab()
    time.sleep(2)
    navigate_new_tab()
    time.sleep(2)
    load_race_url(race)
    time.sleep(8)
    scrape()
    time.sleep(8)
    print('cycle completed')
    
cycle_individual_results_list()

#########################################
#########################################

driver.close()

#########################################
#########################################



#########################################
#########################################



#########################################
#########################################




#########################################
#########################################