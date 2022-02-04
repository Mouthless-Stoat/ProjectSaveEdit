from Data.Library import commandsFunc, var

name = "changeAct"
alias = ["ca"]
description = "[Act] change the current act that you save edit from (0: Act 1, 1: Act 2, etc.)"


def run(arg:list):
    try:
        act = commandsFunc.intToAct(int(arg[0]))
    except:
        act = -1

    if act == -1:
        print("Error")
        return
    var.currentAct = act
