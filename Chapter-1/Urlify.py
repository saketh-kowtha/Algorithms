def urlify(url):
    return "".join(["%20" if e == ' ' else e for e in url])

print urlify("a aa a   a")