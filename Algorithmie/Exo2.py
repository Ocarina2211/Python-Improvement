nombres = [2, 5, 8, 12, 16, 21, 27, 34, 40]
while True :
    try :
        nbr = int(input("Quel nombre souhaites tu rechercher ? : "))
        break
    except ValueError :
        print("Tu dois tapper un nombre.")


gauche = 0
droite = len(nombres) - 1
milieu = (gauche + droite) // 2
tour = 0
while gauche <= droite :
    if nbr < nombres[milieu] :
        droite = milieu - 1 
        milieu = (gauche + droite) // 2
        tour += 1
    elif nbr > nombres[milieu] :
        gauche = milieu + 1 
        milieu = (gauche + droite) // 2
        tour += 1
    elif nbr == nombres[milieu] :
        tour += 1
        print(f"Nombre trouvé en {tour} tours")
        break
else :
    print("Nombre introuvable")