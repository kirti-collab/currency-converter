from currency_converter import CurrencyConverter
import tkinter as tk
c = CurrencyConverter()
# print(c.convert(12,"USD","INR"))

window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

def clicked():
    amount = int(entery1.get())
    cur1 = entery2.get()
    cur2 = entery3.get()
    data = c.convert(amount,cur1,cur2)
    label4 = tk.Label(window,text=data,font="Times 20 bold").place(x=200,y = 300)

label = tk.Label(window,text = "currency converter",font="Times 20 bold").place(x = 120,y = 40)

label1 = tk.Label(window,text = "enter amount here : ", font = "Times 16 bold ").place(x = 70,y = 100)
entery1 = tk.Entry(window)

label2 = tk.Label(window,text = "enter your currency here : ", font = "Times 16 bold ").place(x = 30,y = 150)
entery2 = tk.Entry(window)

label3 = tk.Label(window,text = "enter your desire currency : ", font = "Times 16 bold ").place(x = 20,y = 200)
entery3 = tk.Entry(window)

button = tk.Button(window,text = "click ",font = "Times 16 bold ",command=clicked).place(x = 220,y = 250)

entery1.place(x = 270,y=110)
entery2.place(x = 270,y=155)
entery3.place(x = 270,y=205)

window.mainloop()
