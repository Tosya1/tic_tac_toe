from Player_vs_player import *

class Player_vs_bot (Player_vs_player):
    def __init__(self, board, players, view):
        super().__init__(board, players, view)
        self.labels = []

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
        self.labels.append(label)
        label.pack(fill=BOTH, expand=True)

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
        if self.game_over == False:
            self.view.window.after(500, self.bot_move)

    def bot_move(self):
        move = self.bot_select_cell()
        for i in self.board.board:
            for j in i:
                if j == move:
                    i[i.index(j)] = self.player.mark
        Logger.log(LOG_MSG_MOVE % (self.player.name, self.player.mark, move))
        for i in range(len(self.labels)):
            if self.labels[i]['text'] == str(move):
                self.labels[i]['text'] = self.player.mark
                self.labels[i]['fg'] = self.player.color
        self.check_end_game()

    def bot_select_cell(self):
        li = [j for i in self.board.board for j in i]
        li = list(filter(lambda x: x not in self.marks, li))
        move = choice(list(set(li)))
        return move

    def change_player(self):
        self.player = self.players.players[self.players.players.index(
            self.player) - 1]
        if self.player.name == BOT_NAME:
            self.msg.configure(text=MSG_BOT_MOVE %
                        (self.player.name, self.player.mark))
        else:
            self.msg.configure(text=MSG_MAKE_A_MOVE %
                        (self.player.name, self.player.mark))
        self.msg.configure(fg=self.player.color)

    def create_msg(self):
        super().create_msg()
        if self.player.name == BOT_NAME:
            self.view.window.after(1000, self.bot_move)
