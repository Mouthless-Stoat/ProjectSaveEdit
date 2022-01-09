import os
import fileinput
from termcolor import colored

# TODO add in customization funtion like removing debugging command
# region funtion


class command:
    def __init__(self, commandName: str, desp: str, func):
        self.name = commandName
        self.description = desp
        self.func = func
        commandList.append(self)


def findLineIndex(fileDir, phase, minLineNum=-1, maxLineNum=10000000000):
    file = open(fileDir)
    for lineNum, line in enumerate(file):
        if phase in line:
            if lineNum > minLineNum and lineNum < maxLineNum:
                return lineNum

    return -1


def editLine(fileDir, lineIndex, newLine):
    # fileinput.filelineno() is the line number
    for line in fileinput.input(fileDir, inplace=True):
        if fileinput.filelineno() == lineIndex + 1:  # change only line with line index
            print(newLine)
            continue
        print(line, end="")


def readBetween2Line(fileDir, start: int, stop: int):
    str = ""
    file = open(fileDir)
    for lineNum, line in enumerate(file):
        if lineNum > stop:
            return str
        if lineNum >= start:
            str += line


def readLine(fileDir, lineIndex):
    file = open(fileDir)
    for lineNum, line in enumerate(file):
        if lineNum == lineIndex:
            return line


def readBetweenPhase(fileDir: str, startPhase: str, stopPhase: str):
    a = findLineIndex(fileDir, startPhase)
    b = findLineIndex(fileDir, stopPhase) - 1
    return readBetween2Line(fileDir, a, b)


def clear(arg=""):
    os.system("cls" if os.name == "nt" else "clear")


def printError(statment: str):
    if showErrorMsg:
        print(colored("Error: " + statment, "red", attrs=["reverse"]))


def printCorrection(statment: str, correction=False):
    if showCorrectionMsg:
        if correction:
            statment = "Correction: " + statment
        print(colored(statment, "green", attrs=["reverse"]))


def chunks(list, chunksSize):
    return [list[i : i + chunksSize] for i in range(0, len(list), chunksSize)]


def makeLower(var: list):
    out = []
    for i in var:
        out.append(i)
    return out


# endregion

# region command function
def help(arg=""):
    if arg == "":
        for i in commandList:
            print(i.name)
        return

    for i in commandList:
        if i.name == arg:
            print(i.description)
            return

    printError(f"'{arg}' is not a internal or external command")


def folder(arg=""):
    print(gameFolder)


def start(arg=""):
    os.startfile(f"{gameFolder}\inscryption.exe")
    printCorrection("Please wait while your computer trying to open the game")


def toggelErrorMsg(arg=""):
    global showErrorMsg
    showErrorMsg = not showErrorMsg


def toggelCorrectionMsg(arg=""):
    global showCorrectionMsg
    showCorrectionMsg = not showCorrectionMsg


def readDeck(arg=""):
    # spd is shorten for start player deck
    spd = findLineIndex(saveFile, '"cardIds": {')

    # get number of card in the player deck
    numCardLine = spd + 3
    numCard = int(
        readLine(saveFile, numCardLine).strip('"$rlength": ').replace(",", "")
    )

    # ds = deck start
    ds = spd + 5

    # de = deck end
    de = findLineIndex(saveFile, '"boonIds":', spd) - 3

    deck = (
        readBetween2Line(saveFile, ds, de)
        .replace('"', "")
        .replace("\n", "")
        .replace(" ", "")
        .split(",")
    )

    print(f"Deck: {deck}")
    print(f"Card in deck: {numCard}")


def showCard(arg=""):
    try:
        p = int(arg) - 1
        cardList[p]
    except ValueError:
        printError(f"'{arg}' is not a number")
        printCorrection(f"Auto correct to 1...", True)
        p = 0
    except IndexError:
        printError("Page too large, there only 27 pages")
        printCorrection("Auto correct to 27...", True)
        p = 26

    print(f"Page {p+1}: {cardList[p]}")


def addCard(arg=""):
    findCard = False
    # sd is shorten for start player deck
    sd = findLineIndex(saveFile, '"cardIds": {')

    numCardLine = sd + 3
    numCard = int(
        readLine(saveFile, numCardLine).strip('"$rlength": ').replace(",", "")
    )

    editLine(saveFile, numCardLine, f'"$rlength": {numCard+1},')

    # get number of card in the player deck
    numCardLine = sd + 3
    numCard = int(
        readLine(saveFile, numCardLine).strip('"$rlength": ').replace(",", "")
    )

    # de = deck end
    de = findLineIndex(saveFile, '"boonIds":', sd) - 3

    # find card in the cardlist
    for cardPage in cardList:
        for card in cardPage:
            if card == arg:
                findCard = True

    if not findCard:
        printError(f"'{arg}' is not a card")
        for cardPage in cardList:
            for card in cardPage:
                if arg.lower() == card.lower():
                    arg = card
                    printCorrection(f"Auto correct to {card}", True)
                    findCard = True
                    break

    if arg == "":
        arg = "Stoat"
        findCard = True

    if findCard:
        oldLine = readLine(saveFile, de).strip("\n")
        editLine(saveFile, de, f'{oldLine}, "{arg}"')

        printCorrection(
            f"Card '{arg}' added please reload your game by going to the title screen and continue"
        )
        readDeck()
        return

    printError(f"There are no auto correction that can be done")


