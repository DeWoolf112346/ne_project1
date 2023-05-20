from tkinter import *

def clear():
    entry1.delete(0, END)
def entry_1():
    entry1.insert(0, '1')
def get_text():
    txt = entry1.get()
    label1['text'] = txt
def grt_result():
    if entry1.get() != '':
        res = entry1.get()
        n = 0
        n2 = 0
        s = 0
        for r in res:
            n += 1
            if r == '+':
                s = res[0:n-1]
                n2 = n - 1
        s2 = res[n2:n]
        print(s)
        print(s2)
        result = int(s) + int(s2[1::])
        print(result)
        label1['text'] = result
root = Tk()
root.title('Виджет ENTRY')
root.geometry('500x500')
root.resizable(False, False)
entry1 = Entry(bg='red',
               fg='blue',
               justify='right',
               font=('TxFixedFont', 24))
entry1.pack()
# ins_str = 'Имя пользователя'
# entry1.insert(0, ins_str)
btn_delete = Button(text="Стереть",
                    command=clear)
btn_delete.pack()
btn_1 = Button(text='1',
               command=entry_1)
btn_1.pack()
btn_get = Button(text='Получить текст',
                 command=get_text)
btn_get.pack()
label1 = Label(text='')
label1.pack()
btn_result = Button(text='=',
                    command=grt_result)
btn_result.pack()

root.mainloop()