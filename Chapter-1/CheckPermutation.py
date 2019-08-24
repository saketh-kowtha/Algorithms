def checkPermutation(_str1, _str2):
    if len(_str1) == len(_str2) and counter(_str1) == counter(_str2):
        return True
    else:
        return False



def counter(_str):
    _counter = {}
    for i in _str:
        if i in _counter:
            _counter[i] += 1
        else:
            _counter[i] = 1
    return _counter

