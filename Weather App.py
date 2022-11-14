from tkinter import *
from time import *
from tkinter import messagebox
import requests
from datetime import *

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
window_icon = PhotoImage(file = "window_logo.png")
root.iconphoto(True,window_icon)
def getWeather():
    try:
        city = textfield.get()
        #from previous built console app
        api_key = 'e798e607e1456324fab3003655336dc9'
        weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")


        if weather_data.json()['cod'] == '404' or weather_data.json()['cod'] == '401':  
            #error message
             messagebox.showerror("Weather App","Invalid Entry")
        else:      
            #extracting Data from json 
            weather = weather_data.json()['weather'][0]['description']
            Condition = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])
            humidity = round(weather_data.json()['main']['humidity'])
            wind= round(weather_data.json()['wind']['speed'])
            #preassure = round(weather_data.json()['main']['preassure'])
            visibility = round(weather_data.json()['visibility'])

            t.config(text=(temp,"º"))
            c.config(text = (Condition,"|","FEELS", "LIKE", temp, "º"))

            w.config(text = wind)
            h.config(text = humidity)
            d.config(text = weather) 
            #p.config(text = preassure)
            v.config(text = visibility)

    except Exception as e:
        #error messege
        messagebox.showerror("Weather App","Invalid Entry" +"\n Or" + "\nNo Internet Connection Available")

Search_image = PhotoImage(file="search.png")
myimage = Label(image = Search_image)
myimage.place(x=20,y=20)

textfield = Entry(root,justify = "center", width = 17, font=("poppins",25,"bold"),bg = "#404040",border = 0, fg = "white")
textfield.place(x = 50, y = 40)
textfield.focus()

Search_icon = PhotoImage(file = "search_icon.png")
myimage_icon = Button(image = Search_icon,borderwidth = 0, cursor = "hand2", bg = "#404040",command = getWeather)
myimage_icon.place(x = 400, y = 34)

#logo
Logo_image = PhotoImage(file = "logo.png")
logo = Label(image = Logo_image)
logo.place(x = 150, y = 100) 

Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image = Frame_image)
frame_myimage.pack(padx=5, pady=5, side="bottom")

#time
name = Label(root,font = ("arial",15,"bold"))
name.place(x = 30, y =100)
clock = Label(root,font = ("Helvetica",20))
clock.place(x = 30, y = 130)

#label
label1 = Label(root,text="WIND", font=("Helvetica",15,'bold'),fg = "white",bg = "#1ab5ef")
label1.place(x = 120, y =400)

label2 = Label(root,text="HUMIDTY", font=("Helvetica",15,'bold'),fg = "white",bg = "#1ab5ef")
label2.place(x = 250 , y =400)

label3 = Label(root,text="DESCRIPTION", font=("Helvetica",15,'bold'),fg = "white",bg = "#1ab5ef")
label3.place(x = 430, y =400)

label4 = Label(root,text="VISIBILITY ", font=("Helvetica",15,'bold'),fg = "white",bg = "#1ab5ef")
label4.place(x = 650, y =400)

t = Label(font = ("arial",70,"bold"),fg = "#ee666d")
t.place(x = 400,y = 150)
c = Label(font=("arial",15,"bold"))
c.place(x = 400,y =250)

w = Label(text = "...",font=("arial",20,"bold"),bg = "#1ab5ef")
w.place(x =120, y = 430)
h = Label(text = "...",font=("arial",20,"bold"),bg = "#1ab5ef")
h.place(x =280, y = 430)
d = Label(text = "...",font=("arial",20,"bold"),bg = "#1ab5ef")
d.place(x =450, y = 430)
v = Label(text = "...",font=("arial",20,"bold"),bg = "#1ab5ef")
v.place(x =670, y = 430)

root.mainloop()