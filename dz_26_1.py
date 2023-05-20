from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Графическое окно № 25")

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

button_1 = Button(root, text="Абибус")

button_1.grid(row=0, column=0, sticky="NSEW")

root.mainloop()