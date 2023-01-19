from tkinter import *
window=Tk()

# add widgets here


window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interest():
    p=float(principle.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest= round(i,2)
    name=username.get()
    Showlabel.destroy()

calc_label=Label(window, text="Interest CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
calc_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

cal_button=Button(window, text="Click Here", fg="red", bg="black", bd=4, command=calculate_interest)
cal_button.place(x=130, y=260)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

Showlabel = LabelFrame(window,text="Your Result will be displayed here", bg = "lightcyan", font=("Calibri", 12))
Showlabel.pack(padx=20, pady=20)
Showlabel.place(x=20,y=300)

message=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
message.place(x=20,y=20)
message.pack()

window.mainloop()

