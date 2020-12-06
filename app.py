
class Player:
    '''Creates a player class'''
    def __init__(self, name):
        self.name = name
        self.main = str
        self.wins = 0
        self.losses = 0


    def player_intruduction(self):
        '''Player intruduction'''
        print(f"My name is {self.name} and I play as {self.main}")

    def player_stats(self):
        print(f" {self.name} has {self.wins} wins and {self.losses} loss.")

    def versus(self, opponent):
        '''Figure out who wins'''
        while(True):
            winner = input("Who is the winner? ")
            if winner == self.name:
                print(f"{self.name} won the match")
                self.wins += 1
                opponent.losses +=1
                break
            if winner == opponent.name:
                print(f"{opponent.name} won the match")
                self.losses += 1
                opponent.wins +=1
                break
        
        print("the match is over")
