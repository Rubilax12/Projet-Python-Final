#client.py
#socket = point de connexion (bidirectionnel) entre 2 machines

import socket
import time
import itertools
import string


HOST = "127.0.0.1"  # adresse IP ou hostname (ici localhost)
PORT = 65432  # port utilisé
PASSWORD_FILE = "password.txt"  # Nom du fichier contenant le mot de passe
password = None
chars = string.printable

# Fonction pour vérifier le mot de passe

with open(PASSWORD_FILE, "r") as f:
    password = f.read().strip()

# Define the maximum password length to try
tailleMax = 6



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #création d'un socket TCP
    s.connect((HOST, PORT)) #connexion avec le port & host mentionné plus haut
    #s.sendall(b"Hello world!") #envoi des données vers le serveur
    data = s.recv(1024) #attente de la réponse

    # Track the start time of the password cracking process
print("Début: ")
start_time = time.time()

# Try all possible combinations of characters up to max_length
for length in range(1, tailleMax + 1):
    for combination in itertools.product(chars, repeat=length):
        # Join the characters in the combination to form a password candidate
        candidate = "".join(combination)
        # Check if the candidate matches the password
        if candidate == password:
            # Track the end time of the password cracking process
            end_time = time.time()
            print("Password found:", candidate)
            # Calculate the time taken to crack the password
            time_taken = end_time - start_time
            print("Time taken:", time_taken, "seconds")
            # Terminate the password cracking process
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(candidate.encode())
                # Receive response from server
                data = s.recv(1024)
                print("Received from server:", data.decode())
            raise SystemExit

print("Mdp non trouvé, mission failed!")
