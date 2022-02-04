from Data.Library import saveEditFunc

name = "changeChallengeLevel"
alias = ["ccl"]
description = "[New challenge level] Change Kaycee's mod challenge level. Will not affect other act"


def run(arg: list):
    try:
        int(arg[0])
    except:
        arg.append(0)

    saveEditFunc.editSaveLine(
        saveEditFunc.findSaveLineIndex('"challengeLevel":'),
        f'{8*" "}"challengeLevel": {arg[0]}',
    )
    print("Challenge Level changed")
