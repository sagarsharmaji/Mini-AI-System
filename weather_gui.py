from tkinter import *
import tkinter as tk
import pyttsx3
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("WEATHER FORECAST")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExcercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        #print(result)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+'&appid=7338e7357146d6c783067cc3a4b5bd03'
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        getWeather.temp = int(json_data['main']['temp']-273.15)
        getWeather.pressure = json_data['main']['pressure']
        getWeather.humidity = json_data['main']['humidity']
        getWeather.wind = json_data['wind']['speed']

        t.config(text=(getWeather.temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",getWeather.temp,"°"))

        w.config(text=getWeather.wind)
        h.config(text=getWeather.humidity)
        d.config(text=description)
        p.config(text=getWeather.pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!")

textfield = tk.Entry(root,justify="center",width=18,font=("TrebuchetMS",25,"bold"),bg="#404040",border=2,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=350,y=40)

#logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=180,y=140)

#Bottom Box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time

name = Label(root,font=("TrebuchetMS",15,"bold"))
name.place(x=30,y=100)
clock = Label(root,font=("TrebuchetMS",20))
clock.place(x=30,y=130)

#Label

label1 = Label(root,text="WIND",font=("TrebuchetMS",15,'bold'),fg="white",bg="#838B8B")
label1.place(x=120,y=350)

label2 = Label(root,text="HUMIDITY",font=("TrebuchetMS",15,'bold'),fg="white",bg="#838B8B")
label2.place(x=250,y=350)

label3 = Label(root,text="DESCRIPTION",font=("TrebuchetMS",15,'bold'),fg="white",bg="#838B8B")
label3.place(x=430,y=350)

label4 = Label(root,text="PRESSURE",font=("TrebuchetMS",15,'bold'),fg="white",bg="#838B8B")
label4.place(x=650,y=350)

t = Label(font=("TrebuchetMS",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)

c = Label(font=("TrebuchetMS",15,"bold"))
c.place(x=400,y=250)

w = Label(text="...",font=("TrebuchetMS",20,"bold"),bg="#838B8B")
w.place(x=125,y=430)

h = Label(text="...",font=("TrebuchetMS",20,"bold"),bg="#838B8B")
h.place(x=285,y=430)

d = Label(text="...",font=("TrebuchetMS",20,"bold"),bg="#838B8B")
d.place(x=455,y=430)

p = Label(text="...",font=("TrebuchetMS",20,"bold"),bg="#838B8B")
p.place(x=675,y=430)

root.mainloop()