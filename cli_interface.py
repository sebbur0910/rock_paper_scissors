import game_objects as obj


class CLI_Interface():
    def __init__(self):
        self.game = obj.Game()

    def set_up(self):
        print("Rock Paper Scissors Lizard Spock!")
        num_players = 0
        while not (num_players == 1 or num_players == 2):
            num_players = int(input("How many players would you like to have?"))
            if num_players != 1 and num_players != 2:
                print("Must have either one or two players")
            else:
                self.game.add_human_player(input("Please enter the name of the first human player: "))
                if num_players == 2:
                    self.game.add_human_player(input("Please enter the name of the first human player: "))
                else:
                    self.game.add_computer_player()
        print(self.game.players)
        self.input_max_rounds()

    def input_max_rounds(self):
        self.game.set_max_rounds(int(input("What is the maximum number of rounds? ")))

    def get_choices(self):
        for player in self.game.players:
            if player.name != "Computer":
                chosen = input(f"{player.name} please choose 'rock', 'paper', 'scissors', 'lizard' or 'spock'").lower()
                if chosen not in obj.RPSLS_OBJECTS:
                    print("Invalid user choice")
                    chosen = input(f"{player.name} please choose 'rock', 'paper', 'scissors', 'lizard' or 'spock'").lower()
                else:
                    player.choose_object(chosen)
            else:
                player.choose_object()

    def run_game(self):
        while self.game.is_finished:
            self.get_choices()
            print(self.game.report_round())
            print(self.game.report_score())
        print("Game over")
        print(self.game.report_winner())

    def run_sequence(self):
        self.set_up()
        self.run_game()


if __name__ == "__main__":
    cli = CLI_Interface()
    cli.run_sequence()
