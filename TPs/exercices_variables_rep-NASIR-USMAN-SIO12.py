import math

# Exercice : Générer un mail de contact pour une recherche d'emploi

# Énoncé :
# Écrivez un script Python qui collecte des informations personnelles et professionnelles auprès de l'utilisateur,
# puis génère automatiquement un texte de mail de contact pour une candidature spontanée.
# Le mail doit inclure les informations suivantes :
# - Nom et prénom de l'utilisateur
# - Adresse email et numéro de téléphone
# - Poste recherché
# - Nom de l'entreprise cible

# Votre script doit :
# 1. Utiliser des f-strings pour générer le texte du mail.
# 2. Générer le même texte de mail sans utiliser les f-strings (en concaténant les chaînes de caractères).
# 3. Afficher les deux versions du mail généré.

# Script pour collecter des renseignements et générer un mail de contact pour une recherche d'emploi

# Collecte des renseignements auprès de l'utilisateur
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")
email = input("Entrez votre adresse email : ")
telephone = input("Entrez votre numéro de téléphone : ")
poste_recherche = input("Entrez le poste que vous recherchez : ")
entreprise_cible = input("Entrez le nom de l'entreprise cible : ")

# Génération du texte du mail
mail = f"""
Objet : Candidature spontanée pour le poste de {poste_recherche}

Bonjour,

Je me permets de vous contacter afin de vous proposer ma candidature pour un poste de {poste_recherche} au sein de votre entreprise, {entreprise_cible}. 

Je suis {prenom} {nom}, et je suis joignable par email à l'adresse {email} ou par téléphone au {telephone}. 
Je serais ravi(e) de discuter de mes compétences et de ma motivation à rejoindre votre équipe.

Dans l'attente de votre retour, je vous prie d'agréer mes salutations distinguées.

Cordialement,
{prenom} {nom}
"""

# Affichage du mail généré
print("\nVoici le texte de votre mail de contact :\n")
print(mail)

# Génération du texte du mail sans utiliser f-strings
mail = (
    "Objet : Candidature spontanée pour le poste de " + poste_recherche + "\n\n"
    "Bonjour,\n\n"
    "Je me permets de vous contacter afin de vous proposer ma candidature pour un poste de " + poste_recherche +
    " au sein de votre entreprise, " + entreprise_cible + ".\n\n"
    "Je suis " + prenom + " " + nom + ", et je suis joignable par email à l'adresse " + email +
    " ou par téléphone au " + telephone + ".\n"
    "Je serais ravi(e) de discuter de mes compétences et de ma motivation à rejoindre votre équipe.\n\n"
    "Dans l'attente de votre retour, je vous prie d'agréer mes salutations distinguées.\n\n"
    "Cordialement,\n" + prenom + " " + nom
)

# Affichage du mail généré
print("\nVoici le texte de votre mail de contact :\n")
print(mail)


# Bonus : quand les élèves abordent les conditions 
# Ajoutez une validation pour vérifier que l'adresse email contient un "@" et que le numéro de téléphone ne contient que des chiffres.
if "@" not in email:
    print("Attention : L'adresse email semble invalide.")

if not telephone.isdigit():
    print("Attention : Le numéro de téléphone doit contenir uniquement des chiffres.")

# ----------------- EXERCICES DE MANIPULATION DE NOMBRES -----------------
# Voici quelques exercices pour pratiquer la manipulation de nombres en Python.
# Complétez le code ci-dessous pour afficher la somme de deux nombres de deux façons différentes
# 1. En utilisant des f-strings
# 2. En concaténant les chaînes de caractères
x= 10
y= 5
z= x + y
print(f"La somme de {x} et {y} est {z}")
print("La somme de " + str(x) + " et " + str(y) + " est " + str(z))

# Voici quelques exercices pour pratiquer la manipulation de chaînes de caractères en Python.
# Complétez le code ci-dessous pour afficher une phrase de deux façons différentes
phrase = "Bonjour, je m'appelle John."
print(f"Voici ma phrase : {phrase}")
print("Voici ma phrase : " + phrase)
# Voici quelques exercices pour pratiquer la manipulation de types de données en Python.
# Complétez le code ci-dessous pour afficher le type de différentes variables
print(type(x))
print(type(y))
print(type(z))
print(type(phrase))
print(type(email))
print(type(telephone))  

