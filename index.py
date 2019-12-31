
import os
import csv
import json
from selenium import webdriver

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

def get_all_restaurant_info():
   """Returns a tuple of addresses, ratings, reviews"""
   addresses = []
   ratings = []
   reviews = []
   for restaurant in restaurants:
      driver.get(restaurant[_RESTAURANT_URL])
      address = driver.find_elements_by_class_name(_RESTAURANT_ADDRESS_CLASSNAME)[0].text
      rating = driver.find_elements_by_class_name(_RATING_CLASSNAME)[0].text
      total_reviews = driver.find_elements_by_class_name(_REVIEWS_CLASSNAME)[0].text
      addresses.append(address)
      ratings.append(rating)
      reviews.append(total_reviews)
   driver.close()
   return (addresses, ratings, reviews)

def create_csv_file(all_restaurants_info):
   addresses, ratings, reviews = all_restaurants_info
   with open('restaurant_reviews.csv', 'w') as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=',')
      csv_writer.writerow(addresses)
      csv_writer.writerow(ratings)
      csv_writer.writerow(reviews)

restaurants_data = get_all_restaurant_info()

print(restaurants_data)

create_csv_file(restaurants_data)
