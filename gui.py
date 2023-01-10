import tkinter as tk
import game_objects as obj
from functools import partial

game_mode = "RPSLS"

class GameApp(tk.Tk):

    def __init__(self):
        super().__init__()
        if game_mode == "RPSLS":
            self.object_set = obj.RPSLS_OBJECTS
        else:
            self.object_set = obj.RPS_OBJECTS
        self.configure(background="blue")
        self.game = obj.Game()
        self.title(" ".join([i for i in self.object_set]))
        self.playernum = 0
        self.title_text = tk.Label(self,
                                   text=" ".join([i for i in self.object_set]),
                                   font=("Arial", 12),
                                   background="blue")
        self.title_text.pack()

        self.show_frame("main_menu")

    def show_frame(self, current_frame):
        self.frames = {
            "main_menu": MainMenu(self),
            "action_chooser_1": ActionChooser(self, 1),
            "action_chooser_2": ActionChooser(self, 2),
            "round_results": RoundResults(self),
            "game_over": GameOver(self)
        }
        widgets = self.winfo_children()
        for widget in widgets:
            if widget.winfo_class() == "Frame":
                widget.pack_forget()
        frame_to_show = self.frames[current_frame]
        frame_to_show.pack(expand=True, fill=tk.BOTH)
        frame_to_show.set_up()


class MainMenu(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def set_up(self):
        self.controller.game.players = []
        self.round_num = tk.Label(self,
                                  text="Number of Rounds:",
                                  font=("Arial", 10),
                                  background="blue"
                                  )
        self.config(background="blue")
        self.round_input_box = tk.Entry(self,
                                        )

        self.play_label = tk.Label(self,
                                   text="Play!",
                                   font=("Arial", 20),
                                   compound="center",
                                   background="blue")

        self.comp_button = tk.Button(self,
                                     text="One Player",
                                     command=self.oneplayergame)
        self.player_button = tk.Button(self,
                                       text="Two Players",
                                       command=self.twoplayergame)

        self.place()

    def place(self):
        self.round_num.grid(row=0, column=0, padx=20, pady=10, sticky="nw")
        self.round_input_box.grid(row=1, column=0, sticky="nw", padx=20, pady=0)
        self.play_label.grid(row=2, column=0, columnspan=3, padx=50, pady=20)
        self.comp_button.grid(row=3, column=0, padx=10, pady=10)
        self.player_button.grid(row=3, column=2, padx=10, pady=10)

    def oneplayergame(self):
        self.controller.game.max_rounds = int(self.round_input_box.get())
        self.controller.playernum = 1
        self.controller.game.add_human_player("Player 1")
        self.controller.game.add_computer_player()
        self.controller.show_frame("action_chooser_1")

    def twoplayergame(self):
        self.controller.game.max_rounds = int(self.round_input_box.get())
        self.controller.playernum = 2
        self.controller.game.add_human_player("Player 1")
        self.controller.game.add_human_player("Player 2")
        self.controller.show_frame("action_chooser_1")


class ActionChooser(tk.Frame):

    def __init__(self, controller: GameApp, chooserplayer):
        super().__init__()
        self.chooserplayer = chooserplayer
        self.controller = controller

    def set_up(self):
        self.config(background="blue")
        self.playerlabel = tk.Label(self,
                                    text=f"Player {self.chooserplayer}:\n\tChoose your action",
                                    font=("Arial", 20),
                                    background="blue"
                                    )
        self.playerlabel.pack(side="left")
        for option in self.controller.object_set:
            self.button = tk.Button(self,
                                    text=option,
                                    command=partial(self.option_button, option, self.chooserplayer))
            self.button.pack(fill="x", padx=10, pady=20)

        self.roundlabel = tk.Label(self,
                                   text=f"Round {self.controller.game.current_round} of {self.controller.game.max_rounds}",
                                   background="blue")
        self.roundlabel.pack()

    def option_button(self, option, chooserplayer):

        if chooserplayer == 1 and self.controller.playernum == 2:
            self.controller.show_frame("action_chooser_2")
            self.controller.game.players[0].choose_object(option)
            self.controller.show_frame("action_chooser_2")

        elif chooserplayer == 2 and self.controller.playernum == 2:
            self.controller.game.players[1].choose_object(option)
            self.controller.game.find_winner()
            self.controller.show_frame("round_results")

        elif chooserplayer == 1 and self.controller.playernum == 1:
            self.controller.game.players[0].choose_object(option)
            self.controller.game.players[1].choose_object()
            self.controller.game.find_winner()
            self.controller.show_frame("round_results")


class RoundResults(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.config(background="blue")

    def set_up(self):
        self.p_one_label = tk.Label(self,
                                    text=f"{self.controller.game.players[0].name} chose:\n\n{self.controller.game.players[0].current_object.name}",
                                    padx=20,
                                    pady=10,
                                    background="blue")
        self.p_two_label = tk.Label(self,
                                    text=f"{self.controller.game.players[1].name} chose:\n\n{self.controller.game.players[1].current_object.name}",
                                    padx=20,
                                    pady=10,
                                    background="blue")
        if self.controller.game.round_winner:
            self.winner_label = tk.Label(self,
                                         text=f"{self.controller.game.round_winner.name} wins!",
                                         padx=10,
                                         pady=25,
                                         font=("Arial", 13),
                                         background="blue")
        else:
            self.winner_label = tk.Label(self,
                                         text="Round is a draw!",
                                         padx=10,
                                         pady=25,
                                         font=("Arial",13),
                                         background="blue")
        self.score_label = tk.Label(self,
                                    text=self.controller.game.report_score(),
                                    padx=10,
                                    pady=10,
                                    background="blue")
        self.advance_button = tk.Button(self,
                                        text="Advance",
                                        command=self.advance)
        self.place()

    def place(self):
        self.p_one_label.grid(row=0, column=0)
        self.p_two_label.grid(row=0, column=1)
        self.winner_label.grid(row=1, columnspan=2)
        self.score_label.grid(row=2, columnspan=2)
        self.advance_button.grid(row=3, columnspan=2)

    def advance(self):
        self.controller.report_game_string = self.controller.game.report_score()
        self.controller.game.next_round()
        if self.controller.game.is_finished():
            self.controller.show_frame("game_over")
        else:
            self.controller.show_frame("action_chooser_1")


class GameOver(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.config(background="blue")

    def set_up(self):
        self.game_over_label = tk.Label(self,
                                        text="Game Over!",
                                        font=("Arial", 20),
                                        padx=20,
                                        pady=20,
                                        background="blue")
        self.score_report = tk.Label(self,
                                     text=self.controller.report_game_string,
                                     padx=10,
                                     pady=10,
                                     background="blue")
        self.winner_report = tk.Label(self,
                                      text=self.controller.game.report_winner(),
                                      padx=10,
                                      pady=10,
                                      background="blue")
        self.play_again_button = tk.Button(self,
                                           text="Play again",
                                           command=self.play_again)
        self.exit_button = tk.Button(self,
                                     text="Exit",
                                     command=self.end)
        self.place()

    def place(self):
        self.game_over_label.grid(row=0, columnspan=2)
        self.score_report.grid(row=1, columnspan=2)
        self.winner_report.grid(row=2, columnspan=2)
        self.play_again_button.grid(row=3, column=0, padx=20)
        self.exit_button.grid(row=3, column=1, padx=20)

    def play_again(self):
        self.controller.game.reset()
        self.controller.game = obj.Game()
        self.controller.show_frame("main_menu")

    def end(self):
        self.controller.destroy()


gui = GameApp()
gui.mainloop()
