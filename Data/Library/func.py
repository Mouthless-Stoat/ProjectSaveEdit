import os


def lowerLs(ls: list):
    """
    Return a lowered list
    """
    out = [x.lower() for x in ls]
    return ls


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def isClose(item: str, item2: str, threshold=0.5):
    """
    Returns True if the first item is close to the second item, based on the threshold.

    :param item: the item to be compared
    :type item: str
    :param item2: the item to compare to
    :type item2: str
    :param threshold: the minimum ratio of matching characters for the two strings to be considered a
    match
    :return: The function is returning a boolean value.
    """
    match = 0
    for i in range(len(item)):
        try:
            if item[i] == item2[i]:
                match += 1
        except:
            break
    return bool(match / len(item2) > threshold)


def chunks(list, chunksSize):
    return [list[i : i + chunksSize] for i in range(0, len(list), chunksSize)]
