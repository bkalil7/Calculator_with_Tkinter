from tkinter import *;

window = Tk();

#Defining the size of the window, width = 312 and height = 324
window.geometry("400x330");

#Preventing the window from getting resized
window.resizable(0, 0);

#Window title
window.title("Calculator");

#Setting functions for the calculator

#1. Function to update the displayer whenever a button is clicked. Basically a button updater
def button_click(item):
    operations = ["/", "+", "-", "*", "**", "**2", "%", "**(1/2)"];
    global expression
    global result
    if expression == result and (item in operations):
        expression = expression + str(item)
        input_text.set(expression)
    elif expression == result and not (item in operations):
        expression = "";
        expression += str(item);
        input_text.set(expression);
    elif expression != result:
        expression = expression + str(item);
        input_text.set(expression);
    
#2. Function CLear to clear the calculator
def button_clear():
    global expression;
    expression = "";
    input_text.set(expression);
    
#3. Button equal '=' for showing the result of the expression typed
def button_equal():
    global expression;
    global result;
    result = str(eval(expression));
    input_text.set(result);
    expression = result;
    
#Defining the variables
expression = "";
input_text = StringVar();
result = "";
    
#Creating the frame for the calculator
input_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

#Inside the frame
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = '#eee', bd = 0, justify = RIGHT);
input_field.grid(row = 0, column = 0);
input_field.pack(ipady = 10)# 'ipady' is an internal padding to increase the height of input field

#Frame for the buttons below the input_frame
buttons_frame = Frame(window, width = 322, height = 272.5, bg = "grey");
buttons_frame.pack();

#Setting the buttons
#First row
percentage = Button(buttons_frame, text = "%", width = 10, height = 3, command = lambda: button_click("/100"), bg = 'black', fg = 'white').grid(row = 0, column = 0)
clear = Button(buttons_frame, text = "C", width = 10, height = 3, command = lambda: button_clear()).grid(row = 0, column = 1)
parenthesis1 = Button(buttons_frame, text = "(", width = 10, height = 3, command = lambda: button_click("(")).grid(row = 0, column = 2)
parenthesis2 = Button(buttons_frame, text = ")", width = 10, height = 3, command = lambda: button_click(")")).grid(row = 0, column = 3)
divide = Button(buttons_frame, text = "/", width = 10, height = 3, command = lambda: button_click("/"), bg = 'orange').grid(row = 0, column = 4)


#Second row
power2 = Button(buttons_frame, text = "**2", width = 10, height = 3, command = lambda: button_click("**2"), bg = "black", fg = "white").grid(row = 1, column = 0)
seven = Button(buttons_frame, text = "7", width = 10, height = 3, command = lambda: button_click("7")).grid(row = 1, column = 1)
eight = Button(buttons_frame, text = "8", width = 10, height = 3, command = lambda: button_click("8")).grid(row = 1, column = 2)
nine = Button(buttons_frame, text = "9", width = 10, height = 3, command = lambda: button_click("9")).grid(row = 1, column = 3)
multiply = Button(buttons_frame, text = "x", width = 10, height = 3, command = lambda: button_click("*"), bg = 'orange').grid(row = 1, column = 4)

#Third row
power = Button(buttons_frame, text = "**", width = 10, height = 3, command = lambda: button_click("**"), bg = 'black', fg = "white").grid(row = 2, column = 0)
four = Button(buttons_frame, text = "4", width = 10, height = 3, command = lambda: button_click("4")).grid(row = 2, column = 1)
five = Button(buttons_frame, text = "5", width = 10, height = 3, command = lambda: button_click("5")).grid(row = 2, column = 2)
six = Button(buttons_frame, text = "6", width = 10, height = 3, command = lambda: button_click("6")).grid(row = 2, column = 3)
subtract = Button(buttons_frame, text = "-", width = 10, height = 3, command = lambda: button_click("-"), bg = 'orange').grid(row = 2, column = 4)

#Fourth row
sqrt = Button(buttons_frame, text = "**1/2", width = 10, height = 3, command = lambda: button_click("**(1/2)"), bg = 'black', fg = "white").grid(row = 3, column = 0)
one = Button(buttons_frame, text = "1", width = 10, height = 3, command = lambda: button_click("1")).grid(row = 3, column = 1)
two = Button(buttons_frame, text = "2", width = 10, height = 3, command = lambda: button_click("2")).grid(row = 3, column = 2)
three = Button(buttons_frame, text = "3", width = 10, height = 3, command = lambda: button_click("3")).grid(row = 3, column = 3)
add = Button(buttons_frame, text = "+", width = 10, height = 3, command = lambda: button_click("+"), bg = 'orange').grid(row = 3, column = 4)

#Fifth row
root = Button(buttons_frame, text = "x**(1/y)", width = 10, height = 3, command = lambda: button_click("**(1/"), bg = 'black', fg = "white").grid(row = 4, column = 0)
zero = Button(buttons_frame, text = "0", width = 21, height = 3, command = lambda: button_click("0")).grid(row = 4, column = 1, columnspan = 2)
comma = Button(buttons_frame, text = ",", width = 10, height = 3, command = lambda: button_click(",")).grid(row = 4, column = 3)
equal = Button(buttons_frame, text = "=", width = 10, height = 3, command = lambda: button_equal(), bg = 'orange').grid(row = 4, column = 4)


window.mainloop()