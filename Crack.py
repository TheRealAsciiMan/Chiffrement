from urllib.request import urlretrieve

PREM_CARAC = 0x21
DER_CARAC = 0x1f0df
MODULO = DER_CARAC - PREM_CARAC


def rotX(texte, decalage):
    texte_chiffre = ""
    for lettre in texte:
        if ord(lettre) > PREM_CARAC and ord(lettre) < DER_CARAC:
            ordre_dans_alphabet = ord(lettre) - PREM_CARAC + decalage
            texte_chiffre += chr(ordre_dans_alphabet % MODULO + PREM_CARAC)
        else:
            texte_chiffre += lettre
    return texte_chiffre


def recuperer_texte_etalon():
    # url_mousq = "https://www.gutenberg.org/cache/epub/13951/pg13951.txt"
    url_mousq = "http://ninoo.fr/LC/Term_NSI/seq15_securisation_communications/mousq.txt"
    urlretrieve(url_mousq, 'mousq.txt')


def stat(un_fichier_etalon):
    def occurence(chaine, caractere):
        n = 0
        for i in chaine:
            if i == caractere:
                n += 1
        return n

    liste_occurences = []
    with open(un_fichier_etalon, 'r') as f:
        ligne = f.read()
        lettres_deja_analysees = []
        for car in ligne:
            if car not in lettres_deja_analysees:
                lettres_deja_analysees.append(car)
                nbre_occurence = occurence(ligne, car)
                liste_occurences.append((car, nbre_occurence))
    liste_occurences.sort(key=lambda e: e[1], reverse=True)
    return liste_occurences


def stat2(un_fichier_etalon):
    dico_occurences = {}
    with open(un_fichier_etalon, 'r') as f:
        ligne = f.read()
        for car in ligne:
            if car not in dico_occurences:
                dico_occurences[car] = 0
            dico_occurences[car] += 1
    liste_occurences = list(dico_occurences.items())
    liste_occurences.sort(key=lambda x: x[1], reverse=True)
    lst_sans_ocurrences = []
    for i, j in liste_occurences:
        lst_sans_ocurrences.append(i)
    return lst_sans_ocurrences


def remplace(origine: str, etalon: str) -> str:
    freq_etalon = stat2(etalon)
    # print(freq_etalon)
    freq_origine = stat2(origine)
    # print(freq_origine)
    decode = ""
    with open(origine, 'r') as f:
        ligne = f.read()
        for car in ligne:
            # print(car)
            position = freq_origine.index(car)
            decode += freq_etalon[position]
    return decode


def remplace2(origine: str, etalon: str) -> str:
    freq_etalon = stat2(etalon)
    print(freq_etalon)
    freq_origine = stat2(origine)
    print(freq_origine)
    decalage = ord(freq_origine[1]) - ord(freq_etalon[1])
    decode = ""
    with open(origine, 'r') as f:
        ligne = f.read()
        chaine = rotX(ligne, -decalage)
        decode += chaine
    return decode


ma_liste_codee = stat('rotXcrypte.txt')
print(ma_liste_codee)

# PROGRAMME PRINCIPAL
print("### DEBUT PROGRAMME P. 274 ex 8 ###")
print("ROT47")
message = "Bonjour le monde !"
code = rotX(message, 47)
print(f'Le codage en ROT 47 de "{message}" est : "{code}"')
code2 = rotX(code, 47)
print(f'Le décodage se fait aussi avec ROT 47. Le décodage de : "{code}" est : "{code2}"')

# Analyse de fréquence
# ma_liste = stat('mousq.txt')
# print("Analyse avec la fonction stat : ", ma_liste, '\n ############### \n')
# ma_liste2 = stat2('rotXcrypte.txt')
# print("Analyse avec la fonction stat2 : ", ma_liste2, '\n ############### \n')

# Décodage par analyse de fréquence
print("Décoadage par analyse de fréquence.")
message_decode = remplace('rotXcrypte.txt', 'mousq.txt')
print(message_decode)

# Décodage par analyse de fréquence + décalage
print("Décoadage par analyse de fréquence et décalage.")
message_decode = remplace2('rotXcrypte.txt', 'mousq.txt')
print(message_decode)

print("### FIN   PROGRAMME P. 274 ex 8 ###")