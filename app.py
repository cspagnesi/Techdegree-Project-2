import constants
import copy

teams_list = copy.deepcopy(constants.TEAMS)
players_list = copy.deepcopy(constants.PLAYERS)
num_players = (len(players_list))
num_teams = (len(teams_list))
experience_yes = []
experience_no = []
player_guardians = []

def clean_data():
        for player in players_list:
                if player["experience"] == "YES":
                        player["experience"] = True
                        experience_yes.append(player)
                elif player["experience"] == "NO":
                        player["experience"] = False
                        experience_no.append(player)
                height = player["height"].split()
                player["height"] = int(height[0])
                player["guardians"] = (','.join(player["guardians"].split(" and")))
       
                                                
               
def balance_teams():
        teams_list[0] = (experience_no[0:3]) + (experience_yes[0:3])
        teams_list[1] = (experience_no[3:6]) + (experience_yes[3:6])
        teams_list[2] = (experience_no[6:9]) + (experience_yes[6:9])
        
def menu_interface():
        while True:
                print ("\nBASKETBALL TEAM STATS TOOL\n")
                print ("----MENU----\n")
                print ("Here are your choices:")
                print ("A: Display Team Stats")
                print ("B: Quit\n")
                stats_or_quit = input("Please enter an option.\n")
                stats_or_quit = stats_or_quit.upper()
                if stats_or_quit == "A":
                        print ("\nA: Panthers")
                        print ("B: Bandits")
                        print ("C: Warriors")  
                        pick_team = input("\nEnter an option:\n")
                        pick_team = pick_team.upper()
                        
                        if pick_team == ("A"):
                                roster_length = ("\nTotal players: {}\n".format(int(len(teams_list[0]))))
                                panther_players = []
                                player_heights = []
                                guardians = []
                                experienced_players = []
                                non_experienced_players = []  
                                print (str("\nTeam: Panthers Stats\n"))
                                print ("------------------\n")
                                print (roster_length)
                                for player in teams_list[0]:
                                        panther_players.append(player["name"])
                                        player_heights.append(player["height"])
                                        guardians.append(player["guardians"])
                                        if player in experience_yes:
                                                experienced_players.append(player)
                                        if player in experience_no:
                                                non_experienced_players.append(player) 
                                average_height = sum(player_heights) / len(teams_list[0])
                                guardians = (", ".join(guardians))
                                panther_players = ", ".join(panther_players)
                                average_height = round(average_height)   
                                print ("Roster: {}.".format(panther_players))
                                print ("Average Player Height: {} inches".format(average_height))
                                print ("Guardians: {}".format((guardians)))
                                print ("Experienced players: {}".format(len(experienced_players)))
                                print ("Non-Experienced players: {}".format(len(non_experienced_players)))
                                forward = input("\nPlease type enter 'Y' to continue or 'N' to quit.\n")
                                forward = forward.upper()
                                if forward == "Y":
                                        continue
                                elif forward == "N":
                                        print ("Thanks for using the 'Basketball Stats App'.  Bye now.")
                                        break  
                                else: 
                                        print ("\n\nThat is not a valid value.  Please try again.")
                                        continue
                                
                        elif pick_team == ("B"):
                                roster_length = ("\nTotal players: {}\n".format(int(len(teams_list[1]))))
                                bandit_players = []
                                player_heights = []
                                guardians = []
                                experienced_players = []
                                non_experienced_players = [] 
                                print (str("\nBandits Stats\n"))
                                print ("------------------")
                                print (roster_length)
                                for player in teams_list[1]:
                                        bandit_players.append(player["name"])
                                        player_heights.append(player["height"])
                                        guardians.append(player["guardians"])
                                        if player in experience_yes:
                                                experienced_players.append(player)
                                        if player in experience_no:
                                                non_experienced_players.append(player) 
                                average_height = sum(player_heights) / len(teams_list[1])
                                average_height = round(average_height) 
                                bandit_players = (", ".join(bandit_players))
                                guardians = (", ".join(guardians))
                                print ("Roster: {}".format(bandit_players))
                                print ("Average Player Height: {} inches".format(average_height))
                                print ("Guardians: {}".format(guardians))
                                print ("Experienced players: {}".format(len(experienced_players)))
                                print ("Non-Experienced players: {}".format(len(non_experienced_players)))
                                forward = input("\nPlease type enter 'Y' to continue or 'N' to quit.\n")
                                forward = forward.upper()
                                if forward == "Y":
                                        continue
                                elif forward == "N":
                                        print ("Thanks for using the 'Basketball Stats App'.  Bye now.")
                                        break  
                                else: 
                                        print ("\n\nThat is not a valid value.  Please try again.\n\n")
                                        continue
                                
                        elif pick_team == ("C"):
                                roster_length = ("\nTotal players: {}\n".format(int(len(teams_list[2]))))
                                warriors_players = []
                                player_heights = []
                                guardians = []
                                experienced_players = []
                                non_experienced_players = [] 
                                print (str("\nWarriors Stats\n"))
                                print ("------------------\n")
                                print (roster_length)
                                for player in teams_list[2]:
                                        warriors_players.append(player["name"])
                                        player_heights.append(player["height"])
                                        guardians.append(player["guardians"])
                                        if player in experience_yes:
                                                experienced_players.append(player)
                                        if player in experience_no:
                                                non_experienced_players.append(player) 
                                average_height = sum(player_heights) / len(teams_list[2])
                                average_height = round(average_height)  
                                warriors_players = (", ".join(warriors_players))
                                guardians = (", ".join(guardians))
                                print ("Roster: {}".format(warriors_players))  
                                print ("Average Player Height: {} inches".format(average_height)) 
                                print ("Guardians: {}".format(guardians))
                                print ("Experienced players: {}".format(len(experienced_players)))
                                print ("Non-Experienced players: {}".format(len(non_experienced_players)))
                                forward = input("\nPlease type enter 'Y' to continue or 'N' to quit.\n")
                                forward = forward.upper()
                                if forward == "Y":
                                        continue
                                elif forward == "N":
                                        print ("Thanks for using the 'Basketball Stats App'.  Bye now.")
                                        break  
                                else: 
                                        print ("\n\nThat is not a valid value.  Please try again.\n\n")
                                        continue
                        else:
                                print("\n\n\nThat is not a valid response.  Please try again.\n\n")
                                continue             

                elif stats_or_quit == "B":
                        print("Okay, goodbye.")
                        break
                else:
                        print ("\n\n\nSorry, that's not a valid response.  Please try again.\n\n")
                        continue
                        
if __name__ == "__main__":
        clean_data()
        balance_teams()
        menu_interface()

else:
    "This is not the main directory."
