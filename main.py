import requests
import pandas


#This gets out your info like location,timezone etc

location_res = requests.get("https://ipinfo.io")
location_data = location_res.json()
lat , lon = location_data["loc"].split(",")



weather_res = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m")

weather_data = weather_res.json()

time_temp = {
    "time":[],
    "temp":[],
}

for i in range(24):
    time_temp["time"].append(weather_data["hourly"]["time"][i])
    time_temp["temp"].append(f"{weather_data["hourly"]["temperature_2m"][i]} Celsius")
    

data = pandas.DataFrame(time_temp)


print("Your location's temperature for today is as follows.")
print(data)
