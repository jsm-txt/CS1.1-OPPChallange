from team import Team
from app import Player
class bracket:
    """Creates a bracket class"""
    def __init__(self, num_players):
        self.num_players = num_players
    
    def create_bracket(self, num_players):
        pass



if __name__ == "__main__":
    player = Player("pol", "jol")
    player2 = Player("polu" , "steel")

    player.versus(player2)

