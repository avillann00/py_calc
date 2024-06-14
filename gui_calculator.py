# import tkinter and calculator modules
from tkinter import *
from calculator import *

def clear():
    expression.set("")
    answer.set("")

# adds a character to the expression
def add(character):
    string = expression.get()
    string += character
    expression.set(string)

# calculates the answer
def enter():
    answer.set("")
    ans = "= "
    ans += str(evaluate(expression.get()))
    answer.set(ans)

# make the window and configure some settings
window = Tk()
window.geometry("400x400")
window.title("Calclulator")
icon = PhotoImage(file="calc.png")
window.iconphoto(True, icon)
window.config(background="white")

# the users expression
expression = StringVar()

# the expression answer
answer = StringVar()

# a frame to organize the input, beginning text, and the answer
words = Frame(window, bg="white", relief=SUNKEN, height=300, width=300)
words.pack(side=TOP)

# instructions
instructions = Label(words, text="Enter an expression then press equals", fg="black", bg="white")
instructions.grid(row=0, column=0)

# the expression
Label(words, textvariable=expression, fg="black", bg="white", bd=10, relief=RAISED).grid(row=1, column=0)

# the answer
Label(words, textvariable=answer, fg="black", bg="white", bd=10, relief=RAISED).grid(row=2, column=0)

# clear
Button(window, text="Clear", command=clear).pack(side=BOTTOM)

# submit
Button(window, text="=", command=enter).pack(side=BOTTOM)

# numbers
numbers = Frame(window,bg="white", relief=SUNKEN, height= 300, width=300)
Button(numbers, text="1", bg="white", command= lambda: add("1")).grid(row=0, column=0)
Button(numbers, text="2", bg="white", command= lambda: add("2")).grid(row=0, column=1)
Button(numbers, text="3", bg="white", command= lambda: add("3")).grid(row=0, column=2)
Button(numbers, text="4", bg="white", command= lambda: add("4")).grid(row=1, column=0)
Button(numbers, text="5", bg="white", command= lambda: add("5")).grid(row=1, column=1)
Button(numbers, text="6", bg="white", command= lambda: add("6")).grid(row=1, column=2)
Button(numbers, text="7", bg="white", command= lambda: add("7")).grid(row=2, column=0)
Button(numbers, text="8", bg="white", command= lambda: add("8")).grid(row=2, column=1)
Button(numbers, text="9", bg="white", command= lambda: add("9")).grid(row=2, column=2)
Button(numbers, text="0", bg="white", command= lambda: add("0")).grid(row=3, column=0, columnspan=3)
numbers.pack(side=BOTTOM)

# operators and parentheses
operators = Frame(window, bg="white", relief=SUNKEN, height=300, width=300)
Button(operators, text="+", bg="white", command= lambda: add("+")).grid(row=0, column=0)
Button(operators, text="-", bg="white", command= lambda: add("-")).grid(row=0, column=1)
Button(operators, text="x", bg="white", command= lambda: add("*")).grid(row=0, column=2)
Button(operators, text="/", bg="white", command= lambda: add("/")).grid(row=0, column=3)
Button(operators, text="(", bg="white", command= lambda: add("(")).grid(row=0, column=4)
Button(operators, text=")", bg="white", command= lambda: add(")")).grid(row=0, column=5)
operators.pack(side=BOTTOM)

# run the window
window.mainloop()
