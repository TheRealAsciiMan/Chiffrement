def code_cesar(texte, decalage):
    """
    Fonction qui code un texte suivant la méthode de césar (chaque lettre est
    décalé).
    Arguments ::
        - texte : message à coder de type str
        - decalage : indice de décalage de type int
    Renvoie ::
        - texte_chiffre : le message codé de type str
    >>> code_cesar("VENI, VIDI, DICI", 3)
    YHQL, YLGL, GLFL
    """
    texte_chiffre = ""
    for lettre in texte :
        if lettre in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                      'O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            ordre_dans_alphabet = ord(lettre)+decalage-ord('A')
            texte_chiffre += chr(ordre_dans_alphabet%26+ord('A'))
        else:
            texte_chiffre += lettre
    return texte_chiffre

def code_cesar2(texte, decalage):
    """
    Fonction qui code un texte suivant la méthode de césar (chaque lettre est
    décalé).
    Variante proposée par C. Veillon
    Arguments ::
        - texte : message à coder de type str
        - decalage : indice de décalage de type int
    Renvoie ::
        - texte_chiffre : le message codé de type str
    >>> code_cesar("VENI, VIDI, DICI", 3)
    YHQL, YLGL, GLFL
    """
    texte_chiffre = ""
    liste_avec_lettres = []
    for i in range(65, 91):
        liste_avec_lettres.append(chr(i))
    #print(liste_avec_lettres)
    for lettre in texte :
        if lettre in liste_avec_lettres:
            for i in range(len(liste_avec_lettres)):
                if lettre == liste_avec_lettres[i]:
                    texte_chiffre += liste_avec_lettres[(i+decalage)%26]
        else :
            texte_chiffre += lettre
    return texte_chiffre

def decode_cesar(texte, decalage):
    """
    Fonction qui décode un texte suivant la méthode de césar.
    Arguments ::
        - texte : message codé de type str
        - decalage : indice de décalage de type int
    Renvoie ::
        - le message décodé de type str
    >>> code_cesar("YHQL, YLGL, GLFL", 3)
    VENI, VIDI, DICI
    """
    return code_cesar(texte, -decalage)