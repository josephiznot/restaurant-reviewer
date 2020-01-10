
import os
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('restaurants.json', 'r') as restaurant_urls:
   restaurants = json.loads(restaurant_urls.read())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   options=chrome_options) 

_RATING_CLASSNAME = 'Aq14fc'
_REVIEWS_CLASSNAME = 'z5jxId'
_RESTAURANT_ADDRESS_CLASSNAME = 'T6pBCe'
_RESTAURANT_ADDRESS_FIELD = 'restaurant_address'
_RESTAURANT_REVIEWS_FIELD = 'restaurant_reviews'
_RESTAURANT_RATING_FIELD = 'restaurant_rating'
_RESTAURANT_URL = 'restaurantUrl'
_RESTAURANT_NAME = 'restaurantName'

def get_all_restaurant_info():
   """Returns a tuple of addresses, ratings, reviews"""
   restaurants_data = []
   driver.implicitly_wait(20)
   for i in range(len(restaurants)):
      print('___________________________')
      print(i)
      try:
         driver.get(restaurants[i][_RESTAURANT_URL])
         rating = driver.find_elements_by_class_name(_RATING_CLASSNAME)[0].text
         total_reviews = driver.find_elements_by_class_name(_REVIEWS_CLASSNAME)[0].text
         restaurant_info = restaurants[i][_RESTAURANT_NAME], rating, total_reviews,
      except:
         restaurant_info = '', '', ''
      print(restaurant_info)
      restaurants_data.append(restaurant_info)
   driver.close()
   return restaurants_data

def create_csv_file(all_restaurants_info):
   with open('restaurant_reviews.csv', 'w') as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=',')
      for csv_row in all_restaurants_info:
         csv_writer.writerow(csv_row)

data = get_all_restaurant_info()

print(data)

create_csv_file(data)
