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

def scrape_td_elements():
  raw_results = []
  td_elements = driver.find_elements(By.XPATH, "//div[@id='resultsList']/table/tbody/tr/td")
  for td in td_elements:
    time.sleep(0.1)
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
  print(raw_results)
  print('list selected')
  raw_list = raw_results
  return raw_list




#########################################
#########################################


def remove_nones_and_empties(raw_list):
  raw_list = raw_list
  just_data = []
  for i in raw_list:
    time.sleep(.2)
    if i == "":
      print('blank found')
    elif i == None:
      print('None found')
    elif i == "None":
      print('None found')
    elif i == ' ':
      print('blank found')
    else:
      just_data.append(i)
      print('its chill')
  print(just_data)
  return just_data


#########################################
#########################################

def split_list_to_athlete(just_data):
  just_data = just_data
  split_by_athletes = []
  # 6 DATA POINTS
  n = 6
  # ADD THE 6 DATA POINTS TO NEW SUBLIST
  split_by_athletes = [just_data[i * n:(i + 1) * n] for i in range((len(just_data) + n - 1) // n )] 
  print (split_by_athletes)
  return split_by_athletes

#########################################
#########################################

def remove_teamscore_data(athlete_with_teamscore):
  athlete_with_teamscore = athlete_with_teamscore
  just_athlete_data = []
  for i in athlete_with_teamscore:
    time.sleep(.1)
    if len(i[0]) > 3:
      print(i)
      print('team found')
    elif len(i[2]) > 2:
      print(i)
      print('team found')
    elif len(i[4]) > 8:
      print(i)
      print('team found')
    elif len(i[5]) > 3:
      print(i)
      print('team found')
    else: 
      just_athlete_data.append(i)

#########################################
#########################################



#########################################
#########################################
# end cleaning component functions
#########################################
#########################################

#########################################
#########################################
# begin combining function
#########################################
#########################################

def combine_header_and_cleaned(header_results, cleaned_results):
  header_results = header_results
  cleaned_results = cleaned_results
  print(header_results)
  # final_data = []
  # for item in cleaned_results:
  #   for i in header_results:
  #     item.append(i)
  #   final_data.append[item]
  # return final_data
    
  
  


#########################################
#########################################
# end combining function
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
  just_data = remove_nones_and_empties(raw_list)
  time.sleep(.5)
  athlete_with_teamscore = split_list_to_athlete(just_data)
  time.sleep(.5)
  just_athlete_data = remove_teamscore_data(athlete_with_teamscore)
  time.sleep(.5)
  print(just_athlete_data)
  return just_athlete_data



#########################################
#########################################


# PRIMARY SCRAPING FUNCTION
def perform_program():
  header_results = []
  raw_results = []
  header_results.append(scrape_header())
  time.sleep(5)
  raw_results.append(scrape_td_elements())
  time.sleep(2)
  print(raw_results)
  time.sleep(2)
  print('RACE SCRAPED')
  time.sleep(2)
  cleaned_results = clean(raw_results)
  time.sleep(2)
  final_data = combine_header_and_cleaned(header_results, cleaned_results)
  time.sleep(2)
  print(final_data)
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
    perform_program()
    time.sleep(8)
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
  cycle_individual_results_list()
  driver.close()


#########################################
#########################################




#########################################
#########################################



#########################################
#########################################

def run_program():
  run_scrape()


#########################################
#########################################

run_program()

