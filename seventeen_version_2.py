#!/usr/bin/env python3
# Seventeen version 1



# check no of marb player 1 should remove or calc next move
# player 2 plays
# record number of wins
# write output in another file
# read the input file
def read_input(filename):
    """ This function reads input from input file:i206_placein_input.txt, 
    which contains the number of marbles player 1 picks in every game.
    variables:
    games : list of each line from the input file.
    idx : variable used to select each game on each line
    """

    with open(filename, 'r') as f:
        games = f.readlines()
        for idx in range(len(games)):

            games[idx] = (games[idx].strip()).split(',')

        # print(games)
        return games


def player_1(total_count, game, game_num, idx, textp2):
    """ This function returns various values after player 1 has picked
    marbles according to the input file.

    parameters:
    total_count : Number of marbles remaining before player picks
    game: List of all game inputs from input file
    game_num: Element value from the list called game, which indicates
    game number being played
    idx: Retrieves the number of marbles player 1 needs to pick from the
    game list.
    textp2: (text part 2): This variable  is a list that holds the 
    middle part (i.e play sequence eg:1-1-2-2-3-3-2-2-1) of every line
    in output file. 
    eg: textp2 = '1', '1', '2', '2', '3', '3', '2', '2']

    return:
    last_person: This variable is a flag that holds the value of person
    who is currently playing.Later it is used to calculate who wins the game.
    """
    last_person = 'player 1'
     
    if int(game[game_num][idx]) > total_count:
        play_1 = total_count
        
    else:
        play_1 = int(game[game_num][idx])

    total_count = total_count - play_1

    # adds player 1 pickup values to middle text
    textp2.append(str(play_1))
    return play_1, total_count, last_person, textp2


def player_2(total_count, game, game_num, player_1, textp2):
    """This function calculates variables based on number of marbles 
    picked by player 2. Player 2's strategy is to pick up same number of 
    marbles as player 1

    parameter:
    Player_1: This variable holds the number of marbles picked up by 
    player 1 in the last try"""

    last_person = 'player 2'

    # Picks up remaing number of marbles incase number of marbles remaining 
    # are less than what player 1 picked up.
    if player_1 > total_count:
        play_2 = total_count      
    else:
        play_2 = player_1

    total_count = total_count - play_2
    # print(textp2)
    textp2.append(str(play_2))
    return play_2, total_count, last_person, textp2

def text(game_num, textp2, last_person):
    """ This function creates text for each line i.e for game played,
     in the output file. It basically joins 3 parts of the required 
     output line.
     """

    textpart1 = ("Game #{}. Play sequence: ".format(game_num + 1))
    # textpart2 joins all the tries from the list textp2 to convert it in 
    # the required format = 1-1-2-2-3-3-2-2-1
    textpart2 = "-".join(textp2)
    if last_person == 'player 1':
        textp3 = '. Winner: P2'
    else:
        textp3 = '. Winner: P1'
    # text_per_game : joins all 3 parts of the line and each line
    # to be printed in the output file is stored as an element in the list
    # text_per_game.
    text_per_game = textpart1 + textpart2 + textp3 + '\n'
    return text_per_game


def outputcontent(final_text, p1wins, p2wins):
    """This function will consolidate and write all lines to output file. """
    with open('i206_placein_output2_priyankapatki.txt','w') as f:
        no_of_games = len(final_text)
        for count in range(no_of_games):
            f.write(final_text[count])
        last_line = "Player 1 won {} times; Player 2 won {} times.\n".format(p1wins, repr(p2wins))
        f.write(last_line)




def seventeen_game():
    """This function controls the flow of the game. """

    final_text = []
    games = read_input('i206_placein_input.txt')
    # p2wins : no of wins by player 2
    # p1wins: no of wins by player 1
    p2wins = 0
    p1wins = 0

    # For loop for every game
    for game_num in range(len(games)):
        total_marb = 17
        textp2 = []
        # For loop for every player1 input from the input file for every game
        for playerinput in range(len(games[game_num])):
            play_1, total_marb, last_person, textp2 = player_1(total_marb, games, game_num, playerinput, textp2)
            # If total marbles are 0 , end the game
            if total_marb == 0:
                break
            else:
                play_2, total_marb, last_person, textp2 = player_2(total_marb, games, game_num, play_1,textp2)
                if total_marb == 0:
                    break
        # finding the number of wins per game
        if last_person =='player 1':  
            p2wins += 1  
        else:
            p1wins += 1

        text_per_game = text(game_num, textp2, last_person)

        final_text.append(text_per_game)

# writing output content to a file
    outputcontent(final_text, p1wins, p2wins)


def main():  # CALL YOUR FUNCTION BELOW
    # print("Let's play the game of Seventeen!")
    seventeen_game()

if __name__ == '__main__':
    main()