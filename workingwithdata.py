#Knowing weather for the upcoming 7 days
import requests 
from datetime import datetime, timedelta
import pandas as pd

today = datetime.now()
weekago = today - timedelta(days=7) 

#format date for the api
start_date = weekago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# easily get tashkent weather for the past week 
url = f"https://api.open-meteo.com/v1/forecast?latitude=41.2995&longitude=69.2401&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
response = requests.get(url)
data = response.json()
print(data)


daily_data= data['daily']

dataframa= pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']


}
)
print(dataframa)


