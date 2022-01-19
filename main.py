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


#########################################
#########################################

# GET MEET
def get_meet():
  url = enter_meet()
  driver.get(str(url))

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

# FIND RESULTS TABLE TO NAVIGATE TO INDIVIDUAL RESULTS LINKS
def find_results_table():
  results_table_element = driver.find_element(By.CLASS_NAME, 'meetResultsList')
  print(results_table_element.get_attribute('class'))


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
# begin scraper component functions
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

def scrape_race_length_gender():
  combined_race_lenth_gender = driver.find_element(By.XPATH, "//div[@id='resultsList']/table/thead/tr/th/a")
  print(combined_race_lenth_gender.text)
  return combined_race_lenth_gender


#########################################
#########################################

def scrape_athlete_and_school():
  combined_athlete_school = driver.find_elements(By.XPATH, "//div[@id='resultsList']/table/tbody/tr/td/a")
  for athlete in combined_athlete_school:
    time.sleep(0.2)
    print(athlete.text)
  return combined_athlete_school


#########################################
#########################################

def scrape_athlete_time():
  athlete_times = driver.find_elements(By.XPATH, "//div[@id='resultsList']/table/tbody/tr/td/span")
  for athlete in athlete_times:
    time.sleep(0.2)
    print(athlete.text)
  return athlete_times

#########################################
#########################################

def scrape_td_elements():
  raw_results = []
  td_elements = driver.find_elements(By.XPATH, "//div[@id='resultsList']/table/tbody/tr/td")
  for td in td_elements:
    time.sleep(0.5)
    raw_results.append(td.get_attribute('data-text'))
    raw_results.append(td.text)
  return raw_results


#########################################
#########################################

def scrape_header():
  time.sleep(3)
  scrape_meet_name()
  time.sleep(3)
  scrape_meet_date()
  time.sleep(3)
  scrape_meet_location()
  time.sleep(3)
  scrape_race_length_gender()
  time.sleep(3)



#########################################
#########################################
# end main scraper component functions
#########################################
#########################################


#########################################
#########################################
# begin cleaning component functions
#########################################
#########################################


def select_raw_list(raw_results):
  raw_results = raw_results
  print(raw_results[1])
  print('list selected')
  raw_list = raw_results[1]
  return raw_list




#########################################
#########################################


def remove_nones_and_empties(raw_list):
  raw_list = raw_list
  for i in raw_list:
    time.sleep(.2)
    if i == "":
      raw_list.remove(i)
      print('blank found')
    elif i == "None":
      raw_list.remove(i)
      print('None found')
    else:
      print('its chill')
  print()


#########################################
#########################################






#########################################
#########################################
# end cleaning component functions
#########################################
#########################################


#########################################
#########################################

# PRIMARY CLEANING FUNCTION
def clean(raw_results):
  raw_results = raw_results
  time.sleep(.5)
  raw_list = select_raw_list(raw_results)
  time.sleep(.5)
  cleaned_list = remove_nones_and_empties(raw_list)
  print(cleaned_list)
  print('done cleaning for now')



#########################################
#########################################


# PRIMARY SCRAPING FUNCTION
def scrape():
  raw_results = []
  raw_results.append(scrape_header())
  time.sleep(5)
  raw_results.append(scrape_td_elements())
  time.sleep(2)
  print(raw_results)
  time.sleep(2)
  print('RACE SCRAPED')
  time.sleep(2)
  clean(raw_results)
  time.sleep(10)
  close_race_url()
  time.sleep(5)
  navigate_results_page_return()
  time.sleep(5)
  return raw_results

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
    raw_results = scrape()
    time.sleep(8)
    return raw_results
    print('cycle completed')
    


##########3###############################
#########################################

def run_scrape():
  get_meet()
  time.sleep(1)
  navigate_to_results()
  time.sleep(1)
  find_results_table()
  time.sleep(1)
  raw_results = cycle_individual_results_list()
  driver.close()
  return raw_results

#########################################
#########################################

def run_clean(raw_results):
  print('results received to clean')
  print(raw_results)

#########################################
#########################################

def run_to_csv():
  print('tbd')

#########################################
#########################################

def run_program():
  raw_results = run_scrape()
  run_clean(raw_results)
  run_to_csv()

#########################################
#########################################

run_program()

