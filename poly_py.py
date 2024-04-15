def codage_binaire(message, cle):
    cle = cle * (len(message) // len(cle)) + cle[:len(message) % len(cle)]
    resultat = ""
    for i in range(len(message)):
        ascii_message = ord(message[i])
        ascii_cle = ord(cle[i])
        binaire_message = format(ascii_message, '08b')
        binaire_cle = format(ascii_cle, '08b')
        resultat_binaire = ""
        for j in range(8):
            resultat_binaire += str(int(binaire_message[j]) ^ int(binaire_cle[j]))
        resultat += chr(int(resultat_binaire, 2))
    return resultat


original = "Bonjour !"
print(original)
key = "LUL"
result = codage_binaire(original, key)
print(result)
disc_original = codage_binaire(result, key)
print(disc_original)