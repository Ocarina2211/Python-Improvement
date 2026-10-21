notes = [12, 8, 17, 14, 5, 19, 11, 17, 8, 17]
def frequences(notes):
    resultat = {}
    for note in notes :
        if note in resultat :
            resultat[note] += 1
        else :
            resultat[note] = 1
    return resultat

print(frequences(notes))

