import tkinter as tk
from tkinter import StringVar
import customtkinter as ctk
import math
def evaluate(expression):
    def iterate_number(value):
        num = ""
        characters = []
        prev = None
        
        for char in value:
            if char in "+-*/!^":
                if num:
                    characters.append(float(num))
                    num = ""
                
                if char == '-' and (prev is None or prev in '+-*/!^'):
                    num += char
                else:
                    characters.append(char)
            elif char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    characters.append(float(num))
                    num = ""
                characters.append(char)
            
            prev = char
        
        if num:
            characters.append(float(num))
        
        return characters


    def operation(operators, values):
        
       
        
        operator = operators.pop()
        
        if operator == '!':
            val= values.pop()
            values.append(math.factorial(int(val)))
        else:
            rval = values.pop()
            lval = values.pop()
            if operator == '+':
                values.append(lval + rval)
            elif operator == '-':
                values.append(lval - rval)
            elif operator == '*':
                values.append(lval * rval)
            elif operator == '/':
                values.append(lval / rval)
            elif operator== '^':
                values.append(lval**rval)
        
    characters = iterate_number(expression)
    values = []
    operators = []
    
    mdas = {'+': 1, '-': 1, '*': 2, '/': 2, '!':3, '^': 4}
    for c in characters:
        if isinstance(c, float):
            values.append(c)
        else:
            while (operators and mdas[operators[-1]] >= mdas[c]):
                operation(operators, values)
            operators.append(c)
    while operators:
        operation(operators, values)

    return values[0]

def calculator():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")
    
    root = ctk.CTk()
    root.title("Calculator")
    root.geometry("490x600")
    root.configure(bg='pink')
    
    frame = tk.Frame(root, bg='pink')
    frame.pack(fill=tk.BOTH, expand=True)
    
    display_var = StringVar()
    entry = ctk.CTkEntry(frame, textvariable=display_var, width=400, height=100, font=('Arial', 25), justify='right')
    entry.place(x=45, y=25)
    
    def update_entry(value):
        current_entry = display_var.get()
        display_var.set(current_entry + value)
     
    def equals():
        try:
            entries = display_var.get() 
            result = evaluate(entries)
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    
        
    # def factorial():
    #     try:
    #         current_entry = display_var.get()
    #         number = int(current_entry)
    #         result = 1
    #         for i in range(1, number + 1):
    #             result *= i
    #         display_var.set(result)
    #     except Exception as e:
    #         display_var.set("Error")
    def clear_display():
        display_var.set("")
        
    def backspace():
        current_entry = display_var.get()
        display_var.set(current_entry[:-1])
    
    button_texts = [
        ("!", 30, 150), ("^", 140, 150), ("←", 250, 150), ("/", 360, 150),
        ("7", 30, 230), ("8", 140, 230), ("9", 250, 230), ("*", 360, 230),
        ("4", 30, 310), ("5", 140, 310), ("6", 250, 310), ("-", 360, 310),
        ("1", 30, 390), ("2", 140, 390), ("3", 250, 390), ("+", 360, 390),
        ("0", 30, 470), (".", 140, 470), ("=", 250, 470), ("C", 360, 470)
    ]

    for (text, x, y) in button_texts:
        if text == "=":
            button = ctk.CTkButton(frame, text=text, width=100, height=70, hover_color='hot pink', command=equals)
        elif text == "C":
            button = ctk.CTkButton(frame, text=text, width=100, height=70, hover_color='hot pink', command=clear_display)
        elif text == "←":
            button = ctk.CTkButton(frame, text=text, width=100, height=70, hover_color='hot pink', command=backspace)
        elif text in "!":
            button = ctk.CTkButton(frame, text=text, width=100, height=70, fg_color='seagreen', hover_color='hot pink', command=lambda t=text: update_entry(t)) 
        elif text== "^":
            button= ctk.CTkButton(frame, text= text, width= 100, height= 70, fg_color='seagreen',hover_color= 'hot pink', command=lambda t=text: update_entry(t)) 
    
        else:
            button = ctk.CTkButton(frame, text=text, width=100, height=70, fg_color='hot pink', hover_color='seagreen', command=lambda t=text: update_entry(t))
        button.place(x=x, y=y)
    
    root.mainloop()

calculator()


