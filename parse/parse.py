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

#Получаем инфу по API от комфорткино
def parse_comfortkino(place:str)->"json":
    place = place.lower().strip()
    if place == "fokus" or place == "mega" or place == "almaz":
        link = f"https://{place}.comfortkino.ru/local/php_interface/api/v1/films/playbill/"
        data = requests.get(link, headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}).json()
        for film_counter in range(len(data['data'])):
            data['data'][film_counter]['url'] = f"https://{place}.comfortkino.ru" + data['data'][film_counter]['url']
            # data['data'][film_counter]['pushkin'] = f"https://{place}.comfortkino.ru" + data['data'][film_counter]['pushkin'] 
        return data
    else:
        raise ValueError('Возможные варианты "fokus" or "mega" or "almaz"')

