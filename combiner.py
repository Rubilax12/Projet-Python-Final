import os
import itertools
import string
import time

def load_passwords(filename):
    # Utilisation de l'encodage classique (utf-8)
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        # Lecture de toutes les lignes dans le fichier filename
        for line in f:
            # generator yield pour retourner les élements de la liste ('Rockyou.txt' dans ce script)
            yield line.strip()

def verificationPassword(password):
    filename = "/home/callme_root/Documents/PythonProjet/code/wordlist.txt"
    # Vérifier si la liste existe
    if os.path.exists(filename):
        # 1ere vérification: si le mot de passe est dans la liste
        for mdp in load_passwords(filename):
            if mdp == password:
                end_time = time.time()
                time_taken = end_time - start_time
                print("Mot de passe trouvé: " + mdp + " en " + str(time_taken) + " secondes avec la méthode dictionnaire")
                raise SystemExit
        else:
                print("Mdp non trouvé avec le dictionnaire.")
    else:
        return "List unfoundable."

# Define the maximum password length to try
tailleMax = 6

# Track the start time of the password cracking process
start_time = time.time()

password = "mdp123"
print(verificationPassword(password))

chars = string.printable
# Try all possible combinations of characters up to max_length
for length in range(1, tailleMax + 1):
    for combination in itertools.product(chars, repeat=length):
        # Join the characters in the combination to form a password candidate
        candidate = "".join(combination)
        # Check if the candidate matches the password
        if candidate == password:
            # Track the end time of the password cracking process
            end_time = time.time()
            print("Mdp trouvé: ", candidate)
            # Calculate the time taken to crack the password
            time_taken = end_time - start_time
            print("Temps utilisé:", time_taken, "secondes avec la méthode brute force.")
            # Terminate the password cracking process
            raise SystemExit
