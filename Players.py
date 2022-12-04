from View import*
from Player import*

class Players:
    def __init__(self, view):
        self.view = view
        self.__players = []
        self.lbl = ''
        self.txt = ''
        self.get_players()

    def get_players(self):
        self.view.create_window()
        self.lbl = self.view.create_label(
            self.view.window, 
            MSG_PLR1_NAME, 
            BG_BASE, 
            FG, 
            FONT_SIZE, 
            0, 
            0, 
            MSG_PAD
            ) 
        self.lbl.grid(column=0, row=0) 
        self.txt = self.view.create_entry()
        self.txt.grid(column=1, row=0) 
        btn = self.view.create_button(BTN_TEXT, self.btn_click)
        btn.grid(column=2, row=0)
        self.view.window.mainloop()

    def btn_click(self):
        self.lbl['text'] = MSG_PLR2_NAME
        if self.txt.get() != '':
            player = Player(self.txt.get())
            self.players.append(player)
        else:
            View.show_error(ERR_MSG_EMPTY_NAME)
            if len(self.players) == 0:
                self.lbl['text'] = MSG_PLR1_NAME
        self.txt.delete(0, END)
        if len(self.players) == 2:
            self.view.window.destroy()

    @property
    def players (self):
        return self.__players

