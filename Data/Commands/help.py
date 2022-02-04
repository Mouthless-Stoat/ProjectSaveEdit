import os, Data.Library.func as func

name = "help"
alias = ["?", "h"]
description = "Show a list of command with it alias and description"


def run(arg: list):
    commandList = [
        __import__(command.split(".")[0])
        for command in os.listdir("Data\Commands")
        if command.endswith(".py")
    ]

    print("******************** HELP FORMAT ********************")
    print("[Command Name] [Command Alias]: [Command Description]")
    print("*****************************************************")
    print()

    arg.append("")

    if arg[0] != "":
        for command in commandList:
            try:
                alias = command.alias
            except:
                alias = []

            if command.name.lower() == arg[0] or arg[0] in func.lowerLs(alias):
                print(
                    f"- {command.name} {command.alias}: {command.description.lower().capitalize()}"
                )
                return

    for command in commandList:
        print(f"- {command.name} {command.alias}: {command.description.lower().capitalize()}")
