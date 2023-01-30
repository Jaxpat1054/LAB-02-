def main():
    
    hockey_team = {

        'name' : 'maple leafs',
        'city' : 'toronto',
        'players' : [
            'matthews',
            'marner', 
            'nylander'
        ],
        'games' : [
           {
                'Oppponent' : 'Canadians', #hocket_team['games'][0]['opponents']
                'goals for' : 6,           #hocket_team['games'][0]['goals for']
                'goals against' : 2        #hocket_team['games'][0]['goals against']
           },
           {
                'Oppponent' : 'Senators', #hockey_teamop
                'goals for' : 2,
                'goals against' : 3
           }  
        ]

    }
    new_game = {
        'Oppponent' : 'Bruins',
        'goals for' : 8,
        'goals against' : 0
    }
    #add another game
    hockey_team['games'].append(new_game)
    print_team_info(hockey_team)
    add_players(hockey_team, {'giordane', 'railly', 'engvall'})
    print_team_info(hockey_team)
    print_opponents(hockey_team) 
    return

def print_opponents(team):
    #the maple leafs have played against the Canadians, Senators, Bruins
    print(f"The {team['name'].title()} have played against the ")
    #for i,game in enumerate (team['games']):
    #    if i< len(team{'games'}) - 1:
    #      print 
    #    print(game ['opponent'], end=', ')
    opponent = [g['opponent'] for g in team ['games']]
    print(', '.join{opponent}, end='.\n')
    return    

def add_players(team, new_players):
    team['players'].extend(new_players)
    team['players'].sort()
    for i,p in enumerate (team['players']):
        team['players'][i] = p.capitalize()



def print_team_info(team):
    team_name = team['name'].title()
    team_city = team['city'].capitalize()
    print(f'\nThe players on the {team_city} {team_name} are: ')
    for p in team['players']:
        print(f'-{p.capitalize()}')
        
if __name__ == "__main__":
    main()
