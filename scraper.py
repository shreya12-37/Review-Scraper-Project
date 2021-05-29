import tkinter as tk

root= tk.Tk()
root.title('Review Scraper')

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root, text='Enter product URL:',bg='#F0F8FF')
entry1.config(font=('helvetica', 12))
canvas1.create_window(200, 100, window=entry1)

entry2 = tk.Entry (root, text='Enter number of reviews required:',bg='#F0F8FF')
entry2.config(font=('helvetica', 12))
canvas1.create_window(200, 150, window=entry2)

def reviewScraping ():  
    x = entry1.get()
    y = entry2.get()
    #scraping code to be added 
    canvas1.create_window(200, 200, window=label1)
    
button1 = tk.Button(text='Display reviews', command=reviewScraping)
canvas1.create_window(200, 200, window=button1)


root.mainloop()

