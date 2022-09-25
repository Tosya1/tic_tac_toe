from ui import *
from tkinter import *
from processing import *
from logger import *


def init():
    global players
    global player
    global marks
    global mark
    players = get_players()
    marks = ['X', 'O']
    player = toss_player(players)
    mark = toss_mark(marks)
    board = get_board()
    
    window = Tk()
    window['bg'] = '#AFEEEE'
    window.title('Крестики-нолики')
    window.columnconfigure(5, weight=1, minsize=75)
    window.rowconfigure(0, weight=1, minsize=50)
    draw_board(window, board)

    msg = Label(
    window,
    text=f'По результатам жеребьевки начинает {player} с {mark}',
    width=40,
    bg='#AFEEEE',
    fg='#191970',
    font=('Arial', 20),
    )
    msg.grid(column=5, row=0, rowspan=3)
    log(msg['text'])

    def handle_click(event):
        print(board)
        global mark
        global player
        if event.widget['text'] in marks:
            show_error('Ошибка!', 'Ячейка уже занята. Пожалуйста, выберите другую ячейку.')
        for i in board:
            for j in i:
                if j == int(event.widget['text']):
                    i[i.index(j)] = mark
        log(f'{player} поставил {mark} в ячейку {event.widget["text"]}')
        event.widget['text'] = mark
        if mark == 'X':
            event.widget['fg'] = 'green'
        else:
            event.widget['fg'] = 'red'
        if check_win(board) == True:
            show_info('Игра окончена', f'Победил {player}. Поздравляем!')
            log(f'{player} побеждает в игре.')
            if show_choice('Игра окончена', 'Начать новую игру?') == False:
                window.destroy()
            else:
                window.destroy()
                init()
        elif check_draw(board, marks) != True:
            show_info('Игра окончена', 'Ничья!')
            log('Игра закончилась вничью.')
            if show_choice('Игра окончена', 'Начать новую игру?') == False:
                window.destroy()
            else:
                window.destroy()
                init()
        player = players[players.index(player) -1]
        mark = marks[marks.index(mark) -1]
        msg.configure(text=f'{player}, Ваша очередь проставить {mark}')

    window.bind("<Button-1>", handle_click)
    window.mainloop()

