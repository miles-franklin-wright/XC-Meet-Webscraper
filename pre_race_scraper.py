import time
from athletes_for_pre_scraper import give_athletes

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
def pre_scraper(pre_element, race):
  race = race[0]
  driver.get(race)
  final_data = []
  pre_element = pre_element
  print(pre_element)
  raw_pre_data = pre_element
  final_data = clean_pre(raw_pre_data)
  return final_data
  print('pre scraped')

############################################
############################################
############################################

# LOGIC FOR GETTING THE PRE DATA
def get_pre():
  pre_data = []
  pre_data = driver.find_elements(By.NAME, 'pre')
  print(len(pre_data))
  return pre_data[0].text
  

# CYCLES PRE CLEANING FUNCTIONS
def clean_pre(raw_pre_data):
  raw_pre_data = raw_pre_data
  split_line_pre_data = split_raw_to_lines(raw_pre_data)
  no_empties = remove_empties(split_line_pre_data)
  full_cleaned_data = main_cycle(no_empties)
  print('full_cleaned_data: ', full_cleaned_data)
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
  event = raw_event()
  cleaned_date = raw_date()
  location = raw_location()
  race_length = length(no_empties)
  race_gender = gender(no_empties)
  # athlete_data = raw_athlete_data(no_empties)
  # cleaned_athletes = clean_athlete_data(athlete_data)
  cleaned_athletes = give_athletes(no_empties)
  combined_header_data = combine_header_data(event, race_gender, race_length, cleaned_date, location)
  full_cleaned_data = combined_header_and_data(combined_header_data, cleaned_athletes)
  for i in full_cleaned_data:
    print(i)
  return full_cleaned_data

# RETURNS EVENT
def raw_event():
  meet_name = driver.find_element(By.XPATH, '//h1[@class="meetName"]')
  print(meet_name.text)
  event = meet_name.text
  return event

# RETURNS DATE
def raw_date():
  meet_date = driver.find_element(By.XPATH, "//div[@class='date']/time")
  print(meet_date.text)
  meet_date = meet_date.text
  return meet_date

# RETURNS LOCATION
def raw_location():
  meet_location = driver.find_element(By.XPATH, "//div[@class='venueName']/a")
  print(meet_location.text)
  location = meet_location.text
  return location


# RETURNS GENDER AND LENGTH OF RACE
def raw_gender_and_length(no_empties):
  no_empties = no_empties
  gender_and_length = ''
  for line in no_empties:
    if "Event" in line:
      gender_and_length = line
    else:
      None
  print(gender_and_length)
  return gender_and_length

# RETURN GENDER
def gender(no_empties):
  no_empties = no_empties
  gender = ''
  for line in no_empties:
    if "Boys" in line:
      gender = 'BOYS'
    elif 'BOYS' in line:
      gender = 'BOYS'
    elif 'boys' in line:
      gender = 'BOYS'
    elif 'Girls' in line:
      gender = 'GIRLS'
    elif 'GIRLS' in line:
      gender = 'GIRLS'
    elif 'girls' in line:
      gender = 'GIRLS'
    else:
      print('no gender')
  print(gender)
  return gender

# RETURN GENDER
def length(no_empties):
  no_empties = no_empties
  length = ''
  for line in no_empties:
    if "5k" in line:
      length = '5000'
    elif '5000' in line:
      length = '5000'
    elif '5000m' in line:
      length = '5000'
    elif '2 Mile' in line:
      length = '3200'
    elif '3200m' in line:
      length = '3200'
    else:
      print('no length')
  print(length)
  return length


# RETURNS THE ATHLETE DATA OF THE RACE

def raw_athlete_data(no_empties):
  no_empties = no_empties
  athletes = []
  for i in no_empties:
    if len(i) == 79:
      athletes.append(i)
    elif len(i) == 74:
      athletes.append(i)
    elif len(i) == 75:
      athletes.append(i)
    elif len(i) == 76:
      athletes.append(i)
    elif len(i) == 77:
      athletes.append(i)
    elif len(i) == 78:
      athletes.append(i)
    elif len(i) == 73:
      athletes.append(i)
    elif len(i) == 73:
      athletes.append(i)
    elif len(i) == 72:
      athletes.append(i)
    elif len(i) == 71:
      athletes.append(i)
    elif len(i) == 80:
      athletes.append(i)
    elif len(i) == 81:
      athletes.append(i)
    elif len(i) == 82:
      athletes.append(i)
    elif len(i) == 83:
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

