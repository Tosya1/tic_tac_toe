from Players import*

class Players_bot(Players):
    def __init__(self, view):
        super().__init__(view)

    def btn_click(self):
        if self.txt.get() != '':
            player = Player(self.txt.get())
            self.players.append(player)
            player2 = Player(BOT_NAME)
            self.players.append(player2)
        else:
            View.show_error(ERR_MSG_EMPTY_NAME)
            if len(self.players) == 0:
                self.lbl['text'] = MSG_PLR1_NAME
        self.txt.delete(0, END)
        if len(self.players) == 2:
            self.view.window.destroy()



