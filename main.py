from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = tk.Tk()
root.title("weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj= TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather 
    api=f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&units=metric&exclude=hourly,daily&APPID={Api_key}"
    json_data=requests.get(api).json()
    print(json_data)
    temp=json_data["main"]["temp"]
    humidity=json_data["main"]["humidity"]
    pressure=json_data["main"]["pressure"]
    wind=json_data["wind"]['speed']
    description=json_data["weather"][0]['description']

    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)



    #days
    first=datetime.now()
    day1.config(text=first.strftime("%A"))

    second=first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third=first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourht=first + timedelta(days=3)
    day4.config(text=fourht.strftime("%A"))

    fifth=first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth=first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh=first + timedelta(days=5)
    day7.config(text=seventh.strftime("%A"))

##icon

#  

#label
label1=Label(root,text="Temperature",font=('helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity ",font=('helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure",font=('helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4=Label(root,text="Wind speed",font=('helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5=Label(root,text="Description",font=('helvetica',11),fg="white",bg="#203243")
label5.place(x=50,y=200)

##search box
Search_image=PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)
weat_image=PhotoImage(file="Images/Layer 7.png")
weatherimage=Label(image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

search_icon=PhotoImage(file="Images/Layer 6.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)


## Bottom box
frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)


## bottom boxes

first_box=PhotoImage(file="Images/Rounded Rectangle 2.png")
second_box=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")
Label(frame,image=first_box,bg="#212120").place(x=30,y=30)
Label(frame,image=first_box,bg="#212120").place(x=300,y=30)
Label(frame,image=first_box,bg="#212120").place(x=400,y=30)
Label(frame,image=first_box,bg="#212120").place(x=500,y=30)
Label(frame,image=first_box,bg="#212120").place(x=600,y=30)
Label(frame,image=first_box,bg="#212120").place(x=700,y=30)
Label(frame,image=first_box,bg="#212120").place(x=800,y=30)

#clock
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

#longitude
long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)

### th
t=Label(root,font=('helvetica',11),fg="white",bg="#203243")
t.place(x=150,y=120)

h=Label(root,font=('helvetica',11),fg="white",bg="#203243")
h.place(x=150,y=140)

p=Label(root,font=('helvetica',11),fg="white",bg="#203243")
p.place(x=150,y=160)

w=Label(root,font=('helvetica',11),fg="white",bg="#203243")
w.place(x=150,y=180)

d=Label(root,font=('helvetica',11),fg="white",bg="#203243")
d.place(x=150,y=200)




## first cell
firstframe=Frame(root,width=230,height=132,bg="#282829")
firstframe.place(x=35,y=325)

day1=Label(firstframe,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

## second cell
secondframe=Frame(root,width=95,height=130,bg="#282829")
secondframe.place(x=305,y=325)

day2=Label(secondframe,font="arial 20",bg="#282829",fg="#fff")
day2.place(x=200,y=5)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

## third cell
thirdframe=Frame(root,width=95,height=130,bg="#282829")
thirdframe.place(x=405,y=325)

day3=Label(thirdframe,font="arial 20",bg="#282829",fg="#fff")
day3.place(x=300,y=5)

thirdimage=Label(thirdframe,bg="#282829")
thirdimage.place(x=1,y=15)


## fourth cell
fourthframe=Frame(root,width=95,height=130,bg="#282829")
fourthframe.place(x=505,y=325)

day4=Label(fourthframe,font="arial 20",bg="#282829",fg="#fff")
day4.place(x=400,y=5)

fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=1,y=15)

## fifth cell
fifthframe=Frame(root,width=95,height=130,bg="#282829")
fifthframe.place(x=605,y=325)

day5=Label(fifthframe,font="arial 20",bg="#282829",fg="#fff")
day5.place(x=500,y=5)

fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=1,y=15)

## sixth cell
sixthframe=Frame(root,width=95,height=130,bg="#282829")
secondframe.place(x=705,y=325)

day6=Label(sixthframe,font="arial 20",bg="#282829",fg="#fff")
day6.place(x=600,y=5)

sixthimage=Label(sixthframe,bg="#282829")
sixthimage.place(x=1,y=15)

## seventh cell
seventhframe=Frame(root,width=95,height=130,bg="#282829")
seventhframe.place(x=805,y=325)

day7=Label(seventhframe,font="arial 20",bg="#282829",fg="#fff")
day7.place(x=700,y=5)

seventhimage=Label(seventhframe,bg="#282829")
seventhimage.place(x=1,y=15)



root.mainloop()