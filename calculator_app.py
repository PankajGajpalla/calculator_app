from tkinter import *

first_num = second_num = op = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clr():
    result_label.config(text='')

def operator(st):
    global first_num, op

    first_num = int(result_label['text'])
    op = st
    result_label.config(text='')

def equalto():
    global first_num, second_num, op

    second_num = int(result_label['text'])

    if(op == '+'):
        result_label.config(text=str(first_num + second_num)) 
    elif op == '-':
        result_label.config(text=str(first_num-second_num))
    elif op == '*':
        result_label.config(text=str(first_num*second_num))
    else:
        if second_num == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_num/second_num, 2)))

  

root = Tk()

root.title('Calculator')
root.iconbitmap('enstagam.ico')

root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')


# result 
result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0,columnspan=5, pady=(50, 25), sticky='e')
result_label.config(font=('vardana', 30, 'bold'))

# ---------- first row -------------------------------------------------- 
btn7 = Button(root, text='7', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('vardana', 14, 'bold'))

btn8 = Button(root, text='8', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(8))
btn8.grid(row=1, column=1)
btn8.config(font=('vardana', 14, 'bold'))

btn9 = Button(root, text='9', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(9))
btn9.grid(row=1, column=2)
btn9.config(font=('vardana', 14, 'bold'))

btn_add = Button(root, text='+', bg='#ffa500', fg='white', width=5, height=2, command=lambda: operator('+'))
btn_add.grid(row=1, column=3)
btn_add.config(font=('vardana', 14, 'bold'))

# ---------- second row -------------------------------------------------- 
btn4 = Button(root, text='4', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(4))
btn4.grid(row=2, column=0)
btn4.config(font=('vardana', 14, 'bold'))

btn5 = Button(root, text='5', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(5))
btn5.grid(row=2, column=1)
btn5.config(font=('vardana', 14, 'bold'))

btn6 = Button(root, text='6', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(6))
btn6.grid(row=2, column=2)
btn6.config(font=('vardana', 14, 'bold'))

btn_sub = Button(root, text='-', bg='#ffa500', fg='white', width=5, height=2, command=lambda: operator('-'))
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('vardana', 14, 'bold'))

# ---------- third row -------------------------------------------------- 
btn1 = Button(root, text='1', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(1))
btn1.grid(row=3, column=0)
btn1.config(font=('vardana', 14, 'bold'))

btn2 = Button(root, text='2', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('vardana', 14, 'bold'))

btn3 = Button(root, text='3', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(3))
btn3.grid(row=3, column=2)
btn3.config(font=('vardana', 14, 'bold'))

btn_mul = Button(root, text='*', bg='#ffa500', fg='white', width=5, height=2, command=lambda: operator('*'))
btn_mul.grid(row=3, column=3)
btn_mul.config(font=('vardana', 14, 'bold'))

# ---------- fourth row -------------------------------------------------- 
btn_clr = Button(root, text='C', bg='#ffa500', fg='white', width=5, height=2, command= clr)
btn_clr.grid(row=4, column=0)
btn_clr.config(font=('vardana', 14, 'bold'))

btn0 = Button(root, text='0', bg='#ffa500', fg='white', width=5, height=2, command=lambda: get_digit(0))
btn0.grid(row=4, column=1)
btn0.config(font=('vardana', 14, 'bold'))

btn_equal = Button(root, text='=', bg='#ffa500', fg='white', width=5, height=2, command= equalto)
btn_equal.grid(row=4, column=2)
btn_equal.config(font=('vardana', 14, 'bold'))

btn_div = Button(root, text='/', bg='#ffa500', fg='white', width=5, height=2, command=lambda: operator('/'))
btn_div.grid(row=4, column=3)
btn_div.config(font=('vardana', 14, 'bold'))


root.mainloop()
