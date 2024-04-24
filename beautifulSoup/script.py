from bs4 import BeautifulSoup
import requests

website = 'https://www.nba.com/stats/players/traditional?PerMode=Totals&sort=PTS&dir=-1'

result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())



