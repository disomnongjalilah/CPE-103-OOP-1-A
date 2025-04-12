import tkinter as tk
import math

# Function to handle the calculation logic
def calculate():
    try:
        expression = entry.get().replace('^', '**').replace('÷', '/').replace('×', '*').replace('√', 'math.sqrt(')

        if expression.count('(') > expression.count(')'):
            expression += ')'
        result_value = eval(expression)
        result.set(result_value)
    except ZeroDivisionError:
        result.set("Error: Division by zero!")
    except Exception as e:
        result.set("Error!")


def append_to_entry(value):
    current_text = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, current_text + value)

def clear():
    entry.delete(0, 'end')
    result.set("")


def calculate_sin():
    try:
        result_value = math.sin(float(entry.get()))
        result.set(result_value)
    except Exception:
        result.set("Error!")

def calculate_cos():
    try:
        result_value = math.cos(float(entry.get()))
        result.set(result_value)
    except Exception:
        result.set("Error!")

def calculate_tan():
    try:
        result_value = math.tan(float(entry.get()))
        result.set(result_value)
    except Exception:
        result.set("Error!")

def insert_pi():
    append_to_entry(str(math.pi))


root = tk.Tk()
root.title("Calculator")
root.configure(bg="pink")
root.geometry('420x460')


result = tk.StringVar()


entry = tk.Entry(root, textvariable=result, font=('Arial', 20, 'bold'), bd=15, insertwidth=5, width=25, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ('√', 3, 0), ('C', 2, 3), ('%', 3, 1), ('π', 7, 0),
    ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2), ('^', 3, 2),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('÷', 3, 3),
    ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('×', 4, 3),
    ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 5, 3),
    ('0', 7, 1), ('.', 7, 2), ('+', 6, 3), ('=', 7, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, command=calculate, height=1, width=9, font=('Arial', 18, 'bold'), bg='white').grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == 'sin':
        tk.Button(root, text=text, command=calculate_sin, height=1, width=9, bg='lightcoral', font=('Arial', 18, 'bold')).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == 'cos':
        tk.Button(root, text=text, command=calculate_cos, height=1, width=9, bg='lightcoral', font=('Arial', 18, 'bold')).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == 'tan':
        tk.Button(root, text=text, command=calculate_tan, height=1, width=9, bg='lightcoral', font=('Arial', 18, 'bold')).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == 'π':
        tk.Button(root, text=text, command=insert_pi, height=1, width=9, bg='lightcoral', font=('Arial', 18, 'bold')).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == 'C':
        tk.Button(root, text=text, command=clear, height=1, width=9, bg='lightcoral', font=('Arial', 18, 'bold')).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    elif text == '√':
        tk.Button(root, text=text, command=lambda: append_to_entry('√'), height=1, width=9, bg='lightcoral', font=('Arial', 18, 'bold')).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(root, text=text, command=lambda t=text: append_to_entry(t), height=1, width=9, font=('Arial', 18, 'bold'), bg='lightcoral').grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(8):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
