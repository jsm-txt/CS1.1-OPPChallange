
class Player:
    '''Creates a player class'''
    def __init__(self, name):
        self.name = name
        self.main = str
        self.wins = 0
        self.losses = 0
        self.won = False


    def player_intruduction(self):
        '''Player intruduction'''
        print(f"My name is {self.name} and I play as {self.main}")

    def player_stats(self):
        print(f" {self.name} has {self.wins} wins and {self.losses} loss.")

    def versus(self, opponent):
        '''Figure out who wins'''
        print(f"{self.name} versus {opponent.name}")
        while(True):
            
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

    