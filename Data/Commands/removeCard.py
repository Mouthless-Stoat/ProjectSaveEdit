from Data.Library import func, commandsFunc, saveEditFunc, var
import Data.Commands.deck

name = "removeCard"
alias = ["rmc"]
description = "[Card name] Remove card from your current deck"


def run(arg: list):
    saveFile = saveEditFunc.readSaveFile()

    deckStart, deckEnd = commandsFunc.findDeckStartEnd()
    deck = saveFile[deckStart:deckEnd]

    for i in range(len(deck)):
        deck[i] = deck[i].strip().strip(",").replace("\n", "").replace('"', "")

    try:
        arg[0]
    except:
        print("Error")
        return
        
    cardToRemove, hasFindCard, closeMatch = commandsFunc.findCard(arg[0])

    if not hasFindCard or cardToRemove not in deck:
        print("Error can't find card")
        if len(closeMatch) > 0:
            print(f"Did you mean {closeMatch}")
        return

    numCard, numCardLine = commandsFunc.findNumCard()
    tabNum = 4 * 4
    if commandsFunc.actToInt() == 3:
        tabNum = 5 * 4

    saveEditFunc.editSaveLine(numCardLine, f'{tabNum*" "}"$rlength": {numCard-1},')

    removeCardLine = saveEditFunc.findSaveLineIndex(
        f'"{cardToRemove}"', commandsFunc.findActStart()
    )
    saveEditFunc.editSaveLine(removeCardLine, "", True)
    if removeCardLine == deckEnd - 1:
        saveEditFunc.editSaveLine(
            removeCardLine - 1, saveFile[removeCardLine - 1].strip("\n").strip(",")
        )
    print("Card removed")
    Data.Commands.deck.run([])