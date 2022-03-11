
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
op = webdriver.ChromeOptions()
op.add_argument('headless')
httpString = 'https://www.tripadvisor.com/Restaurants-g60713-San_Francisco_California.html'
driver = webdriver.Chrome(executable_path=r'/Users/wudailing/PycharmProjects/Intermeidate python/venv/lib/chromedriver',options=op)
driver.get(httpString)
c = driver.page_source


# page = requests.get(html,httpString)
soup = BeautifulSoup(c, 'html.parser')
# soup = BeautifulSoup(page.content, 'html.parser')

def restaurant_name():
    restaurants_lst =[]
    restaurants = soup.find_all(class_='bHGqj Cj b')
    for i in range(11):
        r = restaurants[i]
        restauraunt = r.get_text()
        restauraunt = restauraunt.lstrip('1234567890. ')
        restaurants_lst.append(restauraunt)
        restaurants_lst = restaurants_lst[:11]
    return restaurants_lst
    # pattern = r'^[0-9]'
    # if re.search(pattern,restauraunt) != None:

def pic_URL():
    pic_URL_lst = []
    restaurant_pic = soup.find_all(class_= 'ebvuL _R w h GA')
    for i in range(11):
        p = restaurant_pic[i]
        pic_URL = p["style"][23:-3]
        pic_URL_lst.append(pic_URL)
    print(type(p))
    return pic_URL_lst


httpString_attraction = 'https://www.tripadvisor.com/Attractions-g60713-Activities-San_Francisco_California.html'
driver = webdriver.Chrome(executable_path=r'/Users/wudailing/PycharmProjects/Intermeidate python/venv/lib/chromedriver',options=op)
driver.get(httpString_attraction)
c = driver.page_source
soup1 = BeautifulSoup(c, 'html.parser')



def attraction_name():

    attractions = soup1.find_all(class_='bUshh o csemS')
    attractions_lst = []
    for i in range(11):
        attraction = attractions[i]
        attraction = attraction.get_text()
        attraction = attraction.lstrip('1234567890. ')
        attractions_lst.append(attraction)
    return attractions_lst

def attraction_URL():
    lst = soup1.find_all(class_="effdZ w h P0 M0 Gm")
    attraction_pic_URL_lst = []
    for i in range(11):
        paragraph = lst[i]
        pic = paragraph.select('picture>img')
        attraction_pic_URL = pic[0]['src']
        attraction_pic_URL_lst.append(attraction_pic_URL)
    return attraction_pic_URL_lst




