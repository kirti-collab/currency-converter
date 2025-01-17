import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfile,asksaveasfilename

root = tk.Tk()
root.title(" MY OWN NOTEPAD ! ")
root.rowconfigure(0,minsize=800) #gives val to the row 
root.columnconfigure(1,minsize=800)

text_edit = tk.Text(root)
frame_button = tk.Frame(root,relief=tk.RAISED,bd = 3)

button_open = tk.Button(frame_button,text=" open file ")
button_open.grid(row = 0,column=0,padx=5,pady=5)
button_save = tk.Button(frame_button,text=" save as  ")
button_save.grid(row=1,co)
root.mainloop()
