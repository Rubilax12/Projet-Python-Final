import socket #Librairie connexion socket
import itertools #Librairie pour combinaisons BF
import string #Librairie pour caractères
import time #Librairie pour le temps

def brute_force_password(password_length):
    characters = string.ascii_letters + string.digits + string.punctuation #Déf de l'alphabet
    attempts = 0
    for attempt in itertools.product(characters, repeat=password_length):#Tester les combinaisons en fct de l'alphabet + taille
        attempts += 1
        current_attempt = ''.join(attempt) #Concatène les caractères séparément pour avoir un seul bloc
        yield current_attempt, attempts #return

def crack_password(host, port, password_length):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs: #Ouvre socket client
        cs.connect((host, port))#S'y connecte avec port + host
        
        print("Début: ")
        
        start_time = time.time()
        for attempt, attempts_made in brute_force_password(password_length):
           cs.sendall(attempt.encode())
           response = cs.recv(1024).decode()
           if response == "True":
                end_time = time.time()
                time_taken = end_time - start_time
                print(f"Password trouvé: {attempt}")
                print(f"Temps utilisé: {time_taken:.5f} secondes")
                print(f"Nombre de tentatives: {attempts_made}")
                break
        if response == "F":
            print("Aucun mot de passe trouvé. Est-ce la bonne taille mis en paramètre ?")

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Adresse IP du serveur
    PORT = 60002        # Port à écouter
    PASSWORD_LENGTH = 4  # Longueur du mot de passe à brute forcer
    crack_password(HOST, PORT, PASSWORD_LENGTH)
