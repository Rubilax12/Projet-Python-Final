import socket
import time
import itertools
import string

HOST = "127.0.0.1"  #localhost
PORT = 65438  #port > 1023 (privilégié)
PASSWORD_FILE = "password.txt"  
chars = ''.join(filter(lambda x: x not in [' ', '\n', '\t'], string.printable)) #On peut pousser le vice avec les caractères latins mais on ne l'a pas fait

# Taille max à tester (cohérent avec taille du mdp généré)
tailleMax = 8
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#Ouvre un socket
        s.connect((HOST, PORT))#Lie le socket à un host & un port
        

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
                            break
            if candidate != password:
                end_time = time.time()#Nouveau chrono
                time_taken = end_time - start_time
                print(f"Mdp non trouvé, mission échouée! Temps perdu: {time_taken} sec.")

except Exception as e: #Permet de savoir si l'erreur vient de la connexion serveur ou non
    print("Erreur de connexion au serveur.", e)
