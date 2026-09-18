notes = [12, 8, 17, 14, 5, 19, 11]

def analyse_notes(notes):
    moyenne = 0 
    meilleure = notes[0]
    pire = notes[0]
    admis = 0
    echecs = 0
    somme = 0
    
    for i in notes :
        somme += i
        if i > meilleure :
            meilleure = i
        if i < pire :
            pire = i
        if i >= 10 :
            admis += 1
        else:
            echecs += 1
        

    moyenne = somme / len(notes)

    resultat = {
    "moyenne": moyenne,
    "meilleure": meilleure,
    "pire": pire,
    "admis": admis,
    "echecs": echecs
    }

    return resultat
    


print(analyse_notes(notes))