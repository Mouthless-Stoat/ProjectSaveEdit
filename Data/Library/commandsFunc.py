from Data.Library import saveEditFunc, var, func


def findNumCard(act = ""):
    if act == "":
        act = var.currentAct
    actTemp = actToInt(act)
    saveFile = open(saveEditFunc.path, "r+")
    saveFileLines = saveFile.readlines()
    saveFile.close()

    out = 0
    line = -1

    if actTemp == 0:  # get number of card in deck of act 1
        line = saveEditFunc.findSaveLineIndex(
            '"$rlength":',
            saveEditFunc.findSaveLineIndex(
                '"cardIds": {'
            )  # find the '"$rlength":' because that where the card number lie
            # Because the a lot of '"$rlength":'
            # so we have to put a minium at the '"cardIds": {'
        )
        out = (
            saveFileLines[line]
            # clear up everything else except the number
            .strip()
            .strip('"$rlength": ')
            .replace("\n", "")
            .replace(",", "")
        )

    elif actTemp == 1:  # get number of card in deck of act 2
        line = saveEditFunc.findSaveLineIndex(
            '"$rlength":',
            saveEditFunc.findSaveLineIndex(
                '"cardIds": {',
                saveEditFunc.findSaveLineIndex(
                    '"gbcData": {'
                ),  # the same as the code above
                # but because this is a different '"cardIds": '
                # so we have to set a minium at '"gbcData: {'
            ),
        )
        out = (
            saveFileLines[line]
            .strip()
            .strip('"$rlength": ')
            .replace("\n", "")
            .replace(",", "")
        )

    elif actTemp == 2:  # get number of card in deck of act 3
        line = saveEditFunc.findSaveLineIndex(
            '"$rlength":',
            saveEditFunc.findSaveLineIndex(
                '"cardIds": {', saveEditFunc.findSaveLineIndex('"part3Data": {')
            ),
        )
        out = (
            saveFileLines[line]
            .strip()
            .strip('"$rlength": ')
            .replace("\n", "")
            .replace(",", "")
        )

    elif actTemp == 3:  # get number of card in deck of kmod
        line = saveEditFunc.findSaveLineIndex(
            '"$rlength":',
            saveEditFunc.findSaveLineIndex(
                '"cardIds": {',
                saveEditFunc.findSaveLineIndex('"ascensionData": {'),
            ),
        )
        out = (
            saveFileLines[line]
            .strip()
            .strip('"$rlength": ')
            .replace("\n", "")
            .replace(",", "")
        )

    return int(out), line


def actToInt(act = ""):
    """
    Convert the act to an integer.
    :return: The index of the act.
    """
    if act == "":
        act = var.currentAct
    if act.lower() == "act 1":  # act 1 covert to index 0
        return 0
    if act.lower() == "act 2":  # act 2 convert to index 1
        return 1
    if act.lower() == "act 3":  # act 3 convert to index 2
        return 2
    if act.lower() == "kmod":  # kmod convert to index 3
        return 3
    return -1


def intToAct(int: int):
    if int == 0:
        return "act 1"
    if int == 1:
        return "act 2"
    if int == 2:
        return "act 3"
    if int == 3:
        return "kmod"
    return -1


def findDeckStartEnd(act = ""):
    if act == "":
        act = var.currentAct

    actTemp = actToInt(act)
    if actTemp == 0:
        deckStart = saveEditFunc.findSaveLineIndex('"cardIds": {') + 5
        deckEnd = saveEditFunc.findSaveLineIndex('"boonIds":') - 2
    elif actTemp == 1:
        deckStart = (
            saveEditFunc.findSaveLineIndex(
                '"cardIds": {', saveEditFunc.findSaveLineIndex('"gbcData": {')
            )
            + 5
        )
        deckEnd = (
            saveEditFunc.findSaveLineIndex(
                '"boonIds":', saveEditFunc.findSaveLineIndex('"gbcData": {')
            )
            - 2
        )
    elif actTemp == 2:
        deckStart = (
            saveEditFunc.findSaveLineIndex(
                '"cardIds": {', saveEditFunc.findSaveLineIndex('"part3Data": {')
            )
            + 5
        )
        deckEnd = (
            saveEditFunc.findSaveLineIndex(
                '"boonIds":', saveEditFunc.findSaveLineIndex('"part3Data": {')
            )
            - 2
        )

    elif actTemp == 3:
        deckStart = (
            saveEditFunc.findSaveLineIndex(
                '"cardIds": {', saveEditFunc.findSaveLineIndex('"ascensionData": {')
            )
            + 5
        )
        deckEnd = (
            saveEditFunc.findSaveLineIndex(
                '"boonIds":', saveEditFunc.findSaveLineIndex('"ascensionData": {')
            )
            - 2
        )

    return deckStart, deckEnd


def findActStart(act = 0):
    '''
    Finds the line number of the start of act
    
    :param act: The act you want to find the start, defaults to 0 (optional)
    :return: The index of the line where the act starts.
    '''
    if act == 0:
        act = var.currentAct
        actTemp = actToInt(act)
    else:
        actTemp = int(act)
    if actTemp == 0:
        return saveEditFunc.findSaveLineIndex('"currentRun": {')
    elif actTemp == 1:
        return saveEditFunc.findSaveLineIndex('"gbcData": {')
    elif actTemp == 2:
        return saveEditFunc.findSaveLineIndex('"part3Data": {')
    elif actTemp == 3:
        return saveEditFunc.findSaveLineIndex('"ascensionData": {')
    return -1


def findCard(card):
    """
    Return card, hasFindCard, closeMatch

    :param card: The card you're looking for
    :return: The card that is being returned.
    """
    cardOut = ""
    hasFindCard = False
    closeMatch = []
    for cardTemp in var.cardList:
        if cardTemp.lower() == card:
            cardOut = cardTemp
            hasFindCard = True

        flag = len(card) >= 3
        flag2 = card.lower() in cardTemp.lower() and flag
        flag3 = cardTemp.lower() in card.lower() and flag
        if flag2 or flag3 or func.isClose(card.lower(), cardTemp.lower(), 0.25):
            closeMatch.append(cardTemp)

    return cardOut, hasFindCard, closeMatch
