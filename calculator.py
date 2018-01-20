# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:04:44 2018

@author: samsung pc
"""

from tkinter import*
def btnClick(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)

        
def clear(x):
    global operator
    if x==1:
        operator = operator[:-1]
        text_Input.set(operator)
    else:
        operator = ''
        operatorDispl = ''
        text_Input.set(operatorDispl)
    
def equals(c):
    while c==1:
        global operator
        sum = str(eval(operator))
        text_Input.set(sum)
        operator=""

    
    
    

cal  = Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()

txtDisplay = Entry(cal,font=('Times New Roman', 20, 'bold'), textvariable=text_Input, bd=20, insertwidth=4, bg="sky blue", justify="right").grid(columnspan=4)
# PRVI RED DUGMICA
btn7 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(7), bg='sky blue', text='7', width=2).grid(row=1, column=0)
btn8 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(8), bg='sky blue', text='8', width=2).grid(row=1, column=1)
btn9 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(9), bg='sky blue', text='9', width=2).grid(row=1, column=2)
addition = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick('+'), bg='sky blue', text='+', width=2).grid(row=1, column=3)
# DRUGI RED DUGMICA
btn4 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(4), bg='sky blue', text='4', width=2).grid(row=2, column=0)
btn5 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(5), bg='sky blue', text='5', width=2).grid(row=2, column=1)
btn6 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(6), bg='sky blue', text='6', width=2).grid(row=2, column=2)
subtraction = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick('-'), bg='sky blue', text='-', width=2).grid(row=2, column=3)
# TRECI RED DUGMICA
btn1 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(1), bg='sky blue', text='1', width=2).grid(row=3, column=0)
btn2 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(2), bg='sky blue', text='2', width=2).grid(row=3, column=1)
btn3 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(3), bg='sky blue', text='3', width=2).grid(row=3, column=2)
multyplication = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16), command=lambda:btnClick('*'), bg='sky blue', text='x', width=2).grid(row=3, column=3)
# CETVRTI RED DUGMICA
btn0 = Button(cal, padx=16, pady=16, borderwidth=10, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick(0), bg='sky blue', text='  0  ', width=8).grid(columnspan=2, row=4)
btnDot = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick('.'), bg='sky blue', text=".", width=2).grid(row=4, column=2)
Division = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick('/'), bg='sky blue', text='/ ', width=2).grid(row=4, column=3)
# PETI RED DUGMICA
btn0 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:clear(0), bg='sky blue', text='C').grid(row=5, column=0)
btnClear = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16,), command=lambda:clear(1), bg='sky blue', text='←', width=2).grid(row=5, column=1)
btnEquals = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:equals(1), bg='sky blue', text="=").grid(row=5, column=2)
Square = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('Times New Roman', 16, 'bold'), command=lambda:btnClick('**2'), bg='sky blue', text='n²').grid(row=5, column=3)


cal.mainloop()