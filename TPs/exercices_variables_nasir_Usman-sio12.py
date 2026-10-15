import math

# =====================================================================
# EXERCICE PRINCIPAL : Générer un mail de contact pour une recherche d'emploi
# =====================================================================

# ----------------- Collecte des renseignements auprès de l'utilisateur ------------------
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")
email = input("Entrez votre adresse email : ")
telephone = input("Entrez votre numéro de téléphone : ")
poste = input("Entrez le poste recherché : ")
entreprise = input("Entrez le nom de l'entreprise cible : ")

# ----------------- Génération du texte du mail (avec f-strings) ------------------
mail_fstring = f"""
Bonjour,

Je me permets de vous contacter car je souhaite postuler pour le poste de {poste} au sein de votre entreprise {entreprise}.
Actuellement à la recherche de nouvelles opportunités, je serais ravi(e) d'échanger avec vous sur la manière dont mes compétences pourraient contribuer à vos projets.

Vous trouverez ci-joint mon CV.

Cordialement,
{prenom} {nom}
Email : {email}
Téléphone : {telephone}
"""

# ----------------- Affichage du mail généré (f-strings) ------------------
print("\n--- Mail généré avec les f-strings ---")
print(mail_fstring)


# ----------------- Génération du texte du mail sans utiliser f-strings ------------------
mail_concat = "\nBonjour,\n\n" + \
              "Je me permets de vous contacter car je souhaite postuler pour le poste de " + poste + " au sein de votre entreprise " + entreprise + ".\n" + \
              "Actuellement à la recherche de nouvelles opportunités, je serais ravi(e) d'échanger avec vous sur la manière dont mes compétences pourraient contribuer à vos projets.\n\n" + \
              "Vous trouverez ci-joint mon CV.\n\n" + \
              "Cordialement,\n" + \
              prenom + " " + nom + "\n" + \
              "Email : " + email + "\n" + \
              "Téléphone : " + telephone + "\n"

# ----------------- Affichage du mail généré (sans f-strings) ------------------
print("\n--- Mail généré par concaténation ---")
print(mail_concat)


# =====================================================================
# EXERCICES DE MANIPULATION DE NOMBRES
# =====================================================================
x = 10
y = 5
z = x + y

# 1. En utilisant des f-strings
print(f"La somme de {x} et {y} est : {z}")
# 2. En concaténant les chaînes de caractères (en convertissant z en str)
print("La somme de " + str(x) + " et " + str(y) + " est : " + str(z))


# =====================================================================
# EXERCICES DE MANIPULATION DE CHAÎNES DE CARACTÈRES
# =====================================================================
phrase = "Bonjour, je m'appelle John."
# Afficher la phrase de deux façons différentes
print(phrase)
print(f"{phrase}")


# =====================================================================
# EXERCICES DE MANIPULATION DE TYPES DE DONNÉES
# =====================================================================
print("--- Types des variables ---")
print(type(x))
print(type(y))
print(type(z))
print(type(phrase))
print(type(email))
print(type(telephone))


# =====================================================================
# EXERCICES DE SAISIE UTILISATEUR
# =====================================================================
nom_utilisateur = input("Entrez votre nom : ")
age_utilisateur = input("Entrez votre âge : ")
age_utilisateur = int(age_utilisateur)  # conversion de age_utilisateur en entier

annee_naissance = 2026 - age_utilisateur
print(f"Bonjour {nom_utilisateur}, vous êtes né(e) en {annee_naissance}.")


# =====================================================================
# EXERCICES DE MANIPULATION DE VARIABLES
# =====================================================================

# Exercice 1 : Échange de valeurs
a = 5
b = 10
a, b = b, a
print(f"Exercice 1 -> a : {a}, b : {b}")


# Exercice 2 : Calcul de la moyenne
a, b, c = 4, 8, 12
moyenne = (a + b + c) / 3
print(f"Exercice 2 -> Moyenne : {moyenne}")


# Exercice 3 : Conversion Celsius en Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"Exercice 3 -> Fahrenheit : {fahrenheit}")


# Exercice 4 : Calcul de l'aire d'un rectangle
longueur = 7
largeur = 3
aire = longueur * largeur
print(f"Exercice 4 -> Aire : {aire}")


# Exercice 5 : Calcul du périmètre d'un cercle
rayon = 5
perimetre_cercle = 2 * math.pi * rayon
print(f"Exercice 5 -> Périmètre : {perimetre_cercle}")


# Exercice 6 : Inversion de chaîne
chaine = "Python"
chaine_inverse = chaine[::-1]
print(f"Exercice 6 -> Inversion : {chaine_inverse}")


# Exercice 7 : Calcul de la puissance
base = 2
exposant = 3
puissance = base ** exposant
print(f"Exercice 7 -> Puissance : {puissance}")


# Exercice 8 : Vérification de la présence d'un mot
phrase = "Bonjour tout le monde"
mot = "tout"
presence = mot in phrase
print(f"Exercice 8 -> Présent : {presence}")


# Exercice 9 : Calcul du reste
dividende = 17
diviseur = 4
reste = dividende % diviseur
print(f"Exercice 9 -> Reste : {reste}")


# Exercice 10 : Conversion en majuscules
chaine = "hello world"
chaine_maj = chaine.upper()
print(f"Exercice 10 -> Majuscules : {chaine_maj}")


# Exercice 11 : Conversion en minuscules
chaine = "HELLO WORLD"
chaine_min = chaine.lower()
print(f"Exercice 11 -> Minuscules : {chaine_min}")


# Exercice 12 : Remplacement de caractères
phrase = "J'aime Python"
nouvelle_phrase = phrase.replace("Python", "le code")
print(f"Exercice 12 -> Remplacement : {nouvelle_phrase}")


# Exercice 13 : Calcul du carré d'un nombre
nombre = 6
carre = nombre ** 2
print(f"Exercice 13 -> Carré : {carre}")


# Exercice 14 : Extraction de sous-chaîne ("progr")
chaine = "Programmation"
sous_chaine = chaine[0:5].lower() # ou chaine[:5].lower()
print(f"Exercice 14 -> Sous-chaîne : {sous_chaine}")


# Exercice 15 : Arrondi d'un nombre flottant
nombre_flottant = 3.7
nombre_arrondi = round(nombre_flottant)
print(f"Exercice 15 -> Arrondi : {nombre_arrondi}")


# Exercice 16 : Vérification de la longueur d'une chaîne
chaine = "Bonjour"
longueur_sup_10 = len(chaine) > 10
print(f"Exercice 16 -> Longueur > 10 : {longueur_sup_10}")


# Exercice 17 : Conversion d'une chaîne en liste
chaine = "Apprendre Python est amusant"
liste_mots = chaine.split()
print(f"Exercice 17 -> Liste de mots : {liste_mots}")