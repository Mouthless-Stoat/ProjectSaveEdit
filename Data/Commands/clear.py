import os, Data.Library.func as func

name = "clear"
alias = ["cls"]
description = "Clear the terminal"


def run(arg:list):
    func.clear()
