from tkinter import *

win_lable_bool = True
win_canvas_bool = True
win_Button_bool = True

def get_Label():
    global win_label, win_lable_bool
    if win_lable_bool:
        win_label = Tk()
        win_label.title('Виджет Label')
        win_label.geometry('300x200')
        win_label.resizable(False, False)
        label_text = '''activebackground, activeforeground, anchor,
                background, bitmap, borderwidth, cursor,
                disabledforeground, font, foreground,
                highlightbackground, highlightcolor,
                highlightthickness, image, justify,
                padx, pady, relief, takefocus, text,
                textvariable, underline, wraplength
    
            WIDGET-SPECIFIC OPTIONS
    
                height, state, width'''
        label1 = Label(win_label, text=label_text)
        label1.pack()
    win_lable_bool = False

def get_Button():
    global win_button, win_Button_bool
    if win_Button_bool:
        win_button = Tk()
        win_button.title('Виджет Button')
        win_button.geometry('300x300')
        win_button.resizable(False, False)
        button_text = """Construct a button widget with the parent MASTER.
    
            STANDARD OPTIONS
    
                activebackground, activeforeground, anchor,
                background, bitmap, borderwidth, cursor,
                disabledforeground, font, foreground
                highlightbackground, highlightcolor,
                highlightthickness, image, justify,
                padx, pady, relief, repeatdelay,
                repeatinterval, takefocus, text,
                textvariable, underline, wraplength
    
            WIDGET-SPECIFIC OPTIONS
    
                command, compound, default, height,
                overrelief, state, width
            Widget.__init__(self, master, 'button', cnf, kw)"""
        button1 = Label(win_button, text=button_text)
        button1.pack()
    win_Button_bool = False
def get_Canvas():
    global win_canvas, win_canvas_bool
    if win_canvas_bool:
        win_canvas = Tk()
        win_canvas.title('Виджет Canvas')
        win_canvas.geometry('400x200')
        win_canvas.resizable(False, False)
        canvas_text = """Construct a canvas widget with the parent MASTER.
    
            Valid resource names: background, bd, bg, borderwidth, closeenough,
            confine, cursor, height, highlightbackground, highlightcolor,
            highlightthickness, insertbackground, insertborderwidth,
            insertofftime, insertontime, insertwidth, offset, relief,
            scrollregion, selectbackground, selectborderwidth, selectforeground,
            state, takefocus, width, xscrollcommand, xscrollincrement,
            yscrollcommand, yscrollincrement.
            Widget.__init__(self, master, 'canvas', cnf, kw)"""
        canvas1 = Label(win_canvas, text=canvas_text)
        canvas1.pack()
    win_canvas_bool = False

def get_destroy():
    global win_canvas_bool, win_lable_bool, win_Button_bool
    win_label.destroy()
    win_button.destroy()
    win_canvas.destroy()
    win_canvas_bool = True
    win_Button_bool = True
    win_lable_bool = True

root = Tk()
root.title('Основные виджеты')
root.geometry('500x500')
root.resizable(False, False)
btn1 = Button(root, text='Виджет Label', command=lambda:get_Label())
btn2 = Button(root, text='Виджет Button', command=lambda:get_Button())
btn3 = Button(root, text='Виджет Canvas', command=lambda:get_Canvas())
btn4 = Button(root, text='Закрыть все окна', command=lambda:get_destroy())
btn1.place(x=0, y=100)
btn2.place(x=0, y=200)
btn3.place(x=0, y=300)
btn4.place(x=0, y=400)

root.mainloop()