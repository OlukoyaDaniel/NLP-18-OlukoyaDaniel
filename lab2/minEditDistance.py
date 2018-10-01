def mEditDistance(sourceString, targetString):
    if sourceString == "":
        return len(targetString)
    if targetString == "":
        return len(sourceString)
    if sourceString[-1] == targetString[-1]:
        cost = 0
    else:
        cost = 2

    minEditDistance = min([mEditDistance(sourceString[:-1], targetString)+1,
                           mEditDistance(sourceString, targetString[:-1])+1,
                           mEditDistance(sourceString[:-1], targetString[:-1]) + cost])
    return minEditDistance

print(mEditDistance("Mannhaton", "Manhattan"))