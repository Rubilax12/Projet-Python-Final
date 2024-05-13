from flask import Flask, jsonify
import random
import string

app = Flask(__name__) # nécessaire pour créer une application Flask

def generate_password(length=4): #génère un mdp aléatoire
    chars = string.ascii_letters + string.digits #ascii_letters et digits : mdp alphanumérique
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/") #racine
def get_password(): #génère un mot de passe et renvoie une réponse json
    password = generate_password()
    return jsonify(password=password)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    #démarre le serveur sur toutes les interfaces réseau disponibles