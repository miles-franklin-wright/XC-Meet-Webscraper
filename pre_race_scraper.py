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
  raw_pre_data = get_pre()
  full_data = clean_pre(raw_pre_data)
  return full_data
  print('pre scraped')

############################################
############################################
############################################

# LOGIC FOR GETTING THE PRE DATA
def get_pre():
  pre_data = driver.find_element(By.XPATH, "//div[@id='meetResultsBody']/pre")
  return pre_data.text

# CYCLES PRE CLEANING FUNCTIONS
def clean_pre(raw_pre_data):
  raw_pre_data = raw_pre_data
  split_line_pre_data = split_raw_to_lines(raw_pre_data)
  no_empties = remove_empties(split_line_pre_data)
  full_cleaned_data = main_cycle(no_empties)
  return full_cleaned_data

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
  return no_empties

# CYCLES THROUGH AND ISOLATES RAW DATA, RUNS CLEANING FUNCTIONS ON THEM, RETURNS A SINGLE LIST TO BE SENT TO CSV
def main_cycle(no_empties):
  no_empties = no_empties
  event = raw_event(no_empties)
  gender_and_length = raw_gender_and_length(no_empties)
  date_and_place = raw_date_and_place(no_empties)
  athlete_data = raw_athlete_data(no_empties)
  cleaned_gender = clean_gender(gender_and_length)
  cleaned_race_length = clean_race_length(gender_and_length)
  cleaned_date = clean_date(date_and_place)
  cleaned_place = clean_place(date_and_place)
  cleaned_athletes = clean_athlete_data(athlete_data)
  combined_header_data = combine_header_data(event, cleaned_gender, cleaned_race_length, cleaned_date, cleaned_place)
  full_cleaned_data = combined_header_and_data(combined_header_data, cleaned_athletes)
  for i in full_cleaned_data:
    print(i)

# RETURNS EVENT
def raw_event(no_empties):
  no_empties = no_empties
  event = no_empties[3]
  return event

# RETURNS GENDER AND LENGTH OF RACE
def raw_gender_and_length(no_empties):
  no_empties = no_empties
  gender_and_length = no_empties[6]
  return gender_and_length

# RETURNS DATE AND PLACE OF RACE
def raw_date_and_place(no_empties):
  no_empties = no_empties
  date_and_place = no_empties[4]
  return date_and_place

# RETURNS THE ATHLETE DATA OF THE RACE
def raw_athlete_data(no_empties):
  no_empties = no_empties
  athletes = []
  for i in no_empties:
    if len(i) == 79:
      athletes.append(i)
    else:
      None
  return athletes

# CLEANS GENDER
def clean_gender(gender_and_length):
  gender_and_length = gender_and_length
  cleaned_gender = gender_and_length[8:12]
  return cleaned_gender

# CLEANS RACE LENGTH
def clean_race_length(gender_and_length):
  gender_and_length = gender_and_length
  cleaned_length = gender_and_length[12:15]
  return cleaned_length

# CLEANS DATE
def clean_date(date_and_place):
  date_and_place = date_and_place
  cleaned_date = date_and_place[43:]
  return cleaned_date

# CLEANS PLACE
def clean_place(date_and_place):
  date_and_place = date_and_place
  cleaned_place = date_and_place[:12]
  return cleaned_place
  
# CLEANS ATHLETE DATA 
def clean_athlete_data(athlete_data):
  athlete_data = athlete_data
  cleaned_athletes = []
  for i in athlete_data:
    athlete = []
    athlete_place = i[0:3]
    athlete_name = i[9:30]
    athlete_year = i[30:32]
    athlete_school = i[32:59]
    athlete_time = i[69:76]
    athlete_team_place = i[76:]
    athlete.append(athlete_place)
    athlete.append(athlete_name)
    athlete.append(athlete_school)
    athlete.append(athlete_year)
    athlete.append(athlete_time)
    athlete.append(athlete_team_place)
    cleaned_athletes.append(athlete)
  return cleaned_athletes

# COMBINES HEADER DATA INTO LIST
def combine_header_data(event, cleaned_gender, cleaned_race_length, cleaned_date, cleaned_place):
  event = event
  cleaned_gender = cleaned_gender
  cleaned_race_length = cleaned_race_length
  cleaned_date = cleaned_date
  cleaned_place = cleaned_place
  combined_header_data = []
  combined_header_data.append(event)
  combined_header_data.append(cleaned_date)
  combined_header_data.append(cleaned_place)
  combined_header_data.append(cleaned_gender)
  combined_header_data.append(cleaned_race_length)
  return(combined_header_data)


# COMBINES THE HEADER RESULTS AND CLEANED BODY RESULTS
def combined_header_and_data(combined_header_data, cleaned_athletes):
  combined_header_data = combined_header_data
  cleaned_athletes = cleaned_athletes
  full_cleaned_data = []
  for item in cleaned_athletes:
    for i in combined_header_data:
      time.sleep(.05)
      item.append(i)
    full_cleaned_data.append(item)
  return full_cleaned_data

