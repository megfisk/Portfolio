# ITP 115, Spring 2023
# Final Project
# Name: Megan Fisk
# Email: mafisk@usc.edu
# Section: 31849
# Filename: interface.py
# Description: This file contains functions that interface with the user and help the main function of the game run

# imported the helper file and the pretty_print file

import helper
import pretty_print

# Function: displayRules
# Parameter: textfileStr, with a default value of "game_rules.txt"
# Return value: none
# This function reads the text file and prints each line, displaying the rules of the game to the user


def displayRules(textfileStr = "game_rules.txt"):
    file_Rules = open(textfileStr, "r")
    for line in file_Rules:
        line = line.strip()
        print(line)

# Function: isValidNumber
# Parameters: userStr, which is the number entered by the user in another function, startNum, and endNum
# Return value: a boolean value depending on the branching statement
# This function returns a boolean value depending on whether the userStr lies between the startNum and endNum


def isValidNumber(userStr, startNum, endNum):
    if userStr.isdigit() == True:
        if startNum <= int(userStr) <= endNum:
            return True
        else:
            return False
    else:
        return False

# Function: pickPuzzle
# Parameter: puzzle_list, a list of dictionaries where each dictionary represents one puzzle
# Return value: puzzle, which is a dictionary representing one puzzle
# This function prompts the user to enter a number, and if the number is within the correct values (checked by the
# isValidNumber function), then a single puzzle is obtained from the list using the getPuzzleByNum function from the
# helper file


def pickPuzzle(puzzle_list):
    endNum = len(puzzle_list)
    userChoice = input("Enter a puzzle number (1-"+str(len(puzzle_list))+"): ")
    while isValidNumber(userChoice, 1, endNum) == False:
        userChoice = input("Enter a puzzle number (1-" + str(len(puzzle_list)) + "): ")
    puzzle = helper.getPuzzleByNum(puzzle_list, userChoice)
    return puzzle

# Function: getGuessList
# Parameter: wordList, a list of words that have not been found by the user returned by the getWordList function in the
# helper file
# Return value: guess_list, a list of four words guessed by the user
# This function prompts the user for their four guesses and sorts them into a list if within the wordList and not in the
# guess_list already


def getGuessList(wordList):
    print("Enter four items for your guess")
    guess_list = []
    for i in range(1,5):
        guess = input("Item #"+ str(i) + ":")
        guess = guess.upper().strip()
        while guess not in wordList or guess in guess_list:
            guess = input("Item #" + str(i) + ":")
            guess = guess.upper().strip()
        guess_list.append(guess)
    guess_list.sort()
    return guess_list

# Function: checkConnection
# Parameters: puzzle_dict, a dictionary representing one puzzle, and guess_list, a list of the user's four guesses and
# the return value from the getGuessList function
# Return value: group_diff, the value of the group's difficulty based on the branching statement
# This function checks whether the user's guess_list matches any of the groups in the puzzle, and if it does, returns
# the value of the group's difficulty


def checkConnection(puzzle_dict, guess_list):
    group_diff = 0
    for i in range(1,5):
        group = helper.getGroup(puzzle_dict, i)
        if guess_list == group:
            group_diff += i
    return group_diff

# Function: playGame
# Parameter: puzzle_dict, a dictionary representing one puzzle
# Return value: a boolean value based on a branching statement
# This function allows the user to play the game using the displayGrid function from pretty_print, getWordList from
# helper, and getGuessList from interface within a while loop that runs while all the connections have not been found or
# the user has made less than four mistakes


def playGame(puzzle_dict):
    difficultyNum = []
    mistakes = 0
    while len(difficultyNum) < 4 and mistakes < 4:
        pretty_print.displayGrid(puzzle_dict, difficultyNum, mistakes)
        wordList = helper.getWordList(puzzle_dict, difficultyNum)
        guessList = getGuessList(wordList)
        check = checkConnection(puzzle_dict, guessList)
        if check != 0:
            difficultyNum.append(check)
        else:
            mistakes += 1
    pretty_print.displayGrid(puzzle_dict)
    if mistakes == 4:
        return False
    else:
        return True

# Function: savePuzzle
# Parameter: puzzle_dict, a dictionary representing one puzzle
# Return value: none
# This function saves the answers to the puzzle into a new text file with the help of the getColor, getConnection, and
# getGroup functions from the helper file


def savePuzzle(puzzle_dict):
    date = puzzle_dict["date"]
    date = date.strip().replace(" ", "")
    fileP = open(date+".txt", "w")
    for i in range (1,5):
        color = helper.getColor(puzzle_dict, i)
        connection = helper.getConnection(puzzle_dict, i)
        group = helper.getGroup(puzzle_dict, i)
        print(color+":", connection, group, file= fileP)
    print("Puzzle", puzzle_dict["num"], "has been saved to", date+".txt")

