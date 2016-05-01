"""A game of life. Modeled after the game
Real Lives."""

def main():

    """Main function initiate and run game"""

    print("Welcome to Thrive. Enjoy your stay.")
    input("Press ENTER to continue: ")

    a = GameState()
    print(a.return_age())
    print(a.is_game_over())

class GameState:
    
    """Class to store game variables, run life,
    and end game"""

    def __init__(self):
        self.age = 0
        self.game_over = False

    def return_age(self):
        return self.age

    def is_game_over(self):
        return self.game_over

if __name__ == "__main__":   
    main()

