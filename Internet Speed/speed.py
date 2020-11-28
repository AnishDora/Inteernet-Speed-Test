import tkinter as tk
import os
from tkinter import filedialog
import speedtest

s=speedtest.Speedtest()

def upload():
    result=s.upload()*pow(10,-6)
    final=round(result,2)
    mylabel = tk.Label(frame, text=str(final)+" Mbps",font=('Courier', 15))
    mylabel.place(relx=0.40, rely=0.25,height=65,width=150)
def download():
    result=s.download()*pow(10,-6)
    final=round(result,2)
    mylabel = tk.Label(frame, text=str(final)+" Mbps",font=('Courier', 15))
    mylabel.place(relx=0.40, rely=0.25,height=65,width=150)
def reset():
    mylabel = tk.Label(frame, text="0 Mbps",font=('Courier', 15))
    mylabel.place(relx=0.39, rely=0.25,height=65,width=150)


Height = 450
Width = 800

root = tk.Tk()


canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame = tk.Frame(root, bg='#301934')
frame.place(relwidth=1, relheight=1)

button1 = tk.Button(frame, text="Upload Speed", font=('Courier', 15), bd=3, bg="#d1d8e3",  command=lambda: upload())
button1.place(relx=0.07, rely=0.55, relheight=0.10, relwidth=0.25)

button2 = tk.Button(frame, text="Download Speed", font=('Courier', 15), bd=3, bg="#d1d8e3",  command=lambda: download())
button2.place(relx=0.37, rely=0.55, relheight=0.10, relwidth=0.25)


button3 = tk.Button(frame, text="Reset", font=('Courier', 15), bd=3, bg="#d1d8e3",  command=lambda: reset())
button3.place(relx=0.67, rely=0.55, relheight=0.10, relwidth=0.25)


text = tk.Label(frame, text="Welcome to Internet Speed Test", font=('Courier', 15), fg="white", bg='#301934')
text.place(relx=0.10, rely=0.65, relheight=0.5, relwidth=0.75)


text2 = tk.Label(frame, text="Wait for the result after clicking", font=('Courier', 15), fg="white", bg='#301934')
text2.place(relx=0.13, rely=0.10, relheight=0.05, relwidth=0.75)

root.mainloop()
