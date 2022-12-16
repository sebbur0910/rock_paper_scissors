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

        self.place_widgets()

        self.frames = {
            "main_menu": MainMenu(self),
            "action_chooser": ActionChooser(self),
            "round_results": RoundResults(self),
            "game_over": GameOver(self)
        }
        self.show_frame("main_menu")

    def show_frame(self, current_frame):
        widgets = self.winfo_children()
        for widget in widgets:
            if widget.winfo_class() == "Frame":
                widget.pack_forget()
        frame_to_show = self.frames[current_frame]
        frame_to_show.pack(expand=True, fill=tk.BOTH, anchor="center")


    def place_widgets(self):
        self.title_text.pack()
      #  self.MainMenu.pack()

class MainMenu(tk.Frame):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.round_num = tk.Label(self,
                              text="Number of Rounds:",
                              font=("Arial",10))
        self.config(background="blue")
        self.round_input_box = tk.Entry(self,
                                        )

        self.play_label = tk.Label(self,
                                   text="Play!",
                                   font=("Arial", 20),
                                   compound="center")

        self.place()

    def place(self):
        self.round_num.grid(row=0, column=0, sticky="nw", padx=20, pady=10)
        self.round_input_box.grid(row=1, column=0, sticky="nw", padx=20, pady=0)
        self.play_label.grid(row=1, column=1, sticky="e")
class ActionChooser(tk.Frame):
    ...

class RoundResults(tk.Frame):
    ...

class GameOver(tk.Frame):
    ...

if __name__ == "__main__":
    gui = GameApp()
    gui.mainloop()
