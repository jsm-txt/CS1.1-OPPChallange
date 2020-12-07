import random
import math
from team import Team
from app import Player
class Bracket:
    '''Creates a bracket class'''
    def __init__(self):
        self.num_players = 0
        self.player_list = list()
        self.next_round = list()
        self.rounds = 1
        self.team_list = list()

    def create_bracket(self):
        '''Asks the user what kind of match and how many players'''
        num_players = 0
        num_of_teams = 0
        num = None
        while num != "3":
            num = input("[1] Is two versus two? \n[2] One on one match? \n[3] Done? \n ")
            if num == "1":
                while num_of_teams < 2:
                    num_of_teams = int(input("How many teams in the tournament? "))
                    if num_of_teams < 2:
                        print("Enter a number higher than 2")
                self.num_of_teams = num_of_teams

                for i in range(num_of_teams):
                    team = self.create_team()
                    z=0
                    while z < 2:
                        player = self.create_player()
                        team.add_player(player)
                        z+=1
                    self.team_list.append(team)

                self.create_order(self.team_list)
                self.team_match()
                print("----------------------")
                for teams in self.team_list:
                    teams.stats()
                break 
               
            elif num == "2":
                while num_players < 2:
                    num_players = int(input("How many players in the tournament? "))
                    if num_players < 2:
                        print("Enter a number higher than 2")
                self.num_players = num_players
                for i in range(num_players):
                    player = self.create_player()
                    self.player_list.append(player)
                self.create_order(self.player_list)
                self.one_on_one()
                print("----------------------")
                for players in self.player_list:
                    players.stats()
                break
            elif num == "3":
                print("Done")
            else:
                print("Enter a proper value")

    def create_order(self,num_list):
        '''Creates bracket order from random'''
        x=0
        random.shuffle(num_list)
        for item in num_list:
            x+=1
            print(f"{item.name} is {x}")

    def team_match(self):
        '''Puts a team against another team'''
        i = 1
        length_round = math.ceil(len(self.team_list)/2)
        team_list = self.team_list

        while i <= length_round:
            if i != 1:
                team_list = self.next_round[:]
                self.next_round.clear()

            if len(team_list) % 2 != 0:
                self.next_round.append(team_list[len(team_list)-1])
            
            x = 0
            print(f"Starting round {self.rounds}")

            while x < (len(team_list)-1):
                team1 = team_list[x]
                team2 = team_list[x+1]
                team1.versus(team2)
                x+=2
                if team1.won == True:
                    self.next_round.append(team1)
                else:
                    self.next_round.append(team2)
            if i != length_round:
                print(f"Round {self.rounds} is over")
                self.rounds +=1
                print("Teams moving on:")
                for team in self.next_round:
                    print(team.name)
            else:
                print(f"Final round is over")
                team = self.next_round[0]
                player1 = team.players[0]
                player2 = team.players[1]
                print(f"Team {team.name} is the winner!!!")
                print(f"Players {player1.name} and {player2.name} have won!")
            i+=1
        
    def one_on_one(self):
        '''Puts a player agaisnt another player'''
        
        i = 1
        length_round = math.ceil(len(self.player_list)/2)
        player_list = self.player_list

        while i <= length_round:
            if i != 1:
                player_list = self.next_round[:]
                self.next_round.clear()

            if len(player_list) % 2 != 0:
                self.next_round.append(player_list[len(player_list)-1])
            
            x = 0
            print(f"Starting round {self.rounds}")

            while x < (len(player_list)-1):
                player1 = player_list[x]
                player2 = player_list[x+1]
                player1.versus(player2)
                x+=2
                if player1.won == True:
                    self.next_round.append(player1)
                else:
                    self.next_round.append(player2)
            if i != length_round:
                print(f"Round {self.rounds} is over")
                self.rounds +=1
                print("Players moving on:")
                self.print_player(self.next_round)
                
            else:
                print(f"Final round is over")
                self.print_player(self.next_round)
                print(" is the winner!!!")
            i+=1

    def print_player(self, player_list):
            for player in player_list:
                print(player.name)
                
    def create_team(self):
        '''Prompt user for team'''
        team_name = input("Team's name: ")
        team = Team(team_name)
        x=0
        while x > 2:
            player = self.create_player()
            team.add_player(player)
            x+=1
        return team

    def create_player(self):
        '''Prompt user for player'''
        player_name = input("Player's name: ")
        player = Player(player_name)
        return player

if __name__ == "__main__":
    run = True
    response = "Yes"
    while run == True:
        if response == "No" or response == "no":
            run = False
        elif response == "Yes" or response == "no":
            bracket = Bracket()
            bracket.create_bracket()
            bracket.num_players = 0
            bracket.player_list.clear
            bracket.next_round.clear
            bracket.rounds = 1
            bracket.team_list.clear
        else:
            print("Try Again")

        response = input("Create a new bracket? (Yes/No): ")    






