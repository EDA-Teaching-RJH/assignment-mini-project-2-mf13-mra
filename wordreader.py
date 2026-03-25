import re

#simple program that allows you to search, remove from or add words to a list conatining the 3000 most common words in the english language.


#with open("3000words.txt") as wordList:
#     for word in wordList 
#        print(word)


def main(): #main loop
    while True:
        choice = choiceSelector("Please select function:\n1)Read1\n2)Write\n3)Remove\n4)Exit\n", [1, 2, 3, 4])

        if choice == 1:
            read()
        elif choice == 4:
            print("Exiting program...")
            break
    return

            
def read():
    choice = choiceSelector("Please select function:\n1)Read starting with [letters(s)]\n2)Read ending with [letter(s)]\n3)Search for specific word\n", [1, 2])

    if choice == 1:
        letter = "^" + input("Please input starting letter (or number): ")
        print( wordReader(letter))


def choiceSelector(options : str, validSelections : list) -> int:
    while True:
        try:
            choice = int( input(options))
            if choice in validSelections:
                break
            else:
                print("Please input valid choice")
        except:
            print("Please input integer")
    return choice
        
    





main()