# Contexte : Vous êtes développeur pour une petite entreprise qui gère des événements. 
# Vous devez manipuler des variables et utiliser la concaténation pour résoudre les exercices suivants.

# Exercice 1 : Afficher un message de bienvenue
nom = "Alice"
print("Bienvenue " + nom + " !")

# Exercice 2 : Créer une phrase avec deux variables
prenom = "Jean"
ville = "Paris"
print(prenom + " habite à " + ville + ".")

# Exercice 3 : Ajouter un âge à la phrase
age = 25
print(prenom + " a " + str(age) + " ans et habite à " + ville + ".")

# Exercice 4 : Utiliser une concaténation avec des f-strings
print(f"{prenom} a {age} ans et habite à {ville}.")

# Exercice 5 : Créer une phrase avec des informations sur un événement
evenement = "conférence"
date = "15 octobre 2025"
print(f"Une {evenement} est prévue le {date}.")

# Exercice 6 : Ajouter une heure à l'événement
heure = "14h"
print(f"Une {evenement} est prévue le {date} à {heure}.")

# Exercice 7 : Construire une phrase avec des variables numériques
participants = 120
print(f"L'événement aura lieu à {ville} avec {participants} participants.")

# Exercice 8 : Combiner des chaînes de caractères avec des répétitions
separateur = "-"
print(separateur * 20)

# Exercice 9 : Ajouter un titre formaté
titre = "Programme de la journée"
print(separateur * 5 + " " + titre + " " + separateur * 5)

# Exercice 10 : Créer une phrase avec des informations dynamiques
nom_evenement = "Hackathon"
duree = 48
print(f"Le {nom_evenement} durera {duree} heures.")

# # Exercice 11 : Ajouter une condition pour personnaliser un message
# if participants > 100:
#     print(f"L'événement {nom_evenement} est très populaire avec {participants} participants !")

# Exercice 12 : Créer une liste de participants et afficher un message
liste_participants = ["Alice", "Bob", "Charlie"]
print("Les participants sont : " + ", ".join(liste_participants) + ".")

# Exercice 13 : Ajouter un participant et mettre à jour le message
liste_participants.append("Diane")
print("Les participants sont maintenant : " + ", ".join(liste_participants) + ".")

# Exercice 14 : Afficher un message avec le nombre de participants
print(f"Il y a actuellement {len(liste_participants)} participants inscrits.")

# Exercice 15 : Formater une phrase avec des majuscules
nom_entreprise = "TechEvents"
print(f"Bienvenue chez {nom_entreprise.upper()} !")

# Exercice 16 : Créer une phrase avec des variables et des sauts de ligne
description = f"L'événement {nom_evenement} aura lieu à {ville}.\nIl commencera le {date} à {heure}."
print(description)

# # Exercice 17 : Ajouter une variable booléenne pour personnaliser un message
# inscription_ouverte = True
# if inscription_ouverte:
#     print("Les inscriptions sont ouvertes !")
# else:
#     print("Les inscriptions sont fermées.")

# Exercice 18 : Créer une phrase avec des valeurs arrondies
prix = 49.99
print(f"Le prix d'entrée est de {prix:.2f} euros.")

# Exercice 19 : Construire une phrase avec des variables imbriquées
organisateur = "Jean Dupont"
contact = f"Pour toute question, contactez {organisateur} à l'adresse contact@techevents.com."
print(contact)

# Exercice 20 : Créer une phrase finale avec toutes les informations
resume = f"L'événement {nom_evenement} organisé par {nom_entreprise} aura lieu à {ville} le {date} à {heure}. Il durera {duree} heures et accueillera {participants} participants."
print(resume)