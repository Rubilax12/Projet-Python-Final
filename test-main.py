#Partie générer mdp aléatoire
import random
import math
import string

dictionnaire = "0123456789azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN.;,?:/!§*µù%$£=+)°]}à@ç^_è`-|(['{é~&¹²¬<>§Ä¢éÏÇ¼ÃçÜÉøúðØÐ¶"
taille1 = 4
taille2 = 8
taille3 = 16
taille4 = 32

mdp1 = ''.join(random.choices(dictionnaire, k=taille1))
mdp2 = ''.join(random.choices(dictionnaire, k=taille2))
mdp3 = ''.join(random.choices(dictionnaire, k=taille3))
mdp4 = ''.join(random.choices(dictionnaire, k=taille4))

print(f"Votre mot de passe de {len(mdp1)} est {mdp1}")
print(f"Votre mot de passe de {len(mdp2)} est {mdp2}")
print(f"Votre mot de passe de {len(mdp3)} est {mdp3}")
print(f"Votre mot de passe de {len(mdp4)} est {mdp4}")


