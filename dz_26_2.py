from tkinter import *
root = Tk()
root.geometry('400x400')
root.title("Графическое окно № 25")
l = 0
j = 0
k = 0
# root.maxsize(100, 200)
# root.minsize(x, y)
# btn_1 = Button(text='Click me', activebackground='orange')
# btn_1.pack(expand=True)
while l != 1:
    if k == 400:
        l = 1
    if j == 400:
        k = k + 10
        j = 0
    label_1 = Button(text="   ", background='blue', foreground='red')
    label_1.place(x=j, y=k)
    j = j + 10


root.mainloop()