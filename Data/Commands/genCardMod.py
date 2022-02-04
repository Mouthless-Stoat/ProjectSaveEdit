from Data.Library import saveEditFunc, commandsFunc, func, var

name = "genCardMod"
alias = ["gencm", ""]
description = '[card name] Generate a "$v" for a card in your deck'


def run(arg: list):
    if var.currentAct == "kmod":
        print("Nope, Nope, Nope. Don;t ever think about making card mod for kmod it a confusing process and very buggy for now it not useable ")
        return

    if len(arg) < 1:
        print("Error")
        return

    # find if the card name is correct
    cardName, hasFindCard, closeMatch = commandsFunc.findCard(arg[0])
    if not hasFindCard:
        print("Error can't find card")
        print(f"Close match: {closeMatch}")
        return

    # take stuff from copytopia to paste in this case cardModInfos
    temp = open("Data\Library\Copytopia.txt", "r+")
    copytopia = temp.readlines()
    temp.close()

    # open the save file to read the deck
    saveFile = saveEditFunc.readSaveFile()
    deckStart, deckEnd = commandsFunc.findDeckStartEnd()

    # filtering out stuff like "\n" and quote from the deck data for easy use
    deck = saveFile[deckStart:deckEnd]
    deck = [
        temp.strip().replace('"', "").replace(",", "").replace("\n", "")
        for temp in deck
    ]

    if cardName not in deck:
        print("Error you don't have this card in your deck")
        return

    # TODO this suck but it work for now I will find way to improve this

    # find the card "$k" and "$v" line number of the card in "cardModInfos"
    cardSK = saveEditFunc.findSaveLineIndex(
        f'"$k": "{cardName}",',
        commandsFunc.findActStart(),  # find current act start
        commandsFunc.findActStart()
        if commandsFunc.actToInt(var.currentAct) < 3
        else 2147483647,
    )

    # exception if cardModInfo is not in the list and so create one
    if cardSK == -1:
        # find the start of the cardModInfo contents list
        temp = saveEditFunc.findSaveLineIndex(
            '"$rcontent": [', saveEditFunc.findSaveLineIndex('"cardIdModInfos": {', commandsFunc.findActStart())
        )

        print(temp)
        newLine = (
            "\n"  # because f-string can;t contain "\n" so this my way to improvise
        )

        cardModDefault = copytopia[
            copytopia.index("globalCardModA\n")
            + 1 : copytopia.index("globalCardModB\n")
        ]  # take the global card mod and insert it in

        # GLOBAL CARD MOD MODIFIER
        #      "$v": {
        #     "$id": 16,
        #     "$type": "13|System.Collections.Generic.List`1[[DiskCardGame.CardModificationInfo, Assembly-CSharp]], mscorlib",
        #     "$rlength": 0,
        #     "$rcontent": [
        #     ]
        # }

        # make a card mod with the card name and the global card mod modifier
        saveEditFunc.editSaveLine(
            temp,
            f'{saveFile[temp]}{" "*4*5}{"{"}{newLine}{" "*4*6}"$k": "{cardName}",{newLine}{"".join(cardModDefault)}{" "*4*5}{"},"}',
        )

        # inscreasing the "$length"
        saveEditFunc.editSaveLine(
            temp - 1, f"{saveFile[temp-1][:-3]}{int(saveFile[temp-1][-3])+1},"
        )

        print(
            'The card you want to generate a "$v" doesn\'t have it own cardModInfo so the tool make one. Please retry the command for it to generate a "$v" for that card'
        )
        return

    cardSV = cardSK + 1

    # find the next card "$k" to find the end of the current card "$v"
    nextCardSK = saveEditFunc.findSaveLineIndex('"$k": ', cardSK)
    endCardSV = nextCardSK - 3

    startAnchor, endAnchor = "cardModA\n", "cardModB\n"
    # # change what to copy BECAUSE FOR SOME STUPID REASON KMOD USE A DIFFERENT CARD MOD MODIFIER
    # # I HAVE NO FUCKING CLUE Y. WHAT THE ACTUAL FUCK DANIEL
    # if var.currentAct == "kmod":
    #     startAnchor, endAnchor = "KmodCardModA\n", "KmodCardModB\n"

    cardModCopy = copytopia[
        copytopia.index(startAnchor) + 1 : copytopia.index(endAnchor)
    ]

    #clearing the old "$v" to insert the new one
    for i in range(cardSV, endCardSV):
        saveEditFunc.editSaveLine(cardSV + 1, "", True)

    saveEditFunc.editSaveLine(cardSV, "".join(cardModCopy))
    print('"$v" created for your card')
