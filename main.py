import tkinter as tk
import shelve
from random import randint

HEIGHT = 700
WIDTH = 900
GREY = '#404040'
LIGHT_GREY = '#A4A4A4'
TITLE_TEXT = ('TimesNewRoman', 15)
LB_TEXT = ('TimesNewRoman', 20)
TB_TEXT = ('TimesNewRoman', 15)
BORDER = 10
X13 = 0.017
X23 = 0.351
X33 = 0.685


class User:
    def __init__(self, name, age, account):
        self.name = name
        self.age = age
        self.account = account
        self.id = randint(100000, 200000)

    def __str__(self):
        return 'Name: {}\nAge: {}\nAccount: {}\n\n'.format(
            self.name, self.age, self.account)


def prepare_listbox():
    textbox.config(state='normal')
    textbox.delete(0.0, 'end')
    return listbox.curselection()


def show_data():
    selected = prepare_listbox()
    for num in selected:
        name = listbox.get(num).split()[1]
        current = database[name]
        textbox.insert(0.0, current)
    textbox.config(state='disabled')


def transfer_money():
    money = entry.get()
    selected = prepare_listbox()
    '''
    Проблема - при выборе нескольких значений в листбоксе
    не учитывается их порядок. Т.е. программе все равно
    выберешь ли ты 1ю запись и 3ю или 3ю и 1ю. Надо фиксить.
    Код ниже не будет ни за что работать.
    '''
    message = None
    if type(money) is int:
        if len(selected) > 2:
            message = 'Too many users selected!\n'
        elif len(selected) < 2:
            message = 'Too few users selected!\n'
        else:
            pass
    else:
        message = 'You can only transfer an integer amount of money!\n'


root = tk.Tk()
root.geometry('{}x{}'.format(WIDTH, HEIGHT))

bg_image = tk.PhotoImage(file='background.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Titles

init_kwargs = {'master': root, 'bg': GREY, 'fg': 'white',
               'font': TITLE_TEXT}
place_kwargs = {'rely': 0.02, 'relwidth': 0.3, 'relheight': 0.1}

title1 = tk.Label(text='Список пользователей', **init_kwargs)
title1.place(relx=X13, **place_kwargs)
title2 = tk.Label(text='Информация о пользователе', **init_kwargs)
title2.place(relx=X23, **place_kwargs)
title3 = tk.Label(text='Возможные операции', **init_kwargs)
title3.place(relx=X33, **place_kwargs)

# Frames
init_kwargs = {'master': root, 'bg': GREY}
place_kwargs = {'rely': 0.15, 'relwidth': 0.3, 'relheight': 0.8}

frame1 = tk.Frame(**init_kwargs)
frame1.place(relx=X13, **place_kwargs)
frame2 = tk.Frame(**init_kwargs)
frame2.place(relx=X23, **place_kwargs)
frame3 = tk.Frame(**init_kwargs)
frame3.place(relx=X33, **place_kwargs)

# Guts

# Clients there are in database
with shelve.open('clients') as file:
    database = {}
    for user in file:
        database[user] = file[user]
listbox = tk.Listbox(frame1, bd=BORDER, bg=LIGHT_GREY, font=LB_TEXT,
                     selectmode='multiple')
scrollbar1 = tk.Scrollbar(listbox)
listbox.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox.yview)

for num, user in zip(range(len(database)), database):
    listbox.insert(num, '{}: {}'.format(num + 1, user))

scrollbar1.place(relx=0.95, relwidth=0.05, relheight=1)
listbox.place(relwidth=1, relheight=1)

# Info about selected clients
textbox = tk.Text(frame2, bd=BORDER, bg=LIGHT_GREY, font=TB_TEXT,
                  state='disabled')
scrollbar2 = tk.Scrollbar(textbox)
textbox.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=textbox.yview)
scrollbar2.place(relx=0.95, relwidth=0.05, relheight=1)
textbox.place(relwidth=1, relheight=1)

# Functions, the juice
init_kwargs = {'master': frame3, 'bg': LIGHT_GREY,
               'font': TITLE_TEXT, 'bd': BORDER}
place_kwargs = {'relx': 0.04, 'relheight': 0.1}

show = tk.Button(text='Show', command=show_data, **init_kwargs)
show.place(rely=0.02, relwidth=0.92, **place_kwargs)
transfer = tk.Button(text='Transfer', command=transfer_money,
                     **init_kwargs)
transfer.place(rely=0.14, relwidth=0.92, **place_kwargs)
money_label = tk.Label(text='Enter sum:', **init_kwargs)
money_label.place(rely=0.24, relwidth=0.4, **place_kwargs)
entry = tk.Entry(**init_kwargs)
entry.place(relx=0.44, rely=0.24, relwidth=0.52, relheight=0.1)

tk.mainloop()

if __name__ == '__main__':
    pass
