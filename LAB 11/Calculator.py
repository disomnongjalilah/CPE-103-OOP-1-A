import tkinter as tk
import math

def calculate():
    try:
        result_value = eval(entry.get())
        result.set(result_value)
    except ZeroDivisionError:
        result.set("Error!")
    except Exception as e:
        result.set("Error!")

# Functions for number and operator buttons
def append_to_entry(value):
    current_text = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, current_text + value)

def clear():
    entry.delete(0, 'end')
    result.set("")


# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="light blue")
root.geometry('420x440')

# Create StringVar to hold the result
result = tk.StringVar()

# Create the layout
entry = tk.Entry(root, textvariable=result, font=('Arial', 20), bd=25, insertwidth=5, width=25,justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2), ('=',6,0)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, command=calculate, height=1, width=9, font=('Arial', 18)).grid(row=row, column=col, columnspan=10, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(root, text=text, command=lambda t=text: append_to_entry(t), height=1, width=9, font=('Arial', 18)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


# Configure grid to expand
for i in range(6):
       root.grid_columnconfigure(i, weight=1)


# Button for clear
tk.Button(root, text='C', command=clear, height=1, width=9, font=('Arial', 18)).grid(row=1, column=0, columnspan=10, padx=1, pady=1, sticky="nsew")


# Start the main loop
root.mainloop()


