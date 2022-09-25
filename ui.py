from tkinter import *
from tkinter import messagebox  


def get_players():
    global window
    global lbl
    global txt
    global players
    players = []
    
    window = Tk()
    window['bg'] = '#AFEEEE'
    window.title('Крестики-нолики')
    lbl =Label(
    window,
    text='Игрок 1, введите свое имя: ',
    bg='#AFEEEE',
    fg='#191970',
    font=('Arial', 15)
    )
    lbl.grid(column=0, row=0) 
    txt = Entry(window, width=20, font=('Arial', 15))
    txt.grid(column=1, row=0) 
    btn = Button(
        window,
        text="OK",
        font=('Arial', 15),
        bg='#B0E0E6',
        fg='#191970',
        width=12,
        borderwidth=0,
        command=btn_click
    )
    btn.grid(column=2, row=0)
    window.mainloop()
    players = list(filter(lambda x: x != '', players))
    return players

def btn_click():
    i = 2
    while i in [2, 2]:
        lbl['text'] = f'Игрок {i}, введите свое имя: '
        print(txt.get())
        if txt.get() != '':
            players.append(txt.get())
            print(players)
        else:
            show_error('Ошибка!', f'Не указано имя игрока. Пожалуйста, введите свое имя: ')
            if len(players) == 0:
                lbl['text'] = f'Игрок 1, введите свое имя: '
        txt.delete(0, END)
        i +=1
    if len(players) == 2:
        window.destroy()

def draw_board(window, board):
    for i in range(3):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)
        for j in range(3):
            frame = Frame(
                master=window,
                relief=RAISED,
                width=75,
                height=75,
                bg='white'
            )
            frame.grid(row=i, column=j, padx=2, pady=2)
            label = Label(
                master=frame,
                text=f"{board[i][j]}", 
                font=('Arial', 45), 
                bg='white', 
                fg='white', 
                width=5, 
                height=2)
            label.pack(fill=BOTH, expand=True)

def show_error(title, msg):  
    messagebox.showerror(title, msg) 

def show_info(title, msg):  
    messagebox.showinfo(title, msg)  

def show_choice(title, msg):  
    res = messagebox.askyesnocancel(title, msg) 
    return res




