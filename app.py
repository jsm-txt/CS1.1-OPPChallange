class Player:
    """Creates a player class"""
    def __init__(self, name, main):
        self.name = name
        self.main = main


    def player_intruduction(self):
        """Player intruduction"""
        print(f"My name is {self.name} and I play as {self.main}")


if __name__ == "__main__":
    player = Player("pol", "jol")
    player.player_intruduction()