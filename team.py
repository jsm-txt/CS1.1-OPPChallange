from player import Player
class Team:
    def __init__(self, name):
        self.name = name
        self.players = list()
        self.wins = 0
        self.losses = 0
        self.won = False

    def intro(self):
        '''Introduces team'''
        for player in self.players:
            player.intro()
    
    def add_player(self, player):
        '''Adds player to player list'''
        self.players.append(player)
    
    def stats(self):
        '''Print team statistics'''
        print(f"{self.name} has {self.wins} wins and {self.losses} losses.")
    

    def versus(self, opponent):
        '''Figure out who wins'''
        print(f"{self.name} versus {opponent.name}")
        while(True):
            self.won = False
            winner = input("Who is the winner? ")
            if winner == self.name:
                print(f"{self.name} won the match and advances")
                self.wins += 1
                opponent.losses +=1
                self.won = True
                break
                
            if winner == opponent.name:
                print(f"{opponent.name} won the match and advances")
                self.losses += 1
                opponent.wins +=1
                break