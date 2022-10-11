from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from tkinter import Button
import random
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
import sklearn

splash_screen = Tk()
splash_screen.title("Splash Screen")
splash_screen.geometry("800x600")
photo_image = PhotoImage(file="./p2.png")
label = Label(splash_screen, image=photo_image)
label.place(x=0,y=0)

colors = ["purple", "red" , "green" ,"blue","orange"]

def color_changer1():
    fg = random.choice(colors)
    splash_screen_label.config(foreground=fg)
    splash_screen_label.after(100, color_changer1)

def main_window():
    splash_screen.destroy()
    root = Tk()

    root.title("Car Sales Prediction")
    colors = ["purple", "red", "green", "blue", "orange"]

    root.geometry("800x600")
    root.config(background = 'lightyellow')

    def color_changer1():
        fg = random.choice(colors)
        splash_screen_label.config(foreground=fg)
        splash_screen_label.after(100, color_changer1)

    def predict():
        br = brand.get()
        mod = model.get()
        bod = body.get()
        pric = price.get()
        mon = month.get()
        yer = year.get()

        pickled_model = pickle.load(open('model3.pkl', 'rb'))
        var2 = pickled_model.predict(pd.DataFrame([[br, mod, bod, pric, mon, yer]],columns=['OEM', 'MODEL', 'BODY TYPE', 'PRICE IN LAKHS', 'YEAR', 'MONTH']))
        print(var2[0])
        predict_val = int(var2[0])
        la = Label(root,text=predict_val,fg="red",bg="lightyellow",font="comicsansms 20 bold").place(x=320,y=500)
        la1 = Label(root,text="Cars",fg="red",bg="lightyellow",font="comicsansms 20 bold").place(x=430,y=500)


    lab1 = Label(root,text='BRAND NAME',bg="lightyellow",font="comicsansms 12 bold").place(x=60,y=160)
    brand = StringVar()
    ent1 = Entry(root,textvariable=brand,width=22,font="comicsansms 12 bold").place(x=188,y=160)

    lab2 = Label(root, text='MODEL',bg="lightyellow",font="comicsansms 12 bold").place(x=60,y=250)
    model = StringVar()
    ent2 = Entry(root,textvariable=model, width=22, font="comicsansms 12 bold").place(x=188, y=250)

    lab3 = Label(root, text='BODY TYPE',bg="lightyellow",font="comicsansms 12 bold").place(x=60,y=340)
    body = StringVar()
    ent3 = Entry(root, textvariable=body, width=22, font="comicsansms 12 bold").place(x=188, y=340)

    lab4 = Label(root, text='PRICE IN LAKHS',bg="lightyellow",font="comicsansms 12 bold").place(x=430,y=160)
    price = StringVar()
    ent4 = Entry(root,textvariable=price, width=22, font="comicsansms 12 bold").place(x=580, y=160)

    lab5 = Label(root, text='MONTH',bg="lightyellow",font="comicsansms 12 bold").place(x=430,y=250)
    month = StringVar()
    ent5 = Entry(root,textvariable=month, width=22, font="comicsansms 12 bold").place(x=580, y=250)

    lab6 = Label(root, text='YEAR',bg="lightyellow",font="comicsansms 12 bold").place(x=430,y=340)
    year = StringVar()
    ent6 = Entry(root, textvariable=year,width=22, font="comicsansms 12 bold").place(x=580, y=340)


    But1 = Button(root,text="PREDICT",fg="black",bg="lightblue",font="comicsansms 18 bold",command = predict)
    But1.place(x=335,y=430)
    splash_screen_label = Label(root,text='Car Sales Prediction',fg="red",bg="lightyellow",font="comicsansms 24 bold")
    splash_screen_label.place(x=250,y=10)
    color_changer1()

    root.mainloop()

splash_screen.after(3000,main_window)
splash_screen_label = Label(splash_screen,text = "Car Sales Prediction",bg="white",font="comicsansms 24 bold")
splash_screen_label.place(x=250,y=10)
color_changer1()
splash_screen.mainloop()