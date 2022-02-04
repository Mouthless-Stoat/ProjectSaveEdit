version = 0.1

path = ""
pathFile = open("path.txt", "r")

path = pathFile.readlines()[0].strip()
pathFile.close()

currentAct = "act 1"
cardList = []
with open("Data\Library\cardName.txt", "r+") as f:
    temp = f.readlines()
    for card in temp:
        cardList.append(card.strip("\n"))
print(cardList)
