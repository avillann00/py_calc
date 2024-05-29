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
        return self.pop()
    def size(self):
        return len(self.stack)

# returns the operators precedence
def precedence(operator):
    if operator == "+" or "-":
        return 1
    if operator == "*" or "/":
        return 2

# does the mathematical calulations
def perform(operator, num_1, num_2):
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    else:
        return num_1 / num_2

# stack
stack = Stack()
# postfix equation
postfix = []

# opening statement and instructions
print("Hello, welcome to the calculator!")
print("If any letter is typed the program will quit.")

# start of the actual program
while 1:
    # takes input
    equation = input("Enter the equation: ")
    # changes the input to infix
    for i in equation:
        # if letter then break
        if i.isalpha(): 
            break
        # if its a digit add it right away
        if i.isdigit():
            postfix.append(i)
        # if its a space just ignore
        elif i.isspace():
            pass
        else:
            # push the open parenthses
            if i == "(":
                stack.push(i)
            # if closed parenthases, pop until the open one is reached
            elif i == ")":
                while stack.peek() != "(":
                    postfix.append(stack.pop())
                stack.pop()

            # if stack is empty of precedence is lower then push the operator
            if stack.is_empty() or precedence(stack.stack[-1]) < precedence(i):
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
        # push the digits immediately
        if int(i).isdigit():
            stack.push(i)
        # not a digit so perform operation
        else:
            num_2 = int(stack.pop())
            num_1 = int(stack.pop())
            stack.push(str(perform(i, num_1, num_2)))
    if stack.size > 1: 
        print("There was an error with your equation")
    else:
        print("The answer is " + str(stack.pop()))

print("Thank you, have a nice day!")
