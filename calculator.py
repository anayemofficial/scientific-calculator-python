import tkinter as tk
import math
import matplotlib.pyplot as plt
import numpy as np

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("MS-990 Graph Calculator")
root.geometry("520x720")
root.configure(bg="#0f172a")

expression = ""
memory = 0
last_answer = 0
mode = "DEG"

# ---------------- FUNCTIONS ----------------
def press(val):
    global expression
    expression += str(val)
    display.set(expression)


def clear():
    global expression
    expression = ""
    display.set("")


def back():
    global expression
    expression = expression[:-1]
    display.set(expression)


def calculate():
    global expression, last_answer
    try:
        exp = expression.replace("^", "**")
        result = eval(exp)
        last_answer = result
        display.set(str(result))
        expression = str(result)
    except:
        display.set("Error")
        expression = ""

# ---------------- GRAPH FUNCTION ----------------
def plot_graph():
    try:
        exp = expression.replace("^", "**")
        x = np.linspace(-10, 10, 400)
        y = eval(exp)
        plt.figure()
        plt.plot(x, y)
        plt.title(f"y = {expression}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.show()
    except Exception as e:
        display.set("Graph Error")

# ---------------- SCI ----------------
def apply(func):
    global expression
    try:
        x = float(expression)
        if mode == "DEG":
            x = math.radians(x)
        result = func(x)
        display.set(str(result))
        expression = str(result)
    except:
        display.set("Error")

# ---------------- MEMORY ----------------
def m_plus():
    global memory
    memory += float(display.get())


def m_minus():
    global memory
    memory -= float(display.get())


def m_recall():
    press(memory)


def m_clear():
    global memory
    memory = 0

# ---------------- DISPLAY ----------------
display = tk.StringVar()
entry = tk.Entry(root, textvariable=display, font=("Segoe UI", 24),
                 bg="#020617", fg="#38bdf8", bd=0, justify="right")
entry.pack(fill="both", ipadx=10, ipady=25, padx=10, pady=10)

# ---------------- FRAME ----------------
frame = tk.Frame(root, bg="#0f172a")
frame.pack(expand=True, fill="both")

for i in range(8):
    frame.rowconfigure(i, weight=1)
for j in range(6):
    frame.columnconfigure(j, weight=1)


def btn(t, cmd, r, c, bg="#1e293b"):
    tk.Button(frame, text=t, command=cmd,
              font=("Segoe UI", 11, "bold"),
              bg=bg, fg="white", relief="flat").grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

# ---------------- BUTTONS ----------------
btn("AC", clear, 0, 0, "#ef4444")
btn("⌫", back, 0, 1)
btn("(", lambda: press("("), 0, 2)
btn(")", lambda: press(")"), 0, 3)
btn("Ans", lambda: press(last_answer), 0, 4)
btn("GRAPH", plot_graph, 0, 5, "#22c55e")

btn("7", lambda: press("7"), 1, 0)
btn("8", lambda: press("8"), 1, 1)
btn("9", lambda: press("9"), 1, 2)
btn("/", lambda: press("/"), 1, 3)
btn("√", lambda: apply(math.sqrt), 1, 4)
btn("^", lambda: press("^"), 1, 5)

btn("4", lambda: press("4"), 2, 0)
btn("5", lambda: press("5"), 2, 1)
btn("6", lambda: press("6"), 2, 2)
btn("*", lambda: press("*"), 2, 3)
btn("sin", lambda: apply(math.sin), 2, 4)
btn("cos", lambda: apply(math.cos), 2, 5)

btn("1", lambda: press("1"), 3, 0)
btn("2", lambda: press("2"), 3, 1)
btn("3", lambda: press("3"), 3, 2)
btn("-", lambda: press("-"), 3, 3)
btn("tan", lambda: apply(math.tan), 3, 4)
btn("log", lambda: apply(math.log10), 3, 5)

btn("0", lambda: press("0"), 4, 0)
btn(".", lambda: press("."), 4, 1)
btn("+", lambda: press("+"), 4, 2)
btn("=", calculate, 4, 3, "#22c55e")
btn("ln", lambda: apply(math.log), 4, 4)
btn("%", lambda: press("/100"), 4, 5)

btn("π", lambda: press(str(math.pi)), 5, 0)
btn("e", lambda: press(str(math.e)), 5, 1)
btn("1/x", lambda: apply(lambda x: 1/x), 5, 2)
btn("|x|", lambda: apply(abs), 5, 3)
btn("exp", lambda: apply(math.exp), 5, 4)

btn("M+", m_plus, 6, 0)
btn("M-", m_minus, 6, 1)
btn("MR", m_recall, 6, 2)
btn("MC", m_clear, 6, 3)

root.mainloop()

"""
# MS-990 Graph Calculator

## NEW FEATURES
- Graph plotting (like Desmos)
- Scientific + memory functions

## Install dependencies
pip install matplotlib numpy

## Run
python calculator.py
"""
