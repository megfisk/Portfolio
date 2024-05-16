# ITP 115, Spring 2023
# Final Project
# Name: Megan Fisk
# Email: mafisk@usc.edu
# Section: 31849
# Filename: extra_credit.py
# Description: (you fill in)


def addPuzzle(puzzle_list):
    new_puzzle_q = input("Would you like to add a puzzle (Y or N)? ").upper().strip()
    while new_puzzle_q == "Y":
        new_puzzle_dict = {}
        number = input("Enter a starting number (over "+str(len(puzzle_list))+"):")
        date = input("Enter a date:")
        new_puzzle_dict["num"] = number
        new_puzzle_dict["date"] = date
        new_puzzle_dict["color1"] = "YELLOW"
        new_puzzle_dict["difficulty1"] = 1
        connect1 = input("Enter connection1:").upper().strip()
        new_puzzle_dict["connection1"] = connect1
        for i in range(1,5):
            word1 = input("Enter word1"+str(i)+":").upper().strip()
            new_puzzle_dict["word1"+str(i)+""] = word1
        new_puzzle_dict["color2"] = "GREEN"
        new_puzzle_dict["difficulty2"] = 2
        connect2 = input("Enter connection2:").upper().strip()
        new_puzzle_dict["connection2"] = connect2
        for i in range(1,5):
            word2 = input("Enter word2"+str(i)+":").upper().strip()
            new_puzzle_dict["word2" + str(i) + ""] = word2
        new_puzzle_dict["color3"] = "BLUE"
        new_puzzle_dict["difficulty3"] = 3
        connect3 = input("Enter connection3:").upper().strip()
        new_puzzle_dict["connection3"] = connect3
        for i in range(1,5):
            word3 = input("Enter word3" + str(i) + ":").upper().strip()
            new_puzzle_dict["word3" + str(i) + ""] = word3
        new_puzzle_dict["color4"] = "PURPLE"
        new_puzzle_dict["difficulty4"] = 4
        connect4 = input("Enter connection4:").upper().strip()
        new_puzzle_dict["connection4"] = connect4
        for i in range(1,5):
            word4 = input("Enter word4"+str(i)+":").upper().strip()
            new_puzzle_dict["word4"+str(i)+""] = word4
        puzzle_list.append(new_puzzle_dict)
        new_puzzle_q = input("Would you like to add another puzzle (Y or N)? ").upper().strip()



