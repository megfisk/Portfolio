# ITP 115, Spring 2023
# Final Project
# Name: Megan Fisk
# Email: mafisk@usc.edu
# Section: 31849
# Filename: helper.py
# Description: This file contains functions to help create individual puzzles from the file as well as obtain
# information about the words in the puzzle


# Function: createPuzzleList
# Parameter: filenameStr with a default value of connections_data.csv
# Return value: a list of dictionaries where each dictionary represents one puzzle
# This function reads the file and creates a list of dictionaries for use in other functions


def createPuzzleList(filenameStr = "connections_data.csv"):
    puzzle_list = []
    fileIn = open(filenameStr, "r")
    headerLine = fileIn.readline().strip().split(",")
    for line in fileIn:
        puzz_dict = {}
        data_list = line.strip().split(",")
        for i in range(len(headerLine)):
            puzz_dict[headerLine[i]] = data_list[i]
        puzzle_list.append(puzz_dict)
    fileIn.close()
    return puzzle_list

# Function: getPuzzleByNum
# Parameters: puzzle_list, the return value from the createPuzzleList function, and numStr
# Return value: puzzle_dict, a dictionary representing one puzzle based on the numStr parameter matching the "num" key
# This function obtains one puzzle dictionary from the list of dictionaries


def getPuzzleByNum(puzzle_list, numStr):
    for i in range(len(puzzle_list)):
        if puzzle_list[i]["num"] == numStr:
            puzzle_dict = puzzle_list[i]
            return puzzle_dict

# Function: getColor
# Parameters: puzzle_dict, the return value from the getPuzzleByNum function, and difficultyNum
# Return value: color, the color for each difficulty level in the puzzle
# This function obtains the color of each difficulty level in the puzzle using the difficultyNum parameter


def getColor(puzzle_dict, difficultyNum):
    color = str(puzzle_dict["color"+str(difficultyNum)])
    return color

# Function: getConnection
# Parameters: puzzle_dict, the return value from the getPuzzleByNum function, and difficultyNum
# Return value: connection, the connection value for each difficulty level in the puzzle
# This function obtains the connection value for each difficulty level in the puzzle using the difficultyNum parameter


def getConnection(puzzle_dict, difficultyNum):
    connection = str(puzzle_dict["connection"+str(difficultyNum)])
    return connection

# Function: getGroup
# Parameters: puzzle_dict, the return value from the getPuzzleByNum function, and difficultyNum
# Return value: group, a list of four words that belong in the same difficulty level of the puzzle
# This function creates a list of four words corresponding to their difficulty level to be used by other functions


def getGroup(puzzle_dict, difficultyNum):
    group = []
    for i in range(1,5):
        add_i = puzzle_dict["word"+str(difficultyNum)+str(i)]
        group.append(add_i)
    return group

# Function: getWordList
# Parameters: puzzle_dict, the return value from the getPuzzleByNum function, and foundGroupList
# Return value: wordList, a list of words (strings) that have not been found yet during game play
# This function creates a list of words that have not been found yet by the user while the game is played based on the
# values in the foundGroupList parameter

def getWordList(puzzle_dict, foundGroupList):
    wordList = []
    for i in range(1,5):
        if i not in foundGroupList:
            wordList = wordList + getGroup(puzzle_dict, i)
    return wordList

