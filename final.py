import tkinter as tk
from tkinter import ttk
from tkinter import * 
from threading import Thread 
import subprocess 
from amazon_reviews import *

root= tk.Tk()
root.title('Review Scraper')

canvas1 = tk.Canvas(root, width = 450, height = 230)
canvas1.pack()
Label(root, text='Enter Product URL :', font=('helvetica', 12, 'normal')).place(x=50, y=50)
entry1 = tk.Entry (root, text='Enter product URL:',bg='#F0F8FF')
entry1.config(font=('helvetica', 12))
entry1.place(x=220, y=50)
# canvas1.create_window(200, 100, window=entry1)
Label(root, text='Enter No. of pages :', font=('helvetica', 12, 'normal')).place(x=50, y=100)
entry2 = tk.Entry (root, text='Enter number of pages required:',bg='#F0F8FF')
entry2.config(font=('helvetica', 12))
entry2.place(x=220, y=100)
# canvas1.create_window(200, 150, window=entry2)
x = entry1.get()
y = entry2.get()

def scrape():
    process = subprocess.run('scrapy runspider amazon_reviews.py -o output.csv', shell= True)

# Command to run scraping code is 
# scrapy runspider amazon_reviews.py -o reviews.csv

def display():  
    label.config(text="Reviews saved to device as output.csv")
label= Label(root, text= "", font= ('aerial 18 bold'))
label.pack(pady= 20) 
button1 = tk.Button(text='Get CSV file of scraped data',font=('helvetica', 12, 'normal'), command=lambda: [scrape(), display()]).place(x=150, y=150)
# canvas1.create_window(200, 200, window=button1)


root.mainloop()

