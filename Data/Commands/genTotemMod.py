from Data.Library import saveEditFunc, commandsFunc, func, var

name = "genTotemMod"
alias = ["genttm"]
description = "Generate a totem modifier for current act. Act 2 don't have totem so this command do nothing for that."


def run(arg: list):
    print("Started")
    totemStartLine = saveEditFunc.findSaveLineIndex(
        '"totems": {', commandsFunc.findActStart()
    )
    totemEndLine = saveEditFunc.findSaveLineIndex(
        '"totemTops": {', commandsFunc.findActStart()
    )

    temp = open("Data\Library\Copytopia.txt", "r+")
    copytopia = temp.readlines()
    temp.close()

    for i in range(totemStartLine, totemEndLine-1):
        saveEditFunc.editSaveLine(totemStartLine + 1, "", True)

    startAnchor, endAnchor = "totemA\n", "totemB\n"
    if var.currentAct == "kmod":
        startAnchor, endAnchor = "kmodTotemA\n", "kmodTotemB\n"

    totemModCopy = copytopia[
        copytopia.index(startAnchor) + 1 : copytopia.index(endAnchor)
    ]

    saveEditFunc.editSaveLine(totemStartLine, "".join(totemModCopy))
