import tkinter as tk
import math

# Functions for calculation
def add():
    result_value = float(entry1.get()) + float(entry2.get())
    result.set(result_value)
    history.append(f"{entry1.get()} + {entry2.get()} = {result_value}")

def subtract():
    result_value = float(entry1.get()) - float(entry2.get())
    result.set(result_value)
    history.append(f"{entry1.get()} - {entry2.get()} = {result_value}")

def multiply():
    result_value = float(entry1.get()) * float(entry2.get())
    result.set(result_value)
    history.append(f"{entry1.get()} * {entry2.get()} = {result_value}")

def divide():
    try:
        result_value = float(entry1.get()) / float(entry2.get())
        result.set(result_value)
        history.append(f"{entry1.get()} / {entry2.get()} = {result_value}")
    except ZeroDivisionError:
        result.set("Error! Division by zero.")
        history.append("Error! Division by zero.")

def square_roots():
    try:
        result_value = math.sqrt(float(entry1.get()))
        result.set(result_value)
        history.append(f"Square root of {entry1.get()} = {result_value}")
    except ValueError:
        result.set("Error! Invalid input.")
        history.append("Square root: Error! Invalid input.")

def power():
    result_value = float(entry1.get()) ** float(entry2.get())
    result.set(result_value)
    history.append(f"{entry1.get()} ^ {entry2.get()} = {result_value}")



# Function for clear
def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result.set(" ")

# Function for history
def show_history(history_display, history):
    history_display.config(state='normal')
    history_display.delete(1.0, tk.END)
    for entry in history:
        history_display.insert(tk.END, entry + "\n")
    history_display.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="light coral")

# Create StringVar to hold the result
result = tk.StringVar()

# Create the layout
tk.Label(root, text="Enter first number:", bg='light pink', fg='white').grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:", bg='light pink', fg='white').grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Buttons for operations
tk.Button(root, text="Add", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=2, column=2)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=0)
tk.Button(root, text="Square roots", command=square_roots).grid(row=3, column=1)
tk.Button(root, text="Powers", command=power).grid(row=3, column=2)

# Button for clear
tk.Button(root, text='Clear', command=clear).grid(row=4, column=0)

# History display
history_display = tk.Text(root, state='disabled', width=30, height=5)
history_display.grid(row=5, column=0, columnspan=2)

# Button for showing history
history = []  # Initialize an empty history list
tk.Button(root, text='Show History', command=lambda: show_history(history_display, history)).grid(row=6, column=0, columnspan=2)

# Label to show result
tk.Label(root, text="Result:").grid(row=4, column=1)
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=4, column=2)

# Start the main loop
root.mainloop()