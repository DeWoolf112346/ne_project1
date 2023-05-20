from tkinter import *
root = Tk()
root.geometry('100x200')
root.title("Графическое окно № 25")

# root.maxsize(100, 200)
# root.minsize(x, y)
# btn_1 = Button(text='Click me', activebackground='orange')
# btn_1.pack(expand=True)

label_1 = Label(text="hello", background='blue', foreground='red')
label_1.pack(expand=True)
label_2 = Label(text="hi", font=('Arial Black', 5), background='blue', fg="red")
label_2.pack()
label_2.place(x=100, y=50)

root.mainloop()