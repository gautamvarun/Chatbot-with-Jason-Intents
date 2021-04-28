from tkinter import*
from tkinter import messagebox
root = Tk()

root.title('DATA ANALUSIS')
root.geometry("400x400")

frame = LabelFrame(root,padx=5,pady=5,height=900,width=600)
frame.grid(row=1,column=1)

lable1 = Label(frame,text ="CHAT BOT",padx=3,pady=3)
lable1.grid(row=1,column=1)

frame2 = LabelFrame(root,padx=5,pady=5,height=900,width=600)
frame2.grid(row=2,column=1)


e=Entry(frame2,width=50,borderwidth=5,fg="grey")
e.grid(row=0,column=0,padx=5,pady=5)
a=e.get()

def popup():
    response = messagebox.showinfo("hii")   




button1 = Button(frame2,text="chat",padx=2,pady=2,command=popup)
button1.grid(row=1,column=0)

root.mainloop()