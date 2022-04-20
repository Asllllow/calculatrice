from tkinter import *
def add_calculator(symbole):
    global calculation
    calculation += str(symbole)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluation_calc():
    global calculation
    try:
        calculation= str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_calculator()
        text_result.insert(1.0, "Error")

def clear_calculator():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

 

window = Tk()
window.title("calculatrice")
window.geometry("330x350")
window.config(background="#41B77F")
calculation = ""

text_result = Text(window, height=2, width=16, font=("comicsans", 24))
text_result.grid(columnspan=5) 
btn1 = Button(window, text=1, command=lambda: add_calculator(1), width=5)
btn1.grid(row = 1, column = 0, ipady = 10 , ipadx = 10)

btn2 = Button(window, text=2, command=lambda: add_calculator(2), width=5)
btn2.grid(row = 1, column = 1, ipady = 10 , ipadx = 10)

btn3 = Button(window, text=3,command=lambda: add_calculator(3), width=5)
btn3.grid(row = 1, column = 2, ipady = 10 , ipadx = 10)

btn4 = Button(window, text=4, command=lambda:add_calculator(4), width=5)
btn4.grid(row=2, column=0, ipady=10, ipadx=10)

btn5 = Button(window, text=5, command=lambda:add_calculator(5), width=5)
btn5.grid(row=2, column=1, ipady=10, ipadx=10)

btn6 = Button(window, text=6, command=lambda:add_calculator(6))
btn6.grid(row=2, column=2, ipady=10, ipadx=25)

btn7 = Button(window, text=7, command=lambda:add_calculator(7), width=5)
btn7.grid(row=3, column=0, ipady=10, ipadx=10)

btn8 = Button(window, text=8, command=lambda:add_calculator(8), width=5)
btn8.grid(row=3,column=1, ipady=10, ipadx=10) 

btn9 = Button(window, text=9, command=lambda:add_calculator(9), width=5)
btn9.grid(row=3, column=2, ipady=10, ipadx=10)

btnpar = Button(window, text="(", command=lambda:add_calculator("("))
btnpar.grid(row=4,column=0, ipady=10, ipadx=25)

btnpar2 = Button(window, text=")", command=lambda:add_calculator(")"))
btnpar2.grid(row=4, column=2, ipady=10, ipadx=25)

btn0 = Button(window, text=0, command=lambda:add_calculator(0), width=5)
btn0.grid(row=4, column=1, ipady=10, ipadx=10)

btclear = Button(window, text="c", command=clear_calculator)
btclear.grid(row=5, column=1, ipady=10, ipadx=22)

btplus = Button(window, text="+", command=lambda:add_calculator("+"), width=5)
btplus.grid(row=1, column=3, ipady=10, ipadx=10)

btmoins = Button(window, text="-", command=lambda:add_calculator("-"), width=5)
btmoins.grid(row=2, column=3, ipady=10, ipadx=10)

btfois = Button(window, text="X", command=lambda:add_calculator("*"), width=5)
btfois.grid(row=3, column=3, ipady=10, ipadx=10)

btdiviser = Button(window, text="/", command=lambda:add_calculator("/"), width=5)
btdiviser.grid(row=4, column=3, ipady=10, ipadx=10)

btegal = Button(window, text="=", command=evaluation_calc)
btegal.grid(row=5, column=2, ipady=10, ipadx=22)



window.mainloop()




  