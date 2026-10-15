# ==========================================
# Code PIN
# ==========================================
code = int(input("Entrer le code PIN : "))
if code == 4567:
    print("code correct")
else:
    print("code incorrect")


# ==========================================
# Signe d’un nombre
# ==========================================
nombre = int(input("Saisir un nombre entier : "))
if nombre > 0:
    print("Positif")
elif nombre < 0:
    print("Négatif")
else:
    print("Nul")


# ==========================================
# Parité
# ==========================================
nombre = int(input("Saisir un nombre entier : "))
if nombre % 2 == 0:
    print(nombre, "est un nombre pair")
else:
    print(nombre, "est un nombre impair")


# ==========================================
# Age
# ==========================================
age = int(input("Entrer votre âge : "))
if age < 12:
    res = "enfant"
elif age >= 18:
    res = "adulte"
else:
    res = "adolescent"
print("A", age, "ans, vous êtes un", res)
# print(f"A {age} ans, vous êtes un {res}.")


# ==========================================
# Perte ou profit
# ==========================================
fabrication = float(input("Prix de fabrication : "))
vente = float(input("Prix de vente : "))
if fabrication > vente:
    print("perte")
else:
    print("profit")


# ==========================================
# Maximum
# ==========================================
nb1 = float(input("Saisir le premier nombre : "))
nb2 = float(input("Saisir le second nombre : "))
nb3 = float(input("Saisir le troisième nombre : "))
if nb1 > nb2 and nb1 > nb3:
    print("Le maximum est le premier nombre :", nb1)
elif nb2 > nb1 and nb2 > nb3:
    print("Le maximum est le second nombre :", nb2)
else:
    print("Le maximum est le troisième nombre :", nb3)


# ==========================================
# Triangle rectangle
# ==========================================
c1 = int(input("côté 1 : "))
c2 = int(input("côté 2 : "))
c3 = int(input("côté 3 : "))
if c1 <= c2 and c2 <= c3:
    if c3**2 == (c1**2 + c2**2):
        print("triangle rectangle")
    else:
        print("triangle non rectangle")
else:
    print("Les longueurs des côtés n’ont pas été saisies dans l’ordre croissant.")


# ==========================================
# Année bissextile
# ==========================================
annee = int(input("Saisir l'année : "))
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print("Année bissextile")
else:
    print("Année non bissextile")


# ==========================================
# Société de transport
# ==========================================
age = int(input("Saisir votre âge : "))
if age >= 51:
    prix = 10 - (10 * 0.1)
elif age > 21:
    prix = 10
elif age >= 16:
    prix = 10 - (10 * 0.4)
elif age > 5:
    prix = 10 / 2
else:
    prix = 0
print("Le prix du transport est de", prix, "euros.")


# ==========================================
# Voyage scolaire
# ==========================================
eleves = int(input("Nombre d'élèves : "))
jours = int(input("Durée du voyage : "))
# prix du transport
if eleves <= 25:
    transport = 110
else:
    transport = 100
# prix de la nourriture
nourriture = 3.5 * jours
# prix du logement
if eleves < 20:
    logement = 4.2 * jours
elif eleves > 35:
    logement = 4 * jours
else:
    logement = 3.8 * jours
# prix total
total = transport + nourriture + logement
print("Le prix du voyage revient à", total, "euros par élève.")


# ==========================================
# Vinci location
# ==========================================
vehicule = input("Type du véhicule : ")
carburant = input("Carburant : ")
duree = int(input("Durée de location en jour : "))
distance = int(input("Distance en km : "))
offre = bool(input("Offre commerciale : "))
# prix location par jour en fonction du type de véhicule
if vehicule == "Citadine":
    location = 80 * duree
elif vehicule == "Berline":
    location = 100 * duree
elif vehicule == "Sportive":
    location = 130 * duree
else:
    print('Erreur : le type du véhicule est "Citadine" ou "Berline" ou "Sportive"')
# prix du carburant par type de carburant et par km
if carburant == "Essence":
    conso = 1.93 * distance
elif carburant == "Diesel":
    conso = 1.89 * distance
else:
    print('Erreur : le type de carburant est "Essence" ou "Diesel"')
# prix total sans offre commerciale
total = location + conso
# offre commerciale
if offre:
    total = 30 + total * 0.9
print("Le prix total de la location est de", total, "euros.")


# ==========================================
# Natation
# ==========================================
nb_seance = int(input("Nombre de séances : "))
# Tarifs
tarif_A = 145 + 10.5 * nb_seance
tarif_B = 15.5 * nb_seance
# le plus avantageux
if tarif_A < tarif_B:
    print("Pour", nb_seance, "séances, le tarif A est le plus avantageux.")
elif tarif_A > tarif_B:
    print("Pour", nb_seance, "séances, le tarif B est le plus avantageux.")
else:
    print("Pour", nb_seance, "séances, aucun tarif n'est plus avantageux que l'autre.")
# affichage détails tarifs
details = input("Souhaitez-vous afficher les montants des deux tarifs ? (yes/no) : ")
if details == "yes":
    print("Tarif A :", tarif_A, "euros")
    print("Tarif B :", tarif_B, "euros")


# ==========================================
# Voyelle, consonne ou caractère spécial
# ==========================================
ch = input("Saisir un caractère : ")
# vérification de la taille du caractère
if len(ch) != 1:
    print("Veuillez saisir un seul caractère")
