import requests
from bs4 import BeautifulSoup
import re
from enum import Enum

class Weekday(Enum):
    Montag = 1
    Dienstag = 2
    Mittwoch = 3
    Donnerstag = 4
    Freitag = 5

def get_mensa_menu():
    kw = 29
    url = 'https://www.sw-ka.de/de/hochschulgastronomie/speiseplan/mensa_adenauerring/?kw=' + str(kw)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    days = soup.find_all('div', class_=re.compile(r"canteen-day"))

    i = 6 - len(days)
    for day in days:
        print(Weekday(i).name + ":")
        i += 1
        menu_items = day.find_all('tr', class_=re.compile(r"mt-[1-9]"))
        for item in menu_items:
            name = item.find('b').text.strip()
            if item.find('div', class_='energie'):
                energie = item.find('div', class_='energie').text.strip()
                match = re.search(r'(\d+)\s*kcal', energie)
                if match:
                    kcal = match.group(1)
                    print(f'{name}:\n  {kcal}kcal')


get_mensa_menu()
