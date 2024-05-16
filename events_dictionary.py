# ITP 115, Spring 2024
# Assignment 10
# Name: Megan Fisk
# Description: This program allows users to add, update, and delete events from an event dictionary


# defining the displayChoices() function, with no parameters, that displays the choices for the user to choose from

def displayChoices():
    print("Events Dictionary\nA) Add an event\nU) Update an event\nD) Delete an event\nP) Print the events\nQ) Quit")


# defining the displayEvents function, with the eventDict parameter that is our events dictionary; this will get all the
# keys from the dictionary into an alphabetical list and print each one with its corresponding date

def displayEvents(eventDict):
    keys = list(eventDict.keys())
    keys.sort()
    for i in keys:
        print(i, "occurs on", eventDict.get(i))

# defining the addEvent function, with the event dictionary as the parameter; this allows the user to enter an event and
# if it is not in the dictionary already, add it to the dictionary


def addEvent(eventDict):
    event = input("Enter an event:")
    event = event.title().strip()
    if event in eventDict:
        print(event, "is already in the events dictionary")
    else:
        date = input("Enter the date:")
        date = date.title().strip()
        eventDict[event] = date
        print(event, "has been added to the events dictionary")

# defining the updateEvent function, with the event dictionary as the parameter; this allows the user to update the date
# of an event if already in the dictionary


def updateEvent(eventsDict):
    event = input("Enter an event:")
    event = event.title().strip()
    if event not in eventsDict:
        print(event, "is not in the events dictionary")
    else:
        date = input("Enter the date:")
        date = date.title().strip()
        eventsDict[event] = date
        print(event, "has been updated to", date)

# defining the deleteEvent function, with the events dictionary as the parameter; this allows the user to delete an
# event from the dictionary


def deleteEvent(eventsDict):
    event = input("Enter an event:")
    event = event.title().strip()
    if event in eventsDict:
        eventsDict.pop(event)
        print(event, "was deleted from the events dictionary")
    else:
        print(event, "is not in the events dictionary")

# defining the main function with no parameters; create the events dictionary with our starting two events, display the
# choices to the user, allow them to choose a function, and perform the function to our events dictionary as long as
# their choice is not "Q"


def main():
    eventsDict = {"Memorial Day": "May 29, 2023", "Labor Day": "September 4, 2023"}
    displayChoices()
    userInput = input("Choice:").upper().strip()
    while userInput != "Q":
        if userInput == "A":
            addEvent(eventsDict)
        elif userInput == "U":
            updateEvent(eventsDict)
        elif userInput == "D":
            deleteEvent(eventsDict)
        elif userInput == "P":
            displayEvents(eventsDict)
        else:
            print("Invalid choice")
        displayChoices()
        userInput = input("Choice:").upper().strip()

# calling the main function

main()
