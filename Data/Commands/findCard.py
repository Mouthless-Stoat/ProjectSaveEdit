from Data.Library import saveEditFunc, commandsFunc, func, var

name = "findCard"
alias = ["fc"]
description = "Find if a card exist or not. If not will attempt to print close match"


def run(arg: list):
    if len(arg) < 1:
        print("Error")
        return
    cardOut, hasFindCard, closeMatch = commandsFunc.findCard(arg[0])
    if hasFindCard:
        print(f"Card found: {cardOut}")
    else:
        print("Error can't find card")
        print(f"Close match: {closeMatch}")
