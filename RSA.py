def car_to_fig(message):
    alphabet = {'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06', 'G': '07', 'H': '08', 'I': '09', 'J': '10','K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20', 'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26', 'a': '27', 'b': '28', 'c': '29', 'd': '30', 'e': '31', 'f': '32', 'g': '33', 'h': '34', 'i': '35', 'j': '36', 'k': '37', 'l': '38', 'm': '39', 'n': '40', 'o': '41', 'p': '42', 'q': '43', 'r': '44', 's': '45', 't': '46', 'u': '47', 'v': '48', 'w': '49', 'x': '50', 'y': '51', 'z': '52'}
    chiffres = []
    for char in message:
        if char in alphabet:
            chiffres.append(alphabet[char])
    return ''.join(chiffres)

def fig_to_car(message):
    alphabet = {'01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E', '06': 'F', '07': 'G', '08': 'H', '09': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z', '27': 'a', '28': 'b', '29': 'c', '30': 'd', '31': 'e', '32': 'f', '33': 'g', '34': 'h', '35': 'i', '36': 'j', '37': 'k', '38': 'l', '39': 'm', '40': 'n', '41': 'o', '42': 'p', '43': 'q', '44': 'r', '45': 's', '46': 't', '47': 'u', '48': 'v', '49': 'w', '50': 'x', '51': 'y', '52': 'z'}
    result = ''
    for i in range(0, len(message), 2):
        bloc = message[i:i+2]
        if bloc in alphabet:
            result += alphabet[bloc]
    return result

def chiffrement(suite_chiffres, n, e):
    numbers_encrypted = []
    for bloc in suite_chiffres:
        entier = int(bloc)
        number_encrypted = (entier**e) % n
        numbers_encrypted.append(number_encrypted)
    return numbers_encrypted


def dechiffrement(message_chiffre, p, q, n, e):
    d = pow(e, -1, (p-1) * (q-1))
    numbers_decrypted = []
    for bloc_number in message_chiffre:
        number_decrypted = pow(bloc_number, d, n)
        numbers_decrypted.append(str(number_decrypted))
    return ''.join(numbers_decrypted)

original = "Bonjour"
p, q, e, n = 53, 97, 7, 5141
print(original)
original_numbers = car_to_fig(original)
print(original_numbers)
crypted = chiffrement(original_numbers, n, e)
print(crypted)
decrypted = dechiffrement(crypted, p, q, n, e)
print(decrypted)
original_decrypted = fig_to_car(decrypted)
print(original_decrypted)