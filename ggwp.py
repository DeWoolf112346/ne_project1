from tkinter import *
root = Tk()
# root.geometry('500x500')
root.title("Основное окно")

def information_Label():
    root = Tk()
    root.title("Информация о Label")
    f = Canvas(root, width=600, height=300, bg='red')
    root.minsize(width=600, height=300)
    root.maxsize(width=600, height=300)
    label2 = Label(root, text='''word = Lable(activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground,
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, takefocus, text,
            textvariable, underline, wraplength)''', fg='red')
    label2.place(x=150, y=100)
    root.mainloop()


c = Canvas(root, width=500, height=500, bg='green')
# c.create_polygon(200, 200, 250, 150, 300, 200, 300, 200, 200, 200, fill='red')
# c.create_rectangle(200, 200, 300, 300, fill='yellow')

btn1 = Button(text='Информация о Label', fg='red', command=lambda:information_Label())
c.create_window(75, 25, window=btn1, width=150, height=50)
c.pack(expand=True)
btn2 = Button(text='КРЫША', fg='red', command=lambda:c.create_polygon(200, 200, 250, 150, 300, 200, 300, 200, 200, 200, fill='red'))
c.create_window(75, 200, window=btn2, width=150, height=50)
btn3 = Button(text='ОСНОВАНИЕ', fg='red', command=lambda:c.create_rectangle(200, 200, 300, 300, fill='yellow'))
c.create_window(75, 250, window=btn3, width=150, height=50)
btn4 = Button(text='ОКНО', fg='red', command=lambda:c.create_rectangle(225, 225, 275, 275, fill='blue'))
c.create_window(75, 300, window=btn4, width=150, height=50)
root.mainloop()

# c.create_oval(400, 400, 500, 500, fill='orange')
# c.create_polygon(0, 200, 50, 250, 50, 300, fill='white')
# c.create_text(250, 250, text='hi', fill='black' )