from datetime import datetime
from tkinter import *
from playsound import playsound
import threading
import sys

def wait_alarm():
    user_hours = hour_entry.get()
    user_minutues = minute_entry.get()

    while True:
        cur_hours = str(datetime.now().hour)
        cur_minute = str(datetime.now().minute)
        if user_hours == cur_hours and user_minutues == cur_minute:
            break
    playsound('sounds/1.mp3')
    print('Будильник сраболтал!')

def start_alarm():
    t = threading.Thread(target=wait_alarm)
    t.start()

def show_time():
    while True:
        cur_hours = str(datetime.now().hour)
        cur_minute = str(datetime.now().minute)
        cur_seconds = str(datetime.now().second)
        time_label.config(text=f"{cur_hours}:{cur_minute}:{cur_seconds}")

def show_time_th():
    th = threading.Thread(target=show_time)
    th.start()

run = True
root = Tk()
root.title('Будильник >:C')
root.geometry('300x300')
root.resizable(False, False)

c = Canvas(width=300, height=300, bg='blue')
c.pack()

alarm_label = Label(text='Введите время:', font=('CourierNew', 16), bg='blue', fg='red')
alarm_label.place(x=0, y=173)

hour_entry = Entry(width=5)
minute_entry = Entry(width=5)

hour_entry.place(x=185, y=180)
minute_entry.place(x=240, y=180)

time_label = Label(text='', font=('CourierNew', 20), fg='red', bg='blue')
time_label.place(x=110, y=100)

# label1 = Label(text=cur_hours, bg='blue', font=('CourierNew', 16), fg='red')
# label1.place(x=125, y=100)

# label2 = Label(text=':', bg='blue', font=('CourierNew', 16), fg='red')
# label2.place(x=150, y=100)

# label3 = Label(text=cur_minute, bg='blue', font=('CourierNew', 16), fg='red')
# label3.place(x=157, y=100)

btn_alarm = Button(text='Запустить', command=start_alarm)
btn_alarm.place(x=200, y=200)

c.create_window(100, 190, window=alarm_label)

if run == True:
    show_time_th()

root.mainloop()
sys.exit()
run = False



