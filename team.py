class Team:
    def __init__(self, name):
        self.name = name
        self.players = list()

    def view_all_heroes(self):
        '''Prints out all players.'''
        for player in self.players:
            print(player)
    
    def add_player(self, player):
        '''Adds player to player list'''
        self.players.append(player)
    
    def stats(self):
        '''Print team statistics'''
        for player in self.players:
            kd = player.kills / player.deaths
            print("{} Kill/Deaths:{}".format(player.name,kd))