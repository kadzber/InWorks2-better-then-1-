import requests
from bs4 import BeautifulSoup
from datetime import date
import json  

current_date = date.today()
current_year = current_date.year


def Scrap(i):    
    url = f"https://www.formula1.com/en/results/{i}/races/1229/bahrain/race-result"
    Url = requests.get(url)
    soup = BeautifulSoup(Url.text, "html.parser")
    
    grid = soup.find_all('a')
    hrefs = [link['href'] for link in grid if 'href' in link.attrs]

    seen = set()
    results = []
    base_url = "https://www.formula1.com"

    for href in hrefs:
        for i in range(1, current_year + 1):
            if f"/en/results/{i}/races/" in href:
                href_split = href.split('/')
                race_name = href_split[6]
                race_year = href_split[3]
                
                    
                    
                    
                if race_name not in seen:
                    seen.add(race_name)
                    seen.add(race_year)
                    results.append({
                        race_year: [
                        {"url": base_url + href},
                        {"race": race_name}
                        ]
                    })
                    print(results)

Scrap(2024)                    