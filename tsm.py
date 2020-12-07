from team import Team
from player import Player
class TSM(Team):
    '''Team TSM class'''
    
    def intro(self):
        '''Introduces Team TSM player'''
        print("This is Team part of TSM")
        for player in self.players:
            player.intro()
