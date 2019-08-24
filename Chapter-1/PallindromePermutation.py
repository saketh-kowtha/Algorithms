def counter(_str):
    _counter = {}
    for i in _str:
        if i in _counter:
            _counter[i] += 1
        else:
            _counter[i] = 1
    return _counter


def pallindromePermutation(_str1):
    if len(_str1) % 2 == 0:
        for j in counter(_str1).values():
            if j % 2 != 0:
                return False
    else:
        check = False
        print counter(_str1).values()
        for j in counter(_str1).values():
            if j % 2 != 0 :
                if check == True:
                    return False
                check = not check
    return True

