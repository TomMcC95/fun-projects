# import required modules
from datetime import date, timedelta
from suntime import Sun
from geopy.geocoders import Nominatim
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pytz
 
places = ['Aberdeen', 'Devon']

start = '2019-12-31'
end = '2020-12-31'

start_date = date.fromisoformat(start)
end_date = date.fromisoformat(end)

date_range = list(reversed([(end_date - timedelta(days=i)) for i in range((end_date - start_date).days)]))

place_list = []
date_list = []
sunrise_hour_list = []
sunrise_min_list = []
sunset_hour_list = []
sunset_min_list = []

tz = pytz.timezone('GMT')

for place in places:

    for dt in date_range:

        # Nominatim API to get latitude and longitude
        geolocator = Nominatim(user_agent="geoapiExercises")
        
        # input place
        location = geolocator.geocode(place)
        
        # latitude and longitude fetch
        latitude = location.latitude
        longitude = location.longitude
        sun = Sun(latitude, longitude)
 
        # date in your machine's local time zone but can be converted to whatever is necessary.
        sun_rise = sun.get_local_sunrise_time(dt).astimezone(tz)
        sun_set = sun.get_local_sunset_time(dt).astimezone(tz)

        place_list.append(place)
        date_list.append(dt.isoformat())
        sunrise_hour_list.append(sun_rise.strftime('%H'))
        sunrise_min_list.append(sun_rise.strftime('%M'))
        sunset_hour_list.append(sun_set.strftime('%H'))
        sunset_min_list.append(sun_set.strftime('%M'))

df_data = [place_list, date_list, sunrise_hour_list, sunrise_min_list, sunset_hour_list, sunset_min_list]
df_columns = ["Location", "Date", "Sun_Rise_Hour", "Sun_Rise_Min", "Sun_Set_Hour", "Sun_Set_Min"]

df = pd.DataFrame(df_data).transpose()
df.columns = df_columns

print(df.head())

df['Sun_Rise'] = df['Sun_Rise_Hour'].astype(int) + (df['Sun_Rise_Min'].astype(int) / 60)
df['Sun_Set'] = df['Sun_Set_Hour'].astype(int) + (df['Sun_Set_Min'].astype(int) / 60)

xticks = [dt.isoformat() for dt in date_range if dt.day == 1]
xlabels = [dt.strftime("%b") for dt in date_range if dt.day == 1]

yticks = [i*4 for i in range(7)]
ylabels = [("000" + str(i*400))[-4:] for i in range(7)]
    

g0 = sns.lineplot(data = df, x = 'Date', y = 'Sun_Rise', hue='Location', palette="flare")
g0.set_xlabel('Date')
g0.set_xticks(xticks, xlabels)
g0.set_ylabel('Sunrise')
g0.set_ylim(0, 24)
g0.set_yticks(yticks, ylabels)

g1 = sns.lineplot(data = df, x = 'Date', y = 'Sun_Set', hue='Location', ax=g0.axes.twinx(), palette="flare")
g1.set_ylabel('Sunset')
g1.set_ylim(0, 24)

plt.show()