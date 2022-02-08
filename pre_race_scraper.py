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



############################################
############################################
############################################
# MAIN FUNCTION
def pre_scraper():
  load_race_url()
  raw_pre_data = get_pre()
  clean_pre(raw_pre_data)
  print('pre scraped')
############################################
############################################
############################################

# LOADS RACE IN DRIVER
def load_race_url():
  time.sleep(.5)
  race = 'https://nj.milesplit.com/meets/54860-njsiaa-meet-of-champions-2009/results/109612'
  driver.get(race)

# LOGIC FOR GETTING THE PRE DATA
def get_pre():
  pre_data = driver.find_element(By.XPATH, "//div[@id='meetResultsBody']/pre")
  return pre_data.text

# CYCLES PRE CLEANING FUNCTIONS
def clean_pre(raw_pre_data):
  raw_pre_data = raw_pre_data
  split_line_pre_data = split_raw_to_lines(raw_pre_data)
  no_empties = remove_empties(split_line_pre_data)
  excess_removed = remove_headers_and_team_data(no_empties)


# SPLIT TEXT INTO LIST OF LINES
def split_raw_to_lines(raw_pre_data):
  raw_pre_data = raw_pre_data
  split = raw_pre_data.splitlines()
  return split

# REMOVES EMPTY ROWS
def remove_empties(split_line_pre_data):
  split_line_pre_data = split_line_pre_data
  no_empties = []
  for i in split_line_pre_data:
    if i == '':
      None
    elif i == " ":
      None
    else:
      no_empties.append(i)
  print(no_empties)
  return no_empties

# REMOVES VARIETY OF HEADERS  
def remove_headers_and_team_data(no_empties):
  no_empties = no_empties
  event = no_empties[3]
  gender_and_length = no_empties[6]
  date_and_place = no_empties[4]
  print(event, gender_and_length, date_and_place)