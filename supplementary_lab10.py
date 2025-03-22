import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter import messagebox
from tkinter.messagebox import showinfo

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')
window.configure(bg='pink')
icon = PhotoImage(file = "halloween11_109175.png")
window.iconphoto(False, icon)

def choice(event):
    month = event.widget.get()
    day = event.widget.get()
    year = event.widget.get()


# label text for title
ttk.Label(window, text='BIRTHDATE',
          background='pink', foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=0)

# Set label
ttk.Label(window, text="Select the month of your birth :", background='white',
          font=("Times New Roman", 12)).grid(column=0,
                                             row=5, padx=5, pady=25)
#Set Label for day
ttk.Label(window, text='Select the day of your birth', background='white',
          font=('Times New Roman', 12)).grid(column=0, row=6, padx=5, pady=25)

#label for year
ttk.Label(window, text='Select the year of your birth', background='white', font=('Times New Roman', 12)).grid(column=0, row=7, padx=5, pady=25)


# Create Combobox
n = tk.StringVar()
m = tk.StringVar()
o = tk.StringVar()

month = ttk.Combobox(window, width=27, textvariable=n)
day = ttk.Combobox(window, width=27, textvariable=m)
year = ttk.Combobox(window, width=27, textvariable=o)


# Adding combobox drop down list
month['values'] = (' January',
                     ' February',
                     ' March',
                     ' April',
                     ' May',
                     ' June',
                     ' July',
                     ' August',
                     'September',
                     'October',
                     'November',
                     'December')

month.grid(column=1, row=5)
month.current()

#day
day['values'] = ('1','2','3','4','5','6','7','8','9','10',
                 '10','11','12','13','14','15','16','17','18','19','20',
                 '21','22','23','24','25','26','27','28','29','30','31')

day.grid(column=1 ,  row=6)
day.current()

#year
year['values'] = ('2000','2001', '2002','2003','2004','2005','2006','2007',
                  '2008','2009','2010','2011','2012','2013','2014','2015',
                  '2016','2017','2018','2019','2020','2021','2022','2023')

year.grid(column=1, row=7)
year.current()

def choice(event):
    showinfo(
            title = "Selection",
            message = f'You selected {n.get()} {m.get()}, {o.get()}')


year.bind("<<ComboboxSelected>>", choice)
window.mainloop()