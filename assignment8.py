# ITP 115, Spring 2024
# Assignment 8
# Name: Megan Fisk
# Email: mafisk@usc.edu
# Section: 318249
# Description: allow the user to crack a computer generated code using new functions and list modifications

# import the random module
import random


# define the isSingleDigit(userStr) using if loops and .isdigit() and len(userStr)
def isSingleDigit(userStr):
    if userStr.isdigit() is True and len(userStr) == 1:
        return True
    elif userStr.isdigit() is False or len(userStr) != 1:
        return False


# define createCodeList(size using for loop and appending the empty list using random integers
def createCodeList(size):
    codeList = []
    for i in range(size):
        newValue = random.randint(0, 9)
        codeList.append(newValue)
    return codeList


# define the createUserList function that has the user to guess the code, creating a list to be compared to the codeList
def createUserList(size):
    print("The number of digits in the code is", size)
    userList = []
    for i in range(size):
        addValue = input("Enter a digit at index "+ str(i) + ":")
        while isSingleDigit(addValue) is False:
            addValue = input("Enter a digit at index:")
        addValue = int(addValue)
        userList.append(addValue)
    print("Your guess is", userList)
    return userList


# define the displayHints function, comparing the codeList and userList at each index using for and if loops
def displayHints(codeList, userList, size):
    print("Generating hints...")
    hintCount = 0
    for i in range(size):
        if codeList.count(userList[i]) > 0:
            hintCount += 1
            print(userList[i], "at index", i, "occurs", codeList.count(userList[i]), "time(s)")
        if userList[i] == codeList[i]:
            print(codeList[i], "at index", i, "is correct")
    if hintCount == 0:
        print("No correct digits")


# define the main function to allow the user to crack the code
def main():
    size = 3
    codeList = createCodeList(size)
    userList = createUserList(size)
    guessCount = 0
    while userList != codeList:
        displayHints(codeList, userList, size)
        guessCount += 1
        userList = createUserList(size)
    print("You cracked the code in", guessCount, "guesses!")


# calling the main function
main()