# Voici quelques exercices pour pratiquer la saisie utilisateur en Python.
# Complétez le code ci-dessous pour demander à l'utilisateur son nom et son âge,
nom_utilisateur = input("Entrez votre nom : ")
age_utilisateur = input("Entrez votre âge : ")
age_utilisateur = int(age_utilisateur)  # conversion de age_utilisateur en entier
# puis afficher un message personnalisé avec son nom et l'année de naissance.
annee_naissance = 2023 - age_utilisateur
print(f"Bonjour {nom_utilisateur}, vous êtes né(e) en {annee_naissance}.")  
print("Bonjour " + nom_utilisateur + ", vous êtes né(e) en " + str(annee_naissance) + ".")  

# ----------------- EXERCICES DE MANIPULATION DE VARIABLES -----------------

# Exercice 1 : Échange de valeurs
# Échangez les valeurs de deux variables a et b, puis affichez-les.
a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")

# Exercice 2 : Calcul de la moyenne
# Calculez la moyenne de trois nombres donnés.
a, b, c = 4, 8, 12
moyenne = (a + b + c) / 3
print(f"La moyenne est {moyenne}")

# Exercice 3 : Conversion Celsius en Fahrenheit
# Convertissez une température donnée en Celsius en Fahrenheit.
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C correspond à {fahrenheit}°F")

# Exercice 4 : Calcul de l'aire d'un rectangle
# Calculez l'aire d'un rectangle à partir de sa longueur et de sa largeur.
longueur = 7
largeur = 3
aire = longueur * largeur
print(f"L'aire du rectangle est {aire}")

# Exercice 5 : Calcul du périmètre d'un cercle
# Calculez le périmètre d'un cercle à partir de son rayon.
rayon = 5
perimetre = 2 * math.pi * rayon
print(f"Le périmètre du cercle est {perimetre}")

# Exercice 6 : Inversion de chaîne
# Inversez une chaîne de caractères donnée.
chaine = "Python"
chaine_inversee = chaine[::-1]
print(f"Chaîne inversée : {chaine_inversee}")

# Exercice 7 : Calcul de la puissance
# Calculez la puissance d'un nombre donné (exemple : 2^3).
base = 2
exposant = 3
resultat = base ** exposant
print(f"{base}^{exposant} = {resultat}")

# Exercice 8 : Vérification de la présence d'un mot
# Vérifiez si un mot donné est présent dans une phrase.
phrase = "Bonjour tout le monde"
mot = "tout"
presence = mot in phrase
print(f"Le mot '{mot}' est-il dans la phrase ? {presence}")

# Exercice 9 : Calcul du reste
# Calculez le reste de la division de deux nombres.
dividende = 17
diviseur = 4
reste = dividende % diviseur
print(f"Le reste de {dividende} ÷ {diviseur} est {reste}")

# Exercice 10 : Conversion en majuscules
# Convertissez une chaîne de caractères en majuscules.
chaine = "hello world"
chaine_maj = chaine.upper()
print(f"En majuscules : {chaine_maj}")

# Exercice 11 : Conversion en minuscules
# Convertissez une chaîne de caractères en minuscules.
chaine = "HELLO WORLD"
chaine_min = chaine.lower()
print(f"En minuscules : {chaine_min}")

# Exercice 12 : Remplacement de caractères
# Remplacez un mot dans une phrase par un autre mot.
phrase = "J'aime Python"
nouvelle_phrase = phrase.replace("Python", "Java")
print(f"Nouvelle phrase : {nouvelle_phrase}")

# Exercice 13 : Calcul du carré d'un nombre
# Calculez le carré d'un nombre donné.
nombre = 6
carre = nombre ** 2
print(f"Le carré de {nombre} est {carre}")

# Exercice 14 : Extraction de sous-chaîne
# Extrayez une sous-chaîne d'une chaîne donnée.
chaine = "Programmation"
sous_chaine = chaine[0:5]
print(f"Sous-chaîne extraite : {sous_chaine}")

# Exercice 15 : Arrondi d'un nombre flottant
# Arrondissez un nombre flottant à l'entier le plus proche.
nombre_flottant = 3.7
nombre_arrondi = round(nombre_flottant)
print(f"{nombre_flottant} arrondi est {nombre_arrondi}")

# Exercice 16 : Vérification de la longueur d'une chaîne
# Vérifiez si une chaîne contient plus de 10 caractères.
chaine = "Bonjour"
longueur_sup_10 = len(chaine) > 10
print(f"La chaîne contient plus de 10 caractères ? {longueur_sup_10}")

# Exercice 17 : Conversion d'une chaîne en liste
# Convertissez une chaîne de caractères en une liste de mots.
chaine = "Apprendre Python est amusant"
liste_mots = chaine.split()
print(f"Liste des mots : {liste_mots}")

