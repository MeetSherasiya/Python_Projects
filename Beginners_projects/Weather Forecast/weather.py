from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import keys



root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False,False)


def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExcercises")
    location =geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock_text.config(text=f"Current {city} Time")
    clock.config(text=current_time)

    #************* weather *****************
    js_data =  requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid="+ keys.api_key)
    json_data = js_data.json()

    #************* current *****************

    temp = "{:.2f}".format(json_data['current']['temp']-273.15)
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)

    #*********** First cell *******************
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']

    photo1 = ImageTk.PhotoImage(file=f"Beginners_projects/Weather Forecast/icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1 = "{:.2f}".format(json_data['daily'][0]['temp']['day']-273.15)
    tempnight1 = "{:.2f}".format(json_data['daily'][0]['temp']['night']-273.15)

    day1temp.config(text=f"Day:{tempday1}")
    day1tempnight.config(text=f"Night:{tempnight1}")


    #*********** second cell *******************
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']

    img = (Image.open(f"Beginners_projects/Weather Forecast/icon/{seconddayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    tempday2 = "{:.2f}".format(json_data['daily'][1]['temp']['day']-273.15)
    tempnight2 = "{:.2f}".format(json_data['daily'][1]['temp']['night']-273.15)

    day2temp.config(text=f"Day:{tempday2}")
    day2tempnight.config(text=f"Night:{tempnight2}")


    #*********** third cell *******************
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']

    img = (Image.open(f"Beginners_projects/Weather Forecast/icon/{thirddayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3

    tempday3 = "{:.2f}".format(json_data['daily'][2]['temp']['day']-273.15)
    tempnight3 = "{:.2f}".format(json_data['daily'][2]['temp']['night']-273.15)

    day3temp.config(text=f"Day:{tempday3}")
    day3tempnight.config(text=f"Night:{tempnight3}")


    #*********** fourth cell *******************
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']

    img = (Image.open(f"Beginners_projects/Weather Forecast/icon/{fourthdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4

    tempday4 = "{:.2f}".format((json_data['daily'][3]['temp']['day'])-273.15)
    tempnight4 = "{:.2f}".format(json_data['daily'][3]['temp']['night']-273.15)

    day4temp.config(text=f"Day:{tempday4}")
    day4tempnight.config(text=f"Night:{tempnight4}")



    #*********** fifth cell *******************
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']

    img = (Image.open(f"Beginners_projects/Weather Forecast/icon/{fifthdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5

    tempday5 = "{:.2f}".format(json_data['daily'][4]['temp']['day']-273.15)
    tempnight5 = "{:.2f}".format(json_data['daily'][4]['temp']['night']-273.15)

    day5temp.config(text=f"Day:{tempday5}")
    day5tempnight.config(text=f"Night:{tempnight5}")


    #*********** sixth cell *******************
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']

    img = (Image.open(f"Beginners_projects/Weather Forecast/icon/{sixthdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6

    tempday6 = "{:.2f}".format(json_data['daily'][5]['temp']['day']-273.15)
    tempnight6 = "{:.2f}".format(json_data['daily'][5]['temp']['night']-273.15)

    day6temp.config(text=f"Day:{tempday6}")
    day6tempnight.config(text=f"Night:{tempnight6}")


    #*********** seventh cell *******************
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    img = (Image.open(f"Beginners_projects/Weather Forecast/icon/{seventhdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7

    tempday7 = "{:.2f}".format(json_data['daily'][6]['temp']['day']-273.15)
    tempnight7 = "{:.2f}".format(json_data['daily'][6]['temp']['night']-273.15)

    day7temp.config(text=f"Day:{tempday7}")
    day7tempnight.config(text=f"Night:{tempnight7}")




    #*********** Days *******************

    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = second+timedelta(days=1)
    day3.config(text=third.strftime("%A"))

    fourth = third+timedelta(days=1)
    day4.config(text=fourth.strftime("%A"))

    fifth = fourth+timedelta(days=1)
    day5.config(text=fifth.strftime("%A"))

    sixth = fifth+timedelta(days=1)
    day6.config(text=sixth.strftime("%A"))

    seventh = sixth+timedelta(days=1)
    day7.config(text=seventh.strftime("%A"))






#**************** icon *******************************
image_icon = PhotoImage(file="Beginners_projects/Weather Forecast/Images/logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file="Beginners_projects/Weather Forecast/Images/Rounded Rectangle 4.png")
Label(root, image=Round_box, bg="#57adff").place(x=20, y=180)


#**************** label *******************************
label1 = Label(root, text="Temprature", font=("Helvetica", 14), fg="white", bg="#203243")
label1.place(x=50, y=190)

label2 = Label(root, text="Humidity", font=("Helvetica", 14), fg="white", bg="#203243")
label2.place(x=200, y=190)

label3 = Label(root, text="Pressure", font=("Helvetica", 14), fg="white", bg="#203243")
label3.place(x=350, y=190)

label4 = Label(root, text="Wind Speed", font=("Helvetica", 14), fg="white", bg="#203243")
label4.place(x=500, y=190)

label5 = Label(root, text="Description", font=("Helvetica", 14), fg="white", bg="#203243")
label5.place(x=700, y=190)


#**************** Search Box *******************************
Search_image = PhotoImage(file="Beginners_projects/Weather Forecast/Images/Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=330, y=20)


weat_image = PhotoImage(file="Beginners_projects/Weather Forecast/Images/Layer 7.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=350, y=27)

textfield = tk.Entry(root, justify='center', width=13, font=('poppins', 25, 'bold'), bg="#203242", border=0, fg="white")
textfield.place(x=430, y=30)
textfield.focus()


Search_icon = PhotoImage(file="Beginners_projects/Weather Forecast/Images/Layer 6.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=705, y=25)


#**************** Bottom Box *******************************

frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)


#**************** Bottom Boxes *******************************
firstbox = PhotoImage(file="Beginners_projects/Weather Forecast/Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Beginners_projects/Weather Forecast/Images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=20, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=290, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=390, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=490, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=590, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=690, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=790, y=30)



#**************** Clock (here we will place time) *******************************

clock_text = Label(root, font=("Helvetica", 20, 'bold'), fg="white", bg="#57adff")
clock_text.place(x=20, y=20)
clock = Label(root, font=("Helvetica", 15, 'bold'), fg="white", bg="#57adff")
clock.place(x=20, y=60)



#**************** Timezone *******************************

timezone = Label(root, font=("Helvetica", 20, 'bold'), fg="white", bg="#57adff")
timezone.place(x= 20, y=90)

long_lat = Label(root, font=("Helvetica", 10, 'bold'), fg="white", bg="#57adff")
long_lat.place(x= 20, y=125)


#**************** thpwd *******************************

t = Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
t.place(x=50, y=220)

h = Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
h.place(x=200, y=220)

p = Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
p.place(x=350, y=220)

w = Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
w.place(x=500, y=220)

d = Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
d.place(x=700, y=220)







#**************** first cell *******************************
firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=25, y=315)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=120, y=15)

day1 = Label(firstframe, font=("arial 20"), bg="#282829", fg="#fff")
day1.place(x=2, y=3)

day1temp = Label(firstframe, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=2, y=50)

day1tempnight = Label(firstframe, bg="#282829", fg="#57adff", font="arial 15 bold")
day1tempnight.place(x=2, y=75)


#**************** second cell *******************************
secondframe = Frame(root, width=70, height=115, bg="#282829")
secondframe.place(x=295, y=325)

secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=2, y=20)

day2 = Label(secondframe, font=("arial 10"), bg="#282829", fg="#fff")
day2.place(x=2, y=3)

day2temp = Label(secondframe, bg="#282829", fg="#fff")
day2temp.place(x=2, y=70)

day2tempnight = Label(secondframe, bg="#282829", fg="#fff")
day2tempnight.place(x=2, y=85)


#**************** third cell *******************************
thirdframe = Frame(root, width=70, height=115, bg="#282829")
thirdframe.place(x=395, y=325)

thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=2, y=20)

day3 = Label(thirdframe, font=("arial 10"), bg="#282829", fg="#fff")
day3.place(x=2, y=3)

day3temp = Label(thirdframe, bg="#282829", fg="#fff")
day3temp.place(x=2, y=70)

day3tempnight = Label(thirdframe, bg="#282829", fg="#fff")
day3tempnight.place(x=2, y=85)


#**************** fourth cell *******************************
fourthframe = Frame(root, width=70, height=115, bg="#282829")
fourthframe.place(x=495, y=325)

fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=2, y=20)

day4 = Label(fourthframe, font=("arial 10"), bg="#282829", fg="#fff")
day4.place(x=2, y=3)

day4temp = Label(fourthframe, bg="#282829", fg="#fff")
day4temp.place(x=2, y=70)

day4tempnight = Label(fourthframe, bg="#282829", fg="#fff")
day4tempnight.place(x=2, y=85)


#**************** fifth cell *******************************
fifthframe = Frame(root, width=70, height=115, bg="#282829")
fifthframe.place(x=595, y=325)

fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=2, y=20)

day5 = Label(fifthframe, font=("arial 10"), bg="#282829", fg="#fff")
day5.place(x=2, y=3)

day5temp = Label(fifthframe, bg="#282829", fg="#fff")
day5temp.place(x=2, y=70)

day5tempnight = Label(fifthframe, bg="#282829", fg="#fff")
day5tempnight.place(x=2, y=85)


#**************** sixth cell *******************************
sixthframe = Frame(root, width=70, height=115, bg="#282829")
sixthframe.place(x=695, y=325)

sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=2, y=20)

day6 = Label(sixthframe, font=("arial 10"), bg="#282829", fg="#fff")
day6.place(x=2, y=3)

day6temp = Label(sixthframe, bg="#282829", fg="#fff")
day6temp.place(x=2, y=70)

day6tempnight = Label(sixthframe, bg="#282829", fg="#fff")
day6tempnight.place(x=2, y=85)


#**************** seventh cell *******************************
seventhframe = Frame(root, width=70, height=115, bg="#282829")
seventhframe.place(x=795, y=325)

seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=2, y=20)

day7 = Label(seventhframe, font=("arial 10"), bg="#282829", fg="#fff")
day7.place(x=2, y=3)

day7temp = Label(seventhframe, bg="#282829", fg="#fff")
day7temp.place(x=2, y=70)

day7tempnight = Label(seventhframe, bg="#282829", fg="#fff")
day7tempnight.place(x=2, y=85)





root.mainloop()