from Data.Library import func, var

name = "showCard"
alias = ["card", "sc", "c"]
description = "[Page number] Show a list of card. There only 17 pages. If you don't input a number after the command it fail"


def run(arg: list):
    a = func.chunks(var.cardList, 14)
    try:
        arg = int(arg[0])
        a[arg]
    except:
        print("Error")
        return

    print(f"Page {arg}: {a[arg]}")