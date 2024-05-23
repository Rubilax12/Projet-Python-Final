import socket #Librairie socket 
import random #Librairie mdp aléatoire
import string #caractère


def generate_password(length=4):
    characters = string.ascii_letters + string.digits + string.punctuation #Déf de l'aphabet
    return ''.join(random.choice(characters) for _ in range(length)) #return le mdp aléatoire

def start_server(host, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:#server.socket
        ss.bind((host, port))#Se connecte sur port + host
        ss.listen()#Ecoute
        print(f"Serveur en écoute sur: {host}:{port}")
        client_socket, client_address = ss.accept()
        with client_socket as cs:#client.socket
            print(f"Connection en provenance de: {client_address}")
            password = generate_password()
            print(f"Mdp à trouver: {password}")
            while True:
                response = cs.recv(1024).decode()
                if response == password:
                    cs.sendall("True".encode())
                    print(f"Mot de passe trouvé. {password}")
                    break
                else:
                    cs.sendall("F".encode())#F pour false
        
        client_socket.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Adresse IP du serveur
    PORT = 60002        # Port à écouter
    start_server(HOST, PORT)