# good enough
def removeCard(arg=""):
    findCard = False
    # sd is shorten for start player deck
    sd = findLineIndex(saveFile, '"cardIds": {')

    # de = deck end
    de = findLineIndex(saveFile, '"boonIds":', sd) - 2
    # ds = deck start
    ds = sd + 4

    cardLine = findLineIndex(saveFile, f'"{arg}"', ds, de)

    if cardLine == -1:
        printError(f"'{arg}' is not in your deck")
        for cardPage in cardList:
            for card in cardPage:
                if (
                    arg.lower() == card.lower()
                    and findLineIndex(saveFile, f'"{card}"', ds, de) > -1
                ):
                    arg = card
                    printCorrection(f"Auto correct to '{card}'", True)
                    cardLine = findLineIndex(saveFile, f'"{arg}"', ds, de)
                    findCard = True
                    break

        if not findCard:
            printError("There are no auto correction that can be done")
            return

    numCardLine = sd + 3
    numCard = int(
        readLine(saveFile, numCardLine).strip('"$rlength": ').replace(",", "")
    )

    editLine(saveFile, numCardLine, f'"$rlength": {numCard-1},')

    newLine = (
        readLine(saveFile, cardLine)
        .replace(f'"{arg}"', "", 1)
        .replace(",", "", 1)
        .replace("\n", "")
        .replace(" ", "")
    )

    editLine(saveFile, cardLine, newLine)

    # removing commas from the line before
    if newLine == "":
        editLine(
            saveFile, cardLine - 1, readLine(saveFile, cardLine - 1).replace(",", "", 1)
        )

    readDeck()


def quitTer(arg=""):
    exit()


# endregion

# var
commandList = []
showErrorMsg = True
showCorrectionMsg = True

# create the card list
cardListFile = open("cardName.txt", "r")
preCardList = cardListFile.readlines()
cardList = []
for i in preCardList:
    cardList.append(i.strip("\n"))
cardList = chunks(cardList, 9)

# region create command
command("help", "Show list of command", help)

command("fd", "Print the game folder if you are having some issue", folder)

command("start", "Start up Inscryption if you that lazy", start)

command(
    "terr",
    "Toggle error message. Error message being any red message. This is not recommended",
    toggelErrorMsg,
)

command(
    "tcorr",
    "Toggle correction message. Correction message being any message that is green. This is not recommended",
    toggelCorrectionMsg,
)

command(
    "deck",
    "Show what card you currently have in your deck and the number of card in your deck",
    readDeck,
)

command("card", "[page] show the list of card you can add using 'ac'", showCard)

command("ac", "[cardName] Add card into your deck using save edit", addCard)

command("rmc", "[cardName] remove card from your deck using save edit", removeCard)

command("cls", "Clear the terminal", clear)

command("quit", "Quit the tool", quitTer)
# endregion

clear()
print("This tool is still in Alpha testing")
print("If you find a bug pls dm me on discord under the user name khanhFG#3753")
print("Anyway have fun")
print("Tip you can run help and the command name to have the command description")
print("Press enter to continue")
input()

info = open("info.txt", "r")
line = info.read()
if "Please replace this text with your Inscryption folder location" in line:
    printError("You haven't put your game directory")
    quitTer()

gameFolder = line
info.close()
saveFile = f"{gameFolder}\SaveFile.gwsave"

clear()
print("Error: Unexpected data encounter")
print("Begin data wipe")
print("Type 'help' to see command list")

while True:
    choice = input("FLOPPY DRIVE Z:\SaveFile.gwsave> ")  # get input
    hasFindCommand = False
    arg = ""

    # separate the command and the argument
    if len(choice.split(" ")) > 1:
        t = choice.split(" ")
        del t[2:]
        choice, arg = t

    # run the command
    for i, obj in enumerate(commandList):
        if obj.name == choice.lower():
            commandList[i].func(arg)
            hasFindCommand = True

    if not hasFindCommand:
        printError(f"'{choice}' is not a internal or external command")
