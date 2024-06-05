from tkinter import*
import requests
import json
from tkinter.messagebox import*


def get_weather_info():
    api_key = "216eaf8cd17c316cb683c726619ffa28"
    city = city_entry.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    res = requests.get(url)
    json_data = json.loads(res.text)

    weather = json_data["weather"][0]["description"]
    temprature = json_data["main"]["temp"]
    humidity=json_data["main"]["humidity"]
    wind_speed=json_data["wind"]["speed"]

    showinfo(f'{city.title()} weather',f'weather: {weather} \n Temprature : {temprature} \n Humidity : {humidity}'
             f'{humidity} \n wind speed : {wind_speed}')

root = Tk()
root.title = ("weather app")

app_lable = Label(root, text="weather app", font=("fines",29,"bold"))
app_lable.grid(row=0,column=0,columnspan=2)

city_lable = Label(root, text="Enter city name :")
city_lable.grid(row=1,column=0,columnspan=2)

city_entry = Entry(root, width=30)
city_entry.grid(row=1,column=1,pady=10)

btn = Button(root, text= "get weather info", bd=1, command='get_weather_info')
btn.grid(row=2,column=2,pady=10)

root.mainloop()


