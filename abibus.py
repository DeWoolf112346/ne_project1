from tkinter import *
root = Tk()
root.geometry('500x300')
root.title("abibus")
label_1 = Label(text="kak rulit?", font=('Arial Black', 30), background='blue', fg="red")
label_1.pack()
btn_1 = Button(text='Click me', activebackground='orange')
btn_1.pack(expand=True)
label_2 = Label(text="Привет, пупсик!!!", font=('Arial Black', 30), background='blue', fg="red")
label_2.pack()
label_2.place(x=400, y=400)

label_3 = Label(text="Не тута", font=('Arial Black', 30), background='blue', fg="red")
label_3.pack()
label_3.place(x=500, y=0)

root.mainloop()