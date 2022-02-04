from Data.Library import saveEditFunc, commandsFunc, var
name = "deck"
alias = ["d"]
description = "Show your deck"


def run(arg:list):
    saveFile = saveEditFunc.readSaveFile()

    # find the deck end and start
    deckStart, deckEnd = commandsFunc.findDeckStartEnd()

    # filter out stuff for listing the deck
    deck = saveFile[deckStart:deckEnd]
    for i in range(len(deck)):
        deck[i] = deck[i].strip().replace("\n", "").replace(",", "").replace('"', "")
    print(f"You {var.currentAct} deck: {deck}")

    # finding number of card
    numCard, numCardLine = commandsFunc.findNumCard()
    print(f"Number of card in your deck: {numCard}")
