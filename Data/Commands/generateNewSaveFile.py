from Data.Library import var, commandsFunc, saveEditFunc
import os

name = "generateNewSave"
alias = ["mksf", "gensave"]
description = "Generate a new save file. In case your save file get corrupt"


def run(arg: list):
   sampleFile = open("Data\Sample\SaveFile.gwsave", "r+")
   saveFile = open(f"{var.path}", "w")
   for line in sampleFile.readlines():
      saveFile.write(line)
   print("New save file generated")
