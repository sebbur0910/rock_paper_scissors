import tkinter as tk
import game_objects as obj

class GameApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Rock Paper Scissors Spock!")

        self.title_text = tk.Label(self,
                              text="Rock Paper Scissors Spock!",
                              width=40,
                              font=("Arial",20))

        self.interaction_frame = MainMenu()
        self.place_widgets()

    def place_widgets(self):
        self.title_text.pack()
        self.MainMenu.pack()

class MainMenu(tk.Frame):
    def __init__(self):
        super().__init__()

        self.trial_label = tk.Label(self,
                              text="Rock Paper Scissors Spock!",
                              width=40,
                              font=("Arial",20))

        self.place()

    def place(self):
        self.trial_label.pack()
class ActionChooser(tk.Frame):
    ...

class RoundResults(tk.Frame):
    ...

class GameOver(tk.Frame):
    ...

if __name__ == "__main__":
    gui = GameApp()
    gui.mainloop()
