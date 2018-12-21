from tkinter import *
import os
import time
# from pygame import mixer

window = Tk()
window.title('encoding decoding')
window.geometry('700x400')

folder = os.path.dirname(os.path.abspath(__file__))
mainIcon = os.path.join(folder, 'safety-code.ico')
window.iconbitmap(mainIcon)

def binTostr():
    getVal = str(inp.get())
    getVal = getVal.split(' ')
    result = ''
    for i in getVal:
        result += chr(int(i, 2))
    output.insert(END, result)


textBtn = Button(window, text='text', command=binTostr)
textBtn.grid(row=0, column=1, padx=10, pady=5)

binBtn = Button(window, text='bin')
binBtn.grid(row=1, column=1, padx=0, pady=5)

decBtn = Button(window, text='dec')
decBtn.grid(row=2, column=1, padx=0, pady=5)

octBtn = Button(window, text='oct')
octBtn.grid(row=3, column=1, padx=0, pady=5)

hexBtn = Button(window, text='hex')
hexBtn.grid(row=4, column=1, padx=0, pady=5)

type = StringVar()
inp = Entry(window,textvariable=type, font=('verdana', 20))
inp.grid(row=0, column=2, padx=5, pady=10)

output = Text(height=4, width=25, font=('arial')) # show/text box
output.grid(row=0, column=3, padx=5, pady=10)


window.mainloop()

# str to binary
#------------------

# x = 'hello world'
# result = ' '.join(format(ord(i), 'b') for i in x)

#binary to str
#--------------

# str = "1101000 1100101 1101100 1101100 1101111 100000 1110111 1101111 1110010 1101100 1100100"
# str = str.split(' ')
# result = ''
# for i in str:
#     result += chr(int(i, 2))


# binary to decimal
#---------------------

# num = '01111110'
# result = int(num, 2)

# dec to bin
#---------------------

# num = 126
# result = "{0:b}".format(num)

# dec to hex
#--------------

# num = 115
# result = hex(num).split('x')[-1]

# print(result)    
