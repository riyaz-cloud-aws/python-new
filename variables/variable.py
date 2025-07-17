#global_variables

line = "Python is awesome!"

def display():
    print("Inside function:", line)

def text():
    print("Outside function:", line)


display()
text()

#local_variables

def display():
    text = "python was awesome!"
    print("inner function:", text)
    
def fun():
    print("outer function:",text)
    
display()
fun()    

#->it throws error bcoz the value assigned in inner function