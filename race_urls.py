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
def race_urls():
  urls = []
  print('begin cycle, obtaining urls')
  intial_url = get_initial_meet()
  print('got initial meet')
  meet_list = clean_meet_list(intial_url)
  print('obtained urls, cycle closing')
  for meet in meet_list:
    time.sleep(.1)
    meet_races = []
    print('going to: ', str(meet) + '/results')
    navigate_to_results(meet)
    print('adding individual races')
    meet_races = append_individual_races_to_list()
    for race in meet_races:
      time.sleep(.1)
      print('appending:', race.get_attribute('href'))
      urls.append(race.get_attribute('href'))
      print('race url appended')
  urls_to_csv(urls)
  driver.quit()
############################################
############################################
############################################

# ENTERS MOST RECENT (OVERALL) MEET
def enter_initial_meet():
  print("please enter first meet of series you'd like to record")
  url = input()
  print(url)
  return url

# WEBDRIVER NAVIGATES TO INITIAL URL
def get_initial_meet():
  url = enter_initial_meet()
  driver.get(str(url))
  return url

# WEBDRIVER RETURNS EVERY LINK IN MEET HISTORY TAB
def get_meet_list():
  meet_list = driver.find_elements(By.XPATH, "//ul[@class='meets']/li/a")
  meet_list_hrefs = []
  for i in meet_list:
    time.sleep(.1)
    print('added to raw', i.get_attribute('href'))
    meet_list_hrefs.append(i.get_attribute('href'))
  return meet_list_hrefs

# NEW LIST RETURNED WITH MEET URLS 
def clean_meet_list(initial_url):
  initial_url = initial_url
  raw_meet_list_hrefs = get_meet_list()
  meet_list = []
  meet_list.append(initial_url)
  for meet in raw_meet_list_hrefs:
    time.sleep(.1)
    if initial_url in meet:
      print('no good', meet)
    elif 'compare' in meet:
      print('no good', meet)
    else:
      meet_list.append(meet)
      print('added:', meet)
  print('cleaned hrefs:', meet_list)
  return meet_list
  
# CREATE RESULTS HREF TAG
def create_results_url(meet):
  url = meet
  results_url = url + "/results"
  print('results:', results_url)
  return results_url

# GOES TO RESULTS
def navigate_to_results(meet):
  meet = meet
  results_url = create_results_url(meet)
  driver.get(str(results_url))

# RETURNS INDIVIDUAL RACE URLS
def find_individual_results_links():
  individual_results_list = driver.find_elements(By.XPATH, "//table[@class='meetResultsList']/tbody/tr/td/a")
  return individual_results_list
 
# APPENDS EACH INDIVIDUAL RACE URL TO OVERALL URL list
def append_individual_races_to_list():
  urls_to_csv = []
  races_to_append = find_individual_results_links()
  for race in races_to_append:
    urls_to_csv.append(race)
    print('race added')
  return urls_to_csv

# WRITES EACH URL TO CSV
def urls_to_csv(urls):
  urls = urls
  with open('race_urls_csv.csv', 'a') as data:
    writer = csv.writer(data)
    for url in urls:
      time.sleep(.1)
      writer.writerow([url])
  print('rows written to csv')