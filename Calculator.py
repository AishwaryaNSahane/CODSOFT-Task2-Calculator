import tkinter as tk
import math

def on_click(btn_text):
    if btn_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    elif btn_text == "√":
        try:
            result = math.sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == "<-":
        entry.delete(len(entry.get())-1)
    else:
        entry.insert(tk.END, btn_text)

root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=20, font=("Helvetica", 20), bd=10, justify="right")
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ("C", "√", "/", "<-"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("!", "0", ".", "=")
]


for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = tk.Button(root, text=buttons[i][j], padx=15, pady=15, font=("Helvetica", 18), command=lambda text=buttons[i][j]: on_click(text))
        btn.grid(row=i+1, column=j)

root.mainloop()
