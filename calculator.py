# import the re modlule to help with parsing
import re

# class object for a stack
class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()
    def size(self):
        return len(self.stack)

# returns the operators precedence
def precedence(operator):
    if operator in ("-", "+"):
        return 1
    if operator in ("*", "/"):
        return 2
    else:
        return 0

# does the mathematical calulations
def perform(operator, num_1, num_2):
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    else:
        try:
            return num_1 / num_2
        except ZeroDivisionError:
            raise ZeroDivisionError("Not allowed to divide by 0")

def evaluate(expression):
    # stack
    stack = Stack()
    # postfix equation
    postfix = []

    # parses the equation
    expression = re.findall(r'(\d+|\+|\-|\*|\/|\(|\))',expression)

    # changes the input to infix
    for i in expression:
        # if its a digit add it right away
        if i.isdigit():
            postfix.append(i)
        # if its a space just ignore
        elif i.isspace():
            pass
        else:
            if i == "(":
                stack.push(i)
            # if closed parenthases, pop until the open one is reached
            elif i == ")":
                while stack.peek() != "(":
                    postfix.append(stack.pop())
                stack.pop()
            else:
                # if stack is empty of precedence is lower then push the operator
                if stack.is_empty() or precedence(stack.peek()) < precedence(i):
                    stack.push(i)
                # else pop the top operator and push the new one
                else:
                    postfix.append(stack.pop())
                    stack.push(i)
    # empty the stack
    while not stack.is_empty():
        postfix.append(stack.pop())

    # evaluate the postfix
    for i in postfix:
        # if it's an operator then perform the operation
        if i == "+" or i == "-" or i == "*" or i == "/":
            num_2 = int(stack.pop())
            num_1 = int(stack.pop())
            stack.push(str(perform(i, num_1, num_2)))   
        # is a digit so push it
        else:
            stack.push(int(i))
    postfix.clear()
    if stack.size() > 1: 
        while not stack.is_empty():
            stack.pop()
        print("There was an error with your equation")
        return -999999999999999
    else:
        return stack.pop()

# takes input
def start():
    while True:
        equation = input("Enter the equation: ")

        # if a stop keyword is entered is entered
        if equation.lower() == "quit" or equation.lower() == "stop" or equation.lower() == "break":
            break

        # if a letter is inputed then quit
        for i in equation:
            if i.isalpha():
                print("A letter was in the expression")
                break

<<<<<<< Updated upstream
        evaluate(equation)
<<<<<<< HEAD
=======
        print("The answer is " + str(evaluate(equation)))
=======
>>>>>>> main
def main():
    # opening statement and instructions
    print("Hello, welcome to the calculator!")
    print("If quit is entered the program will quit.")
    start()
    print("Thank you, have a nice day!")
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> main

if __name__ == "__main__":
    main()
