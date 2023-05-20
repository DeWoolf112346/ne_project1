from tkinter import *

def summa():
    if entry1.get() != '':
        res = entry1.get()
        res1 = entry2.get()
        result = int(res) + int(res1)
        label1['text'] = result

def raznost():
    if entry1.get() != '':
        res = entry1.get()
        res1 = entry2.get()
        result = int(res) - int(res1)
        label1['text'] = result

def proizvedenie():
    if entry1.get() != '':
        res = entry1.get()
        res1 = entry2.get()
        result = int(res) * int(res1)
        label1['text'] = result

root = Tk()
root.title('Виджет ENTRY')
root.geometry('500x500')
root.resizable(False, False)
entry1 = Entry(bg='purple',
               fg='red',
               justify='right',
               font=('TxFixedFont', 24))
entry1.pack()

label2 = Label(text='+     -      *', font=('TxFixedFont', 24))
label2.pack()

entry1.insert()


entry2 = Entry(bg='dark green',
               fg='red',
               justify='right',
               font=('TxFixedFont', 24))
entry2.pack()

summa_btn = Button(text='Сумма',
                   font=('TxFixedFont', 24),
                   command=summa)
summa_btn.pack()

raznost_btn = Button(text='Разность',
                   font=('TxFixedFont', 24),
                   command=raznost)
raznost_btn.pack()

proizvedenie_btn = Button(text='Произведение',
                   font=('TxFixedFont', 24),
                   command=proizvedenie)
proizvedenie_btn.pack()

label1 = Label(text='', font=('TxFixedFont', 50))
label1.pack()

root.mainloop()