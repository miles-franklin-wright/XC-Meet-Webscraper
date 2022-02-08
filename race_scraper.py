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

############################################
############################################
############################################
# MAIN FUNCTION
def scraper():
  # CALLS URL CSV READER
  race_urls = load_race_urls_csv()
  # LOOPS THROUGH SCRAPING PROGRAM
  cycle_races(race_urls)
  driver.quit()
############################################
############################################
############################################

# LOADS IN URLS FROM RACE_URLS_CSV
def load_race_urls_csv():
  race_urls = []
  with open('race_urls_csv.csv', 'r') as urls_from_csv:
    csv_urls = csv.reader(urls_from_csv)
    print('checking race urls:')
    for race in csv_urls:
      print(race)
      race_urls.append(race)
  return race_urls

# CYCLES THROUGH EACH RACE IN RACE_URLS
def cycle_races(race_urls):
  time.sleep(8)
  race_urls = race_urls
  for race in race_urls:
    driver.implicitly_wait(3)
    load_race_url(race)
    time.sleep(8)
    perform_program(race)
    time.sleep(8)
    print('cycle completed')

# LOADS RACE IN DRIVER
def load_race_url(race):
  time.sleep(.5)
  race = race[0]
  driver.get(race)

# SCRAPES RACE AND REMOVES RACE FROM RACE_URLS_CSV  
def perform_program(race):
  race = race
  header_results = []
  raw_results = []
  header_results = scrape_header()
  print('header results:', header_results)
  time.sleep(2)
  raw_results.append(scrape_td_elements())
  print('raw results:', raw_results)
  time.sleep(2)
  print('RACE SCRAPED')
  time.sleep(2)
  cleaned_results = clean(raw_results)
  time.sleep(2)
  final_data = combine_header_and_cleaned(header_results, cleaned_results)
  time.sleep(2)
  print('final data:', final_data)
  time.sleep(2)
  can_remove = main_csv_function(final_data)
  time.sleep(1)
  remove_race_url_from_csv(can_remove, race)
  time.sleep(2)

# CLEANS RAW DATA
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
  print('just athlete data:', just_athlete_data)
  return just_athlete_data

# ADDS THE CLEANED DATA TO DATA.CSV
def main_csv_function(final_data):
  success = False
  final_data = final_data
  with open('data.csv', 'a')  as data:
    writer = csv.writer(data)
    writer.writerows(final_data)
  print('rows written to csv')
  success = True
  return success

# REMOVES THE RACE URL FROM RACE_URLS_CSV
def remove_race_url_from_csv(success, race):
  race = race
  success = success
  with open('race_urls_csv.csv', 'rb') as unedited, open('race_urls_csv.csv', 'wb') as edited:
      writer = csv.writer(edited)
      next(unedited)
      for row in unedited:
        unedited.write(row)
  

# COMBINES THE HEADER RESULTS AND CLEANED BODY RESULTS
def combine_header_and_cleaned(header_results, cleaned_results):
  header_results = header_results
  cleaned_results = cleaned_results
  print('header and cleaned results:', header_results, cleaned_results)
  final_data = []
  for item in cleaned_results:
    time.sleep(.1)
    for i in header_results:
      time.sleep(.05)
      item.append(i)
    final_data.append(item)
  return final_data

# FINDS THE MEET NAME
def scrape_meet_name():
  meet_name = driver.find_element(By.CLASS_NAME, 'meetName')
  print(meet_name.text)
  return meet_name.text

# FINDS THE MEET DATE
def scrape_meet_date():
  meet_date = driver.find_element(By.XPATH, "//div[@class='date']/time")
  print(meet_date.text)
  return meet_date.text

# FINDS THE LOCATION OF THE MEET
def scrape_meet_location():
  meet_location = driver.find_element(By.XPATH, "//div[@class='venueName']/a")
  print(meet_location.text)
  return meet_location.text

# FINDS BOTH GENDER OF RACE AND ITS LENGTH
def scrape_race_length_gender():
  time.sleep(2)
  combined_race_lenth_gender = driver.find_element(By.XPATH, "//div[@id='resultsList']/table/thead/tr/th/a")
  print(combined_race_lenth_gender.text)
  return combined_race_lenth_gender.text

# SEPARATES OUT GENDER FROM COMBINED 
def scrape_gender():
  combined = scrape_race_length_gender()
  gender = combined[0:5]
  return gender
  
# SEPARATES OUT RACE LENGTH FROM COMBINED
def scrape_race_length():
  combined = scrape_race_length_gender()
  race_length = combined[5:10]
  return race_length
  
# SCRAPES ALL ELEMENTS FROM THE TABLE (BOTH EMPTIES AND NON)
def scrape_td_elements():
  raw_results = []
  td_elements = driver.find_elements(By.XPATH, "//div[@id='resultsList']/table/tbody/tr/td")
  for td in td_elements:
    time.sleep(0.1)
    raw_results.append(td.get_attribute('data-text'))
    raw_results.append(td.text)
  return raw_results

# FUNCTION THAT CYCLES THROUGH ALL MORE MINOR HEADER SCRAPING FUNCTIONS AND RETURNS ONE LIST
def scrape_header():
  header_elements = []
  time.sleep(2)
  meet_name = scrape_meet_name()
  header_elements.append(meet_name)
  time.sleep(2)
  meet_date = scrape_meet_date()
  header_elements.append(meet_date)
  time.sleep(2)
  meet_location = scrape_meet_location()
  header_elements.append(meet_location)
  time.sleep(2)
  gender = scrape_gender()
  header_elements.append(gender)
  time.sleep(2)
  race_length = scrape_race_length()
  header_elements.append(race_length)
  time.sleep(2)
  return header_elements

# SPECIFIES THE LIST (RAW LIST = LIST WITHIN A LIST)
def select_raw_list(raw_results):
  raw_results = raw_results
  raw_list = raw_results[0]
  print('selected element 0 of raw results; raw list:', raw_list)
  return raw_list

# REMOVES THE NONES AND EMPTIES FROM THE RAW BODY DATA
def remove_nones_and_empties(raw_list):
  raw_list = raw_list
  just_data = []
  for i in raw_list:
    time.sleep(.1)
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

# SPLITS THE RAW DATA INTO LIST OBJECTS WITH INDIVIDUAL ATHLETES
def split_list_to_athlete(just_data):
  just_data = just_data
  split_by_athletes = []
  n = 6
  split_by_athletes = [just_data[i * n:(i + 1) * n] for i in range((len(just_data) + n - 1) // n )] 
  print (split_by_athletes)
  return split_by_athletes

# REMOVES THE TEAMSCORE DATA AT THE END OF THE BODY LIST
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
  return just_athlete_data