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
    unique_hrefs = []
    base_url = "https://www.formula1.com"

    for href in hrefs:
        for i in range(1, current_year + 1):
            if f"/en/results/{i}/races/" in href:
                href_split = href.split('/')
                race_name = href_split[6]
                race_year = href_split[3]
                if race_name not in seen:
                    seen.add(race_name)
                    unique_hrefs.append(base_url + href)

    return unique_hrefs

def extract_race_results(url):
    try:
        Url = requests.get(url)
        soup = BeautifulSoup(Url.text, "html.parser")
        
        table = soup.find("tbody")
        rows = table.find_all("tr")
        
        race_results = []
        for row in rows[1:]:
            cols = row.find_all("td")
            if len(cols) > 0:
                result = {
                    "Position": cols[0].text.strip(),
                    "Driver": cols[1].text.strip(),
                    "Team": cols[2].text.strip(),
                    "Laps": cols[3].text.strip(),
                    "Time": cols[4].text.strip(),
                    "Status": cols[5].text.strip()
                }
                race_results.append(result)
        
        return race_results
    except Exception as e:
        print(f" {url} probably didn't happen yet")
        return []

def moreScrap():
    all_results = []
    for x in range(1950, current_year + 1):
        race_urls = Scrap(x)
        
        for url in race_urls:
            race_results = extract_race_results(url)
            if race_results:
                print(f"Results for {url}:")
                for result in race_results:
                    print(result)
                    all_results.append(result)
    
    with open("output.json", "w") as save_file:
        json.dump(all_results, save_file, indent=6)

moreScrap()