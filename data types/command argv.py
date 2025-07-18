import sys

def add():
    add = num1 + num2
    return add
def sub():
    sub = num1 - num2
    return sub
def mul():
    mul = num1 * num2 
    return mul
def div():
    div = num1 / num2
    return div

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = add()
    print(output)
    
if operation =="sub":
    output= sub()
    print(output)
    
if operation == "mul":
    output = mul()
    print(output)
    
if operation == "div":
    output = div()
    print(output)

