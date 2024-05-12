import socket
import string
import random

HOST = "127.0.0.1"  #localhost
PORT = 65438  #port à utiliser > 1023

def generate_random_password(length=8):#Fct pour générer mdp aléatoire (avec lenght = taille)
    characters = ''.join(filter(lambda x: x not in [' ', '\n', '\t'], string.printable))
    return ''.join(random.choice(characters) for _ in range(length))#Créer un mdp aléatoire à partir des characters définis en amont

def store_password(password):#Fct stockage password
    with open("password.txt", "w") as f:#Dans le fichier password.txt
        f.write(password)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#Ouvre un socket
    s.bind((HOST, PORT))#Lie le socket à un host & un port
    s.listen()#Ecoute
    print(f"Serveur à l'écoute sur le port: {PORT}")

    random_password = generate_random_password()#Mdp générer à chaque lancement du pgrm
    print("Mot de passe aléatoire généré: ********") # amélioration -> étoile dynamique en fct de length
    store_password(random_password)#Rempli le fichier txt
    print("Mot de passe aléatoire stocké dans le fichier: 'password.txt'")

    conn, addr = s.accept()#accepter connexion d'un client
    print(f"Connecté à {addr}")#afficher qui s'est connecté
   

    with conn:#Créer un bloc (qui permettra de garantir la fermeture du socket)
        while True:#Boucle infinie (tant qu'il y a un client)
            data = conn.recv(1024)#Reçoit les données du client et les stocke dans la variable data
            if data == random_password.encode():#compare data (données client) au mdp généré plus tôt (qu'on a encodé en byte car data est sous forme de byte)
                print(f"Mot de passe correct: {data}. Fermeture du serveur.")#Affichage de ce qu'a envoyer le client
                password_found = True
                break#Fermeture du socket
            else:
                print(f"Mot de passe incorrect. Données reçues: {data}. Fermeture du serveur.")#Affichage de l'envoi du client
                break #fermeture socket


        
