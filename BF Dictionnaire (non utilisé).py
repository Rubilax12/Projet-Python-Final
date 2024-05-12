import os

def load_passwords(filename):
    #Utilisation de l'encodage classique (utf-8)
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        #Lecture de toutes les lignes dans le fichier filename
        for line in f:
            #generator yield pour retourner les élements de la liste ('Rockyou.txt' dans ce script)
            yield line.strip()

def verificationPassword(password):
    filename = "/home/callme_root/Documents/PythonProjet/code/wordlist.txt"
    #Vérifier si la liste existe
    if os.path.exists(filename):
        #1ere vérification: si le mot de passe est dans la liste
        for mdp in load_passwords(filename):
            if mdp == password:
                print(mdp)
                return "Bad Password :/ (found in common passwords)"
    else:
        return "List unfoundable."


password = "mdp123"
print(verificationPassword(password))
