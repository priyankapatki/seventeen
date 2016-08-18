#!/usr/bin/env python3
# Seventeen version 1

def num_of_marbles(total_count):
    # Displays number of marbles left in jar
    if total_count > 0:
         print("Number of marbles left in jar: {}".format(total_count))

    return total_count


def player_1(total_count):

    # number of marbles player 1 removes
    last_person = 'player'
    play_1 = input("\nYour turn: How many marbles will you remove (1-3)? ")
    if total_count > 3:
        max_num_remove = 3
    else:
        max_num_remove = total_count
    if check_validity(play_1, total_count, max_num_remove) == 'check again':
        return player_1(total_count)

    else: 
        num_removed = check_validity(play_1, total_count, max_num_remove)
       
        print("You removed {} marbles.".format(num_removed))
        total_count  = total_count - num_removed
        total_count = num_of_marbles(total_count)
        # print("total = {}".format(total_count))
        # print("num = {}".format(num_removed))
        # print((total_count, num_removed))
        return (total_count, num_removed,last_person)



def check_validity(player1, total_count, max_remove):
    # check for validity of the  player input

    try:
        player1 = int(player1)
    except:
        print("Sorry, that is not a valid option. Try again!")# remove i
        # print(total_count)
        num_of_marbles(total_count)
        return 'check again'

    else:
        if player1 > max_remove or player1 <= 0:
            print("Sorry, that is not a valid option. Try again!")
            # print(total_count)
            num_of_marbles(total_count)
            return 'check again'
        else:
            return player1

def computer_player(play1_removed, total_count):
    # Since no specific strategy for computer was specified.
    # Strategy used was :number of marbles computer removes is the same
    # as user unless there are fewer marbles left in the jar, in that case
    # it just picks up 1.
    last_person = 'computer'
    print("\nComputer's turn...")
    if total_count >= play1_removed:
        comp_play = play1_removed
    else:
        comp_play = 1
    print("Computer removed {} marbles.".format(comp_play))
    total_count  = total_count - comp_play
    num_of_marbles(total_count)
    return total_count, last_person



def seventeen_game():
    """This function controls the game flow. """
    total_num = num_of_marbles(17)

    while total_num > 0 :
        total_num, play1, last_person = player_1(total_num)
        if total_num == 0:
            break

        total_num,last_person = computer_player(play1, total_num)
        if total_num == 0:
            break
    # deciding the winner
    if last_person == 'player':
        print("\nThere are no marbles left. Computer wins!")
    else:
        print("\nThere are no marbles left. Player wins!")



def main():  # CALL YOUR FUNCTION BELOW
    print("Let's play the game of Seventeen!")
    seventeen_game()

    

if __name__ == '__main__':
    main()