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


def text_to_bin_encoded(message, cle):
    cle = cle * (len(message) // len(cle)) + cle[:len(message) % len(cle)]
    resultat = ""
    for i in range(len(message)):
        ascii_message = ord(message[i])
        ascii_cle = ord(cle[i])
        binaire_message = format(ascii_message, '08b')
        binaire_cle = format(ascii_cle, '08b')
        for j in range(8):
            resultat += str(int(binaire_message[j]) ^ int(binaire_cle[j]))
    return resultat

def bin_encoded_to_text(message, cle):
    cle_binary = ""
    for i in range(len(cle)):
        ascii_cle = ord(cle[i])
        binaire_cle = format(ascii_cle, '08b')
        cle_binary += str(binaire_cle)
    cle_binary = cle_binary * (len(message) // len(cle)) + cle_binary[:len(message) % len(cle)]
    resultat = ""
    for i in range(0, len(message), 8):
        octet_message = message[i:i+8]
        octet_cle = cle_binary[i:i+8]
        result_binary = ""
        for j in range(8):
            result_binary += str(int(octet_message[j]) ^ int(octet_cle[j]))
        ascii_message = chr(int(result_binary, 2))
        resultat += ascii_message
    return resultat


original = "https://www.speedrun.com/AsciiMan"
print(original)
key = "LUL"
result = codage_binaire(original, key)
print(result)
disc_original = codage_binaire(result, key)
print(disc_original)

original = "https://www.speedrun.com/AsciiMan"
print("\n"+original)
key = "LUL"
result = text_to_bin_encoded(original, key)
print(result)
disc_original = bin_encoded_to_text(result, key)
print(disc_original)