from tkinter import *                       #importing the module tkinter

#function to save the string in variable
def press(number):
    global op                                       #global declaring the variable
    op = op + str(number)
    text_Input.set(op)

#function to evaluate the result and display it
def result():
   #try, except used because incase used give invalid input then display will show error message
   
    try:

        global op

        total = str(eval(op))

        text_Input.set(total)

        op = total


    except:

        text_Input.set(" Error ")
        op = ""
#function to clear the display

def clear():
    global op
    op = ""
    text_Input.set("")

#main body to make user GUI
master = Tk()
master.title("Atul's Calculator")                                       #giving title name to my calcculator
op = ""
text_Input = StringVar()                                                #making string class
txtDisplay = Entry(master, font=('arial', 20), textvariable=text_Input, bd=20, insertwidth=4, bg="light blue").grid(            #User GUI Display formation(Entry is used)
    columnspan=4)

button7 = Button(master, padx=12, bd=8, pady=12, bg="black", fg="white", font=('arial', 20, 'bold'), text="7",      #making buttons using Bi=utton widget and styling them
                 command=lambda: press(7)).grid(row=1, column=0)

button8 = Button(master, padx=12, bd=8, pady=12, bg="black", text="8", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press(8)).grid(row=1, column=1)

button9 = Button(master, padx=12, bd=8, pady=12, bg="black", text="9", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press(9)).grid(row=1, column=2)

div = Button(master, padx=12, bd=8, pady=12, bg="black", text="/", fg="white", font=('arial', 20, 'bold'),
             command=lambda: press("/")).grid(row=1, column=3)


button4 = Button(master, padx=12, bd=8, pady=12, bg="black", text="4", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press(4)).grid(row=2, column=0)

button5 = Button(master, padx=12, bd=8, pady=12, bg="black", text="5", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press(5)).grid(row=2, column=1)

button6 = Button(master, padx=12, bd=8, pady=12, bg="black", text="6", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press(6)).grid(row=2, column=2)

buttonproduct = Button(master, padx=12, bd=8, pady=12, bg="black", text="*", fg="white", font=('arial', 20, 'bold'),
                       command=lambda: press("*")).grid(row=2, column=3)


button1 = Button(master, padx=12, bd=8, pady=12, bg="black", text="1", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press(1)).grid(row=3, column=0)

button2 = Button(master, padx=12, bd=8, pady=12, bg="black", text="2", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press(2)).grid(row=3, column=1)

button3 = Button(master, padx=12, bd=8, pady=12, bg="black", text="3", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press(3)).grid(row=3, column=2)

buttonsub = Button(master, padx=12, bd=8, pady=12, bg="black", text="-", fg="white", font=('arial', 20, 'bold'),
                   command=lambda: press("-")).grid(row=3, column=3)


button0 = Button(master, padx=10, bd=8, pady=12, bg="black", text="0", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press(0)).grid(row=4, column=0)

buttonc = Button(master, padx=10, bd=8, pady=12, bg="black", text="C", fg="white", font=('arial', 20, 'bold'),
                 command=lambda:clear()).grid(row=4, column=1)

buttonans = Button(master, padx=11, bd=8, pady=12, bg="black", text="=", fg="white", font=('arial', 20, 'bold'),
                   command=lambda:result()).grid(row=4, column=2)

buttonadd = Button(master, padx=8, bd=8, pady=12, bg="black", text="+", fg="white", font=('arial', 20, 'bold'),
                   command=lambda: press("+")).grid(row=4, column=3)
bracket = Button(master, padx=15, bd=8, pady=12, bg="black", text="(", fg="white", font=('arial', 20, 'bold'),
             command=lambda: press("(")).grid(row=5, column=0)
bracket1 = Button(master, padx=15, bd=8, pady=12, bg="black", text=")", fg="white", font=('arial', 20, 'bold'),
             command=lambda: press(")")).grid(row=5, column=1)

percent = Button(master, padx=15, bd=8, pady=12, bg="black", text=".", fg="white", font=('arial', 20, 'bold'),
             command=lambda: press(".")).grid(row=5, column=2)
button00 = Button(master, padx=2, bd=8, pady=12, bg="black", text="00", fg="white", font=('arial', 20, 'bold'),
                 command=lambda: press("00")).grid(row=5, column=3)
master.mainloop()           #mainloop
