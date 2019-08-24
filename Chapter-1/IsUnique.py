def isUnique(_str):
    for index, key in enumerate(_str):
        if _str.index(key) != index:
            return False
    return True

