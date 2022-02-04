from Data.Library import saveEditFunc, commandsFunc, var
import random

name = "changeSeed"
alias = ["cs"]
description = "[New seed] change your current seed"


def run(arg: list):
    act = commandsFunc.actToInt()

    currentSeedLine = (
        saveEditFunc.findSaveLineIndex('"randomSeed":')
        if act != 3
        else saveEditFunc.findSaveLineIndex('"currentRunSeed":')
    )
    
    try:
        newSeed = int(arg[0])
    except:
        newSeed = random.randint(1, 9999999)

    if (
        saveEditFunc.editSaveLine(
            currentSeedLine,
            "\t"
            + ('"randomSeed": ' if act != 3 else '"currentRunSeed": ')
            + str(newSeed)
            + ",",
        )
        != -1
    ):
        print("Seed Changed")
        print(f"New seed: {newSeed}")
