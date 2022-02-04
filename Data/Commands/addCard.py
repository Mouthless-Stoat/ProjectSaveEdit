from Data.Library import commandsFunc, saveEditFunc, func, var
import Data.Commands.deck

name = "addCard"
alias = ["ac"]
description = "[card name] Add card to your deck using save edit"


def run(arg: list):
    act = commandsFunc.actToInt()
    addedCard = ""
    hasFindCard = False
    closeMatch = []
    try:
        arg[0]
    except:
        print("Error")
        return
        
    addedCard, hasFindCard, closeMatch = commandsFunc.findCard(arg[0])

    if not hasFindCard:
        print("Error can't find card")
        if len(closeMatch) > 0:
            print(f"Did you mean {closeMatch}")
        return

    saveFile = saveEditFunc.readSaveFile()

    deckStart, deckEnd = commandsFunc.findDeckStartEnd()

    deck = saveFile[deckStart:deckEnd]

    numCard, numCardLine = commandsFunc.findNumCard()
    tabNum = 4 * 5
    if act == 3:
        tabNum = 5 * 5

    saveEditFunc.editSaveLine(numCardLine, f'{(tabNum-4)*" "}"$rlength": {numCard+1},')

    newline = "\n"
    # [The old line without the new line symbol], \n [20 space(4 tabs)]"[addedCard]"
    saveEditFunc.editSaveLine(
        deckEnd - 1, f'{deck[-1][:-1]},{newline}{(tabNum)*" "}"{addedCard}"'
    )
    print("Card added")
    Data.Commands.deck.run([])
