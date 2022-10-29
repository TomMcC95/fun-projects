import requests
import datetime
import time
import pandas as pd
 
# API KEY
API_key = "c401a909b7f91296c928b3924d5a12c3"
lat = 54.586312
lon = -5.821666
start = time.mktime(datetime.datetime(2021, 8, 1, 0, 0).timetuple())
end = time.mktime(datetime.datetime(2021, 8, 2, 0, 0).timetuple())
 
# This stores the url
base_url = f"http://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={API_key}"
 
# this variable contain the JSON data which the API returns
weather_data = requests.get(base_url).json()

df = pd.json_normalize(weather_data)


print(df.head())
