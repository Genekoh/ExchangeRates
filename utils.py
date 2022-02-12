def listToCommaSepString(l):
    fs = ""
    for i, s in enumerate(l):
        if i == 0:
            fs += s
        else:
            fs += f",{s}"

    return fs
