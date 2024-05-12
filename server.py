#server.py

import socket
import string
import random

HOST = "127.0.0.1"  #addresse IP ou hostname utilisé (ici localhost)
PORT = 65432  # Port d'écoute

# Génération du mot de passe aléatoire
def generate_random_password(length=2):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Stockage du mot de passe aléatoire dans un fichier texte
def store_password(password):
    with open("password.txt", "w") as f:
        f.write(password)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Création d'un socket
    s.bind((HOST, PORT)) #associe l'IP & le port
    s.listen() #Ecoute
    print(f"Serveur à l'écoute sur le port {PORT}")
    

    # Génération du mot de passe aléatoire
    random_password = generate_random_password()
    print(f"Mot de passe aléatoire généré : {random_password} à flouter ?") #A FLOUTER ?

    # Stockage du mot de passe aléatoire dans un fichier
    store_password(random_password)
    print("Mot de passe aléatoire stocké dans le fichier 'password.txt'")

    while True:
        conn, addr = s.accept() #Attente d'une connexion
        print(f"Connected by {addr}") # Affiche l'adresse du client une fois la connexion établie
    
        with conn: #Une fois la connexion établie éxecute ce code:
            while True:
                data = conn.recv(1024)
                if data == store_password:
                    print("test")
                if not data:
                    print("Fin de la transmission de données.")
                    break
                print(f"Données reçues: {data}") # Affiche les données reçues
                conn.sendall(data)
