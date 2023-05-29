import requests
from bs4 import BeautifulSoup

radiant = input().split()
dire = input().split()
total = 0

for radiant_hero in radiant:
    for dire_hero in dire:
        url = "https://www.dotabuff.com/heroes/" + radiant_hero + "/counters"

        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
                   'accept': '*/*'}

        req = requests.get(url, headers=headers)
        src = req.text

        soup = BeautifulSoup(src, "lxml")
        winrate = soup.find("tr", {"data-link-to": "/heroes/" +
                dire_hero}).find(class_="bar").next_element.next_element.text

        winrate = round(float(winrate.replace("%", "")) - 50, 2)
        total += winrate

total = round(total, 2)

if total >= 1:
    print("Radiant!", end=" ")
elif total <= -1:
    print("Dire", end=" ")
else:
    print("Pass", end=" ")

print(total)
