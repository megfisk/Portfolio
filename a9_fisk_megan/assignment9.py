# ITP 115, Spring 2024
# Assignment 9
# Name: Megan Fisk
# Description: This program reads data from a csv file about computer languages and allows the user to select data
# they want to save to a file and write to a text file

# defining the createOptionslist function which creates a list containing the options of information for the user to
# choose from; with the filenameStr parameter being the file name with the default of "languages.csv"; return value is
# the header row of the csv file, showing the options for the user to choose from

def createOptionslist(filenameStr = "languages.csv"):
    fileIn = open(filenameStr, "r")
    headerLine = fileIn.readline().strip()
    headerRow = headerLine.split(",")
    fileIn.close()
    return headerRow

# defining the createDatalist function which creates a list of information depending on the user's input; optionsList
# parameter is the header row from the return of the createOptionslist function; choiceStr parameter is the user choice;
# filenameStr parameter is the name of the file; return value is a list with the requested piece of info for each
# language


def createDatalist(optionsList, choiceStr, filenameStr):
    dataList = []
    infoIndex = optionsList.index(choiceStr)
    fileIn = open(filenameStr, "r")
    fileIn.readline()
    for line in fileIn:
        line = line.strip().split(",")
        info = line[infoIndex]
        dataList.append(info)
    fileIn.close()
    return dataList

# defining the getUserChoice function which prompts the user for a valid choice; optionsList parameter is the list of
# options from the getOptionslist function; return value is the string of the user's choice, stripped


def getUserChoice(optionsList):
    userList = optionsList[2:]
    print("Available information about the languages include")
    print(userList)
    userChoice = input("Enter your choice:").strip().lower()
    while userChoice not in userList:
        print(userChoice, "is not a valid choice")
        userChoice = input("Enter your choice:").strip().lower()
    print("You have entered", userChoice)
    return userChoice


# defining the writeTextfile function, which creates a new .txt file and writes the requested information into it;
# langList parameter is the list of the titles of each language; infoList parameter is a list of the user requested
# information; choiceStr parameter is the user's choice from the getUserChoice function; no return value

def writeTextfile(langList, infoList, choiceStr):
    string = choiceStr + ".txt"
    stringIn = open(string, "w")
    print("language -> ", choiceStr, file = stringIn)
    for i in range(len(langList)):
       if infoList[i] != "NA":
           print(langList[i], "->", infoList[i], file = stringIn)
    stringIn.close()
    print("Information saved to", string)


# defining the main function; no parameters; it creates the optionsList, creates the langList using the createDatalist
# function, gets the user's choice using the getUserChoice function, creates the infoList using the createDatalist
# function and the user's choice, and creates a new .txt file using the writeTextfile function

def main():
    print("Computer languages")
    optionsList = createOptionslist("languages.csv")
    langList = createDatalist(optionsList, "title", "languages.csv")
    userChoice = getUserChoice(optionsList)
    infoList = createDatalist(optionsList, userChoice, "languages.csv")
    writeTextfile(langList, infoList, userChoice)

# calling the main function

main()


