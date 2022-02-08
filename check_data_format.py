# SELENIUM SETUP
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-hsm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# DECLARE DRIVER
driver = webdriver.Chrome(options=chrome_options) 
 


def check_format():
  try:
    check = driver.find_element(By.XPATH, "//div[@id='meetResultsBody']/pre")
    if check.text != '':
      print('go to pres')
  except NoSuchElementException:
    print('go to formatted')