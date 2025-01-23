import requests
from bs4 import BeautifulSoup
from datetime import date
import json  

current_date = date.today()
current_year = current_date.year

def Scrap(year):    
    url = f"https://www.formula1.com/en/results/{year}/races/1229/bahrain/race-result"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    grid = soup.find_all('a')
    hrefs = [link['href'] for link in grid if 'href' in link.attrs]
    
    results = []
    base_url = "https://www.formula1.com"
    
    seen = set()  
    
    for href in hrefs:
        if f"/en/results/{year}/races/" in href:
            href_split = href.split('/')
            raceName = href_split[6]
            
            if raceName not in seen:
                seen.add(raceName)
                results.append({
                    "url": base_url + href,
                    "race": raceName,
                    "year": year
                })
    
    return results


def extract_race_results(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        table = soup.find("tbody")
        rows = table.find_all("tr")
        
        race_results = []
        for row in rows[0:]:  
            cols = row.find_all("td")
            if len(cols) > 0:
                result = {
                "Pos": cols[0].text.strip(),  
                "Driver": cols[2].text.strip(), 
                "DriverNum": cols[1].text.strip(),  
                "Constructor": cols[3].text.strip(),  
                "Laps": cols[4].text.strip(),                           
                "TimeToLeader": cols[5].text.strip()     
                        
                      
                }
                race_results.append(result)
        
        return race_results
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return []


def more_fucking_aroud():
    resultsByYear = {}

    for i in range(1950, current_year + 1):
        print(f"Scraping results for year: {i}")
        race_urls = Scrap(i)
        
        year_results = []
        
        for race in race_urls:
            print(f"Extracting results for {race['race']} ({race['year']})")
            race_results = extract_race_results(race['url'])
            if race_results:  # Only append if there are results
                year_results.append({
                    "race": race['race'],
                    "year": race['year'],
                    "results": race_results
                })
        
        resultsByYear[i] = year_results
    
    return resultsByYear


# Run the scraping and saving the results
data = more_fucking_aroud()

with open("race_results.json", "w") as f:
    json.dump(data, f, indent=4)


