def generateDeck() -> list: #generates list with uno cards, every card is a seperate library.
    deck = []
    colours = ["yellow", "red", "blue", "green"]
    
    for colour in colours:
        for x in range(0, 10): #every deck is the same so hard coding isnt an issue as this will likely never see change.
            deck.append({"num" : x, "colour" : colour, "type" : "normal"})
            deck.append({"num" : x, "colour" : colour, "type" : "normal"}) #2 cards of each type so appending the same thing twice
        
        for x in range(0, 2):
            deck.append({"num" : "skip", "colour" : colour, "type" : "bully"}) #bully typing because these cards would have extra functions in a game
            deck.append({"num" : "+2", "colour" : colour, "type" : "bully"}) #bully means a +2 or +4 card
            deck.append({"num" : "turn", "colour" : colour, "type" : "bully"})
        
    for x in range(0, 4):
        deck.append({"num" : "colPick", "colour" : "black", "type" : "bully"})
        deck.append({"num" : "+4", "colour" : "black", "type" : "bully"})
    return deck

deck = generateDeck()

for card in deck:
    print(card["colour"] + " " + str( card["num"])) #neat way to show the list/library structure we just made


#made this before the module started and change it a bit to fulfill technical requirements mentioned on coversheet for libraries :D
