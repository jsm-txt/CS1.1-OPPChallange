class Team:
    def __init__(self, name):
        self.name = name
        self.players = list()
        self.wins = 0
        self.losses = 0
        self.won = False
    
    def add_player(self, player):
        '''Adds player to player list'''
        self.players.append(player)
    
    def stats(self):
        '''Print team statistics'''
        for player in self.players:
            kd = player.kills / player.deaths
            print("{} Kill/Deaths:{}".format(player.name,kd))
    

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