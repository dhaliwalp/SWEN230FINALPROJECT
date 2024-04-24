import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import time
import numpy as np

test_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2023-24&SeasonType=Regular%20Season&StatCategory=PTS'

r = requests.get(url=test_url).json()

print(r)