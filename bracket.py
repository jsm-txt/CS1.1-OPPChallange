import random
from team import Team
from app import Player
class Bracket:
    '''Creates a bracket class'''
    def __init__(self):
        self.num_players = 0
        self.player_list = list()

    def create_bracket(self):
        '''Asks the user what kind of match and how many players'''
        num_players = 0
        num = None
        while num != "3":
            num = input("[1] Is two versus two? \n[2] One on one match? \n[3] Done? \n ")
            if num == "1":
                pass
               
            elif num == "2":
                while num_players < 2:
                    num_players = int(input("How many players in the tournament? "))
                    if num_players < 2:
                        print("Enter a number higher than 2")
                for i in range(num_players):
                    player = self.create_player()
                    self.player_list.append(player)
                    self.num_players = num_players
                break
            else:
                print("Enter a proper value")
        
    def create_order(self):
        '''Creates bracket order from random'''
        x=0
        random.shuffle(self.player_list)
        for player in self.player_list:
            x+=1
            print(f"Player {x} is {player.name}")

    
    def print_player(self):
        for player in self.player_list:
            print(player.name)

    def team_match(self):
        pass

    def one_on_one(self):
        """Puts a player agaisnt another player"""


        player1 = self.player_list[0]
        player2 = self.player_list[1]
        player1.versus(player2)

    def create_player(self):
        """Prompt user for player info"""
        player_name = input("Player's name: ")
        player = Player(player_name)
        return player

if __name__ == "__main__":
    # player = Player("pol", "jol")
    # player2 = Player("polu" , "steel")

    # player.versus(player2)

    bracket = Bracket()
    bracket.create_bracket()
    bracket.create_order()




