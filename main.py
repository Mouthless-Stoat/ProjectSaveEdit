import sys, os, importlib, shlex
from Data.Library import var, func, commandsFunc
import Data.Commands.backupSaveFile


def reloadCommands():
    global commandsList
    commandsList = []
    for file in os.listdir("Data\Commands"):
        if file.endswith(".py"):
            print(f"Reloaded {file}!")
            commandsList.append(__import__(file.split(".")[0]))

    for command in commandsList:
        importlib.reload(command)


sys.path.insert(0, "Data\Commands")
commandsList = []
reloadCommands()

var.version = 0.1

Data.Commands.backupSaveFile.run([])  # backup the save file

func.clear()
print(f"Project Save Edit V{var.version}")

while True:
    hasFindCommand = False
    # take input
    c = input(f"FLOPPY DRIVE Z:\SaveFile\{var.currentAct.capitalize()}> ").strip()
    cArgs = []

    # do split it up
    c = shlex.split(c)
    # print(c)
    if len(c) > 0:
        c, cArgs = c.pop(0).strip(), c
        # print(c, cArgs)

    # find command to execute
    for command in commandsList:
        try:
            c.lower()
        except:
            break

        if command.name.lower() == c.lower() or c.lower() in func.lowerLs(
            command.alias
        ):
            for i in range(len(cArgs)):
                cArgs[i] = cArgs[i].lower()

            command.run(cArgs)
            hasFindCommand = True
            break

    # some special command for making custom commands
    if c in ["reload", "rl"]:
        reloadCommands()
        hasFindCommand = True

    elif c in ["quit", "q"]:
        quit()

    elif c in ["mkcmd", "makecommand", "addcommand", "acmd"]:
        if len(cArgs) < 4:
            cArgs = ["newCommand", "newCommand", "", "This a new command"]

        print(f"Command file '{cArgs[0]}' created")
        temp = open(f"Commands\{cArgs.pop(0)}.py", "w+")
        temp.writelines(
            [
                "from Data.Library import saveEditFunc, commandsFunc, func, var\n",
                f'name = "{cArgs.pop(0)}"\n',
                f"alias = {cArgs[:-1]}\n",
                f'description = "{cArgs[-1]}"\n',
                "def run(arg: list):\n",
                '    print("Command Ran")',
            ]
        )
        temp.close()

        hasFindCommand = True

    elif c == "runall":
        for command in commandsList:
            command.run([])
        hasFindCommand

    if not hasFindCommand:
        print("Command not found")
