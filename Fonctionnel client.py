import socket
import time
import itertools
import string

HOST = "127.0.0.1"  
PORT = 65430  
PASSWORD_FILE = "password.txt"  
chars = string.printable

# Define the maximum password length to try
tailleMax = 4
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        

        print("Début du BruteForce: ")
        start_time = time.time()#Lancement du chronomètre

        with open(PASSWORD_FILE, "r") as f:#Ouvre le fichier ou le mdp aléatoire est stocké
            for password in f:
                password = password.strip()#Supprime les retours chariots (sauts de ligne)
                for length in range(1, tailleMax + 1):#itère de 1 à TailleMax + 1
                    for combination in itertools.product(chars, repeat=length):#Génére toutes les combinaisons possibles
                        candidate = "".join(combination)#Créer une chaine de caractères
                        if candidate == password:#Si le mdp est trouvé alors:
                            end_time = time.time()#Nouvelle déclaration du temps
                            print("Mdp trouvé:", candidate)#Affichage du mdp
                            time_taken = end_time - start_time
                            print("Temps utilisé:", time_taken, "secondes")#Affichage du temps
                            s.sendall(candidate.encode())#converti candidate en byte puis l'envoie au serveur
                            response = s.recv(1024)#réponse du serveur
                            print("Reçu du serveur:", response)#affichage de la réponse (décodage)
                            break
                else:
                    print("Mdp non trouvé, mission failed!")

except Exception as e:
    print("Erreur de connexion au serveur.", e)
