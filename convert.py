from tkinter import *
import datetime

window = Tk ()
window.geometry ("500x500")
window.config(background ='blue')
window.title('conversion')

def dolar (x) :
    dol =x /0.708
    return dol

def dinar (y) :
    d = y/1.41
    return d

Label(window, text = "your conversion" )
c=Button (window, text = "convert to JOD", command = dinar)
c.pack()
b= Button (window, text = "convert to USD", command = dolar)
b.pack()
text = Entry (window,width = 100)
text.pack()
window.mainloop()


    
