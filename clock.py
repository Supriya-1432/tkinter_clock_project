import tkinter as tk
from time import strftime
import tkcalendar as tkcal

root=tk.Tk()
root.title("Clock")

def time():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

def display_date():
    date=mycal.get_date()
    selected_date=tk.Label(root, font=("ds-digital",20) , background="black" , foreground="cyan",text=date)
    selected_date.pack()

label1 = tk.Label(root, font=("ds-digital",20) , background="black" , foreground="cyan",text="Current time:")
label1.pack(pady=20)
label = tk.Label(root, font=("ds-digital",20) , background="black" , foreground="cyan")
label.pack(pady=20)
time()
label2 = tk.Label(root, font=("ds-digital",20) , background="black" , foreground="cyan",text="Calendar:")
label2.pack(pady=20)
mycal=tkcal.Calendar(root,date_pattern='dd/mm/yyyy')
mycal.pack()
button=tk.Button(root,font=("ds-digital",15) ,text="Select date",command=display_date)
button.pack(pady=20)


root.mainloop()
