"""Tkinter - модуль для создания оконныхи приложений"""
"""Примеры - paint, google, pycharm"""
from tkinter import *
root = Tk()
root.iconbitmap(default="pic/popo1.ico")
# icon = PhotoImage(file='pic/popo1.ico')
# root.iconphoto(False, icon)
root.title('Оконное приложение') # zagolovok
root.geometry("400x200") # 300 shirina 500 visota
root.minsize(200, 100)
root.maxsize(800, 640)
# root.attributes("-alpha", 0.1)
# root.attributes('-toolwindow', True)
button_1 = Button(root, text="Кнопка_1", fg='blue')
button_2 = Button(root, text="Кнопка_2", fg='red')
button_1.pack(side=BOTTOM)
button_2.pack(side=RIGHT)

root.mainloop()