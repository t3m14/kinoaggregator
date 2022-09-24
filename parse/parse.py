from bs4 import BeautifulSoup
import requests
import re

def parse_impulse():
    films_data = []
    all_sites_link = "https://impulschel.ru/poster"
    html = requests.get(all_sites_link).text
    soup = BeautifulSoup(html, "html.parser")
    films  = soup.find_all("div", class_="poster_list_item")
    for film in films:
        film_link = 'https://impulschel.ru' + film.find("div", class_="photo").a['href']
        name = film.find("div", class_="f_title").a.text
        film_html = requests.get(film_link).text
        soup = BeautifulSoup(film_html, "html.parser")
        desc = soup.find_all("div", class_="value")[1].p.text
        image = 'https://impulschel.ru' + soup.find("div", class_="photo").img['src']
        pegiinfo = soup.find("div", class_="value").text.strip()
        genere = soup.find("td", class_="value").text.strip()
        
        schedule = soup.find_all("div", class_="schedule_row")
        timing = []
        for item in schedule:
            date_item = item.find("div", class_="schedule_row_date").text
            date = re.split('\d', date_item)[0] + " " + re.findall("\d", date_item)[0] + re.split('\d', date_item)[-1]
            price = item.find("span", class_="time__marked")['title']
            time = item.find("span", class_="time__marked").text
            timing_item = {
                    "date": date,
                    "time" : time,
                    "price" : price
                }
            timing.append(timing_item)
        film_dict = {
        "link" : film_link,
        "name" : name,
        "description" : desc,
        "image" : image,
        "pegiinfo" : pegiinfo,
        "genere" : genere,
        "timing" : timing
        }
        films_data.append(film_dict)
    return films_data

parse_impulse()