else:
    if (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "y" or
        ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U" or ch == "Y"):
        print(ch, ": voyelle")
    elif (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
        print(ch, ": consonne")
    else:
        print(ch, ": caractère spécial")


# ==========================================
# Facture
# ==========================================
HT = float(input("Saisir le prix hors taxe : "))
print("Prix HT :", round(HT, 2), "euros")
# calcul prix TTC (TVA = 19.6)
TVA = 19.6
TTC = HT * (1 + TVA / 100)
print("Prix TTC :", round(TTC, 2), "euros")
# remise
if TTC < 1000:
    pourcentage_remise = 0
elif TTC < 2000:
    pourcentage_remise = 1
elif TTC < 5000:
    pourcentage_remise = 3
else:
    pourcentage_remise = 5
remise = TTC * pourcentage_remise / 100
print("Remise :", round(remise, 2), "euros")
# Net à payer
NetAPayer = TTC - remise
print("Prix Net à payer :", round(NetAPayer, 2), "euros")


# ==========================================
# Calculatrice
# ==========================================
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
operation = input("Entrez l'opération (addition, soustraction, multiplication, division) : ")
if operation == "addition":
    print(f"{nombre1} + {nombre2} = {round(nombre1 + nombre2, 2)}")
elif operation == "soustraction":
    print(f"{nombre1} - {nombre2} = {round(nombre1 - nombre2, 2)}")
elif operation == "multiplication":
    print(f"{nombre1} * {nombre2} = {round(nombre1 * nombre2, 2)}")
elif operation == "division":
    if nombre2 != 0:
        print(f"{nombre1} / {nombre2} = {round(nombre1 / nombre2, 2)}")
    else:
        print("Erreur : Division par zéro !")
else:
    print("Opération non valide.")


# ==========================================
# Impôts
# ==========================================
revenu = float(input("Entrez votre revenu annuel : "))
impot = 0
if revenu <= 10000:
    impot = 0
elif revenu <= 25000:
    impot = (revenu - 10000) * 0.1
elif revenu <= 50000:
    impot = (25000 - 10000) * 0.1 + (revenu - 25000) * 0.15
else:
    impot = (25000 - 10000) * 0.1 + (50000 - 25000) * 0.15 + (revenu - 50000) * 0.2
print(f"L'impôt à payer est de {impot} €.")


# ==========================================
# Nature d’un triangle
# ==========================================
a = float(input("Entrez la longueur du premier côté : "))
b = float(input("Entrez la longueur du deuxième côté : "))
c = float(input("Entrez la longueur du troisième côté : "))
# Vérification si les côtés forment un triangle valide
if a + b >= c and a + c >= b and b + c >= a:
    # Détermination du type de triangle
    if a == b == c:
        print("C'est un triangle équilatéral.")
    elif a == b or a == c or b == c:
        print("C'est un triangle isocèle.")
    else:
        print("C'est un triangle scalène.")
else:
    print("Les longueurs fournies ne forment pas un triangle valide.")


# ==========================================
# Salaire net
# ==========================================
salaire_base = float(input("Entrez le salaire de base de l'employé : "))
nombre_ventes = int(input("Entrez le nombre de ventes réalisées par l'employé : "))
anciennete = int(input("Entrez le nombre d'années travaillées (ancienneté) : "))
poste = bool(input("L'employé est-il un cadre ? (True/False) : "))
# Calcul de la prime de performance
prime_performance = 0
if nombre_ventes > 100:
    prime_performance = salaire_base * 0.10
# Calcul de la prime d'ancienneté
prime_anciennete = 0
if anciennete >= 5 and anciennete <= 10:
    prime_anciennete = salaire_base * 0.05
elif anciennete > 10:
    prime_anciennete = salaire_base * 0.10
# Calcul de la prime de responsabilité
prime_responsabilite = 0
if poste:
    prime_responsabilite = salaire_base * 0.05
# Calcul du salaire brut (salaire de base + primes)
salaire_brut = salaire_base + prime_performance + prime_anciennete + prime_responsabilite
# Calcul des taxes selon le salaire brut
if salaire_brut < 2000:
    taxes = salaire_brut * 0.20
elif salaire_brut <= 5000:
    taxes = salaire_brut * 0.30
else:
    taxes = salaire_brut * 0.40
# Calcul du salaire net après déduction des taxes
salaire_net = salaire_brut - taxes
# Afficher les résultats
print(f"Salaire de base : {salaire_base} €")
print(f"Prime de performance : {prime_performance} €")
print(f"Prime d'ancienneté : {prime_anciennete} €")
print(f"Prime de responsabilité : {prime_responsabilite} €")
print(f"Salaire brut : {salaire_brut} €")
print(f"Montant des taxes : {taxes} €")
print(f"Salaire net : {salaire_net} €")


# ==========================================
# Mot de passe
# ==========================================
import re
mdp = input("Entrez un mot de passe : ")
est_valide = True
if len(mdp) < 8:
    print("Le mot de passe doit contenir au moins 8 caractères.")
    est_valide = False
if not re.search("[A-Z]", mdp):
    print("Le mot de passe doit contenir au moins une majuscule.")
    est_valide = False
if not re.search("[0-9]", mdp):
    print("Le mot de passe doit contenir au moins un chiffre.")
    est_valide = False
if not re.search("[@#!$%&*]", mdp):
    print("Le mot de passe doit contenir au moins un caractère spécial (@, #, !, $, %, &, *).")
    est_valide = False
if est_valide:
    print("Mot de passe valide.")
else:
    print("Mot de passe invalide.")