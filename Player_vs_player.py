from View import *
from Board import *
from constants import *
from Player import *
from Players import *
from Logger import *

class Player_vs_player:
    def __init__(self, board, players, view):
        self.view = view
        self.board = board
        self.marks = [MARK_X, MARK_O]
        self.players = players
        self.player = ''
        self.msg = ''
        self.game_over = False

    def init(self):
        if len(self.players.players) != 2:
            self.view.window.destroy()
        else:
            self.player = Player.toss_player(self.players.players)
            self.player.mark = Player.toss_mark(self.marks)
            self.player.set_color(self.marks)
            self.players.players[self.players.players.index(
                self.player) - 1].mark = self.marks[self.marks.index(self.player.mark) - 1]
            self.players.players[self.players.players.index(
                self.player) - 1].set_color(self.marks)
            self.view.create_window()
            self.view.window.columnconfigure(
                5, weight=1, minsize=MSG_MIN_WIDTH)
            self.view.window.rowconfigure(0, weight=1, minsize=MSG_MIN_HEIGHT)
            self.draw_board()
            self.create_msg()
            self.show_statistic(0, 0, 5)
            self.show_statistic(1, 1, 5)
            self.view.window.bind("<Button-1>", self.handle_click)
            self.view.window.mainloop()

    def draw_board(self):
        for i in range(3):
            self.view.window.columnconfigure(
                i, weight=1, minsize=MSG_MIN_WIDTH)
            self.view.window.rowconfigure(i, weight=1, minsize=MSG_MIN_HEIGHT)
            for j in range(3):
                self.draw_cell(i, j)

    def draw_cell(self, i, j):
        frame = View.create_frame(self.view.window)
        frame.grid(row=i, column=j, padx=FRAME_PAD,
                pady=FRAME_PAD, sticky=NSEW)
        label = self.view.create_label(
            frame,
            f"{self.board.board[i][j]}",
            BG_BOARD,
            BG_BOARD,
            FONT_SIZE_CELL,
            CELL_WIDTH,
            CELL_HEIGHT,
            MSG_PAD
        )
        label.pack(fill=BOTH, expand=True)

    def create_msg(self):
        self.msg = self.view.create_label(
            self.view.window,
            MSG_START_GAME % (self.player.name, self.player.mark),
            BG_BASE,
            self.player.color,
            FONT_SIZE_COMMENT,
            0,
            0,
            MSG_PAD
        )
        self.msg.grid(column=5, row=0, rowspan=CELL_SPAN)
        Logger.log(self.msg['text'])

    def show_statistic(self, pl_index, col_index, raw_index):
        msg = self.view.create_label(
            self.view.window,
            MSG_STAT % (self.players.players[pl_index].name,
                    self.players.players[pl_index].wins, self.players.players[pl_index].losses),
            BG_BASE,
            self.players.players[pl_index].color,
            FONT_SIZE_COMMENT,
            0,
            0,
            MSG_PAD
        )
        msg.grid(column=col_index, row=raw_index, pady=MSG_STAT_PADY)

    def handle_click(self, event):
        if event.widget['text'] in self.marks:
            View.show_error(ERR_MSG_CHECKED_CELL)
        else:
            self.make_a_move(event)

    def make_a_move(self, event):
        for i in self.board.board:
            for j in i:
                if j == int(event.widget['text']):
                    i[i.index(j)] = self.player.mark
        Logger.log(LOG_MSG_MOVE %
                (self.player.name, self.player.mark, event.widget["text"]))
        event.widget['text'] = self.player.mark
        event.widget['fg'] = self.player.color
        self.check_end_game()

    def check_end_game(self):
        if self.board.check_win() == True:
            self.game_over = True
            self.player.add_win()
            self.players.players[self.players.players.index(
                self.player) - 1].add_loss()
            View.show_info(TITLE_GAME_OVER, MSG_VIN % (self.player.name))
            Logger.log(LOG_MSG_VIN % (self.player.name))
            if View.show_choice(TITLE_GAME_OVER, MSG_NEW_GAME) == False:
                self.view.window.destroy()
            else:
                self.view.window.destroy()
                self.__class__.init(self.__class__(
                    Board(), self.players, View()))
        elif self.board.check_draw(self.marks) != True:
            self.game_over = True
            self.player.add_draw()
            self.players.players[self.players.players.index(
                self.player) - 1].add_draw()
            View.show_info(TITLE_GAME_OVER, MSG_DRAW)
            Logger.log(MSG_DRAW)
            if View.show_choice(TITLE_GAME_OVER, MSG_NEW_GAME) == False:
                self.view.window.destroy()
            else:
                self.view.window.destroy()
                self.__class__.init(self.__class__(
                    Board(), self.players, View()))
        else:
            self.change_player()

    def change_player(self):
        self.player = self.players.players[self.players.players.index(
            self.player) - 1]
        self.msg.configure(text=MSG_MAKE_A_MOVE %
                (self.player.name, self.player.mark))
        self.msg.configure(fg=self.player.color)
