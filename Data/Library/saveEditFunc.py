from Data.Library.var import *
import sys


def editSaveLine(lineIndex: int, replacement: str, delLine=False) -> None:
    """
    Replace a line in a file with the replacement string.

    :param lineIndex: The line number of the line to be replaced
    :param replacement: The string to replace the line with
    :return: The line that was replaced.
    """
    if lineIndex < 0:
        print("Error")
        return -1

    saveFile = open(path, "r+")
    lines = saveFile.readlines()
    saveFile.close()
    saveFile = open(path, "w")
    lines[lineIndex] = replacement + "\n"
    if delLine:
        lines.remove(replacement + "\n")
    saveFile.writelines(lines)
    saveFile.close()


def findSaveLineIndex(phase: str, minLineIndex=-1, maxLineIndex=2147483647) -> int:
    """
    Return the line index of a given phase in the save file.

    :param phase: The phase that you want to find the line index for
    :param minLineIndex: The index of the line to start searching from
    :return: The index of the line containing the phase.
    """
    saveFile = open(path, "r+")
    lines = saveFile.readlines()
    saveFile.close()

    for i in range(len(lines)):
        if phase in lines[i] and i > minLineIndex and i < maxLineIndex:
            return i
    else:
        return -1


def readSaveFile() -> list:
    """
    Reads the save file and returns a list of lines.
    :return: A list of strings.
    """
    saveFile = open(path, "r+")
    out = [line for line in saveFile.readlines()]
    saveFile.close()
    return out
