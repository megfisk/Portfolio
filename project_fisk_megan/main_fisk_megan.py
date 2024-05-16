# ITP 115, Spring 2023
# Final Project
# Name: Megan Fisk
# Email: mafisk@usc.edu
# Section: 31849
# Filename: main_fisk_megan.py
# Description: This is the main function in which the program is run and the game is played

# import the helper, interface, and extra_credit files

import helper
import interface
import extra_credit

# Function: main
# Parameters: none
# Return value: none
# This function allows the user to play the game, first displaying the rules, then creating the puzzle_list, prompting
# the user to pick a puzzle, and calling the playGame function to run the game. If the game is won, a congratulatory
# message is printed. If lost, Better luck next time is printed. The puzzle is then saved to a new file named after the
# puzzle date.The user is then asked if they would like to add a puzzle to the list as a part of extra credit. If the
# user chooses yes, then the extra_credit function file is used to call the addPuzzle function, in which the user can
# add a puzzle of their own to the puzzle_list. Once added, the user is able to play again if they wish, with their
# new puzzle added to the puzzle options. The function is done when the user chooses that they would not like to play
# again


def main():
    print("Let's play Connections!\n")
    interface.displayRules()
    puzzleList = helper.createPuzzleList()
    puzzle_dict = interface.pickPuzzle(puzzleList)
    result = interface.playGame(puzzle_dict)
    if result is True:
        print("Congratulations!")
    else:
        print("Better luck next time.")
    interface.savePuzzle(puzzle_dict)

    # beginning of the extra credit code, with added branching in the main function to make the program run more
    # seamlessly (everything prior to this comment closely follows the directions of the Final Project instructions)

    extra_credit.addPuzzle(puzzleList)
    play_again = input("Would you like to play again (Y or N)?").upper().strip()
    if play_again == "Y":
        puzzle_dict = interface.pickPuzzle(puzzleList)
        result = interface.playGame(puzzle_dict)
        if result is True:
            print("Congratulations!")
        else:
            print("Better luck next time.")
        interface.savePuzzle(puzzle_dict)
        extra_credit.addPuzzle(puzzleList)
    elif play_again == "N":
        print("Thanks for playing!")


main()
