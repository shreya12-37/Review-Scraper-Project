import tkinter as tk
from tkinter import ttk
from tkinter import * 
root= tk.Tk()
root.title('Review Scraper')

canvas1 = tk.Canvas(root, width = 450, height = 230)
canvas1.pack()
Label(root, text='Enter Product URL :', font=('helvetica', 12, 'normal')).place(x=50, y=50)
entry1 = tk.Entry (root, text='Enter product URL:',bg='#F0F8FF')
entry1.config(font=('helvetica', 12))
entry1.place(x=220, y=50)
# canvas1.create_window(200, 100, window=entry1)
Label(root, text='Enter No. of Reviews :', font=('helvetica', 12, 'normal')).place(x=50, y=100)
entry2 = tk.Entry (root, text='Enter number of reviews required:',bg='#F0F8FF')
entry2.config(font=('helvetica', 12))
entry2.place(x=220, y=100)
# canvas1.create_window(200, 150, window=entry2)

def reviewScraping ():  
    x = entry1.get()
    y = entry2.get()
    #scraping code to be added 
    # canvas1.create_window(200, 200, window=label1)
    
button1 = tk.Button(text='Display reviews',font=('helvetica', 12, 'normal'), command=reviewScraping).place(x=150, y=150)
# canvas1.create_window(200, 200, window=button1)


root.mainloop()
