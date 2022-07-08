import hashlib

while True:
    try:
        # on saisie le nom du fichier où se trouve tous les mdp
        wordlist = input("Entre le fichier contenant des mots de passe : (.txt) ")
        # on ouvre et lis le fichier des mdp
        wordlist = open(wordlist, "r")
        # on entre le hash qu'on veux essayer de "convertir" en mdp
        hash = input("Entre le hash du mot de passe à retrouver : ")
        # si ya pas d'erreu on sort du try et du except sinon on rentre dans le except
        break
    except:
        print("Pas de fichier portant ce nom ! \n")

# on va lire chaque ligne du fichier
for word in wordlist.readlines():
    # .strip permet de faire un saut de ligne après chaque lecture de mot dans le fichier sinon les hashs on être a la suite
    word = word.strip('\n').encode("utf-8")
    # on hash en sha256 le mot dans le fichier
    wordlist_hash = hashlib.sha256(word).hexdigest()

    # si le hash de base correspond au hash d'un mot du fichier alors mot de passe trouvé
    if (hash == wordlist_hash):
        print("\nMot de passe trouvé.\nLe mot de passe est : " + str(word) + "\n")
        # des qu'on a trouvé le mdp on arrete tout
        break
    else:
        print("Mot de passe non trouvé")