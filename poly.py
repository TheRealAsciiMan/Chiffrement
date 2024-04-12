PREM_CARAC = ord('A') - 1
DER_CARAC = ord('Z')
#PREM_CARAC = 32
#DER_CARAC = 126
#PREM_CARAC = 0x21
#DER_CARAC = 0x1f0df
MODULO = DER_CARAC - PREM_CARAC

def codage_cle_chiffrement(chaine_a_coder, cle):

    chaine_chiffree = ""
    i = 0
    for car in chaine_a_coder :
        if car != " ":
            ord_car = ord(car) - PREM_CARAC
            ord_cle = ord(cle[i%len(cle)]) - PREM_CARAC
            sum_ord = ord_car + ord_cle
            #print(f"car : {car} - ord_car : {ord_car} - ord_cle : {ord_cle} - sum_ord : {sum_ord} - ")
            if sum_ord <= MODULO :
                car2 = chr(PREM_CARAC + sum_ord)
            else :
                car2 = chr(PREM_CARAC + sum_ord%MODULO)
            i += 1
        else :
            car2 = car
        chaine_chiffree += car2
    return chaine_chiffree

def car_to_num(c):
    return ord(c) - PREM_CARAC

def num_to_car(n):
    if n <= MODULO :
        return chr(PREM_CARAC + n)
    else :
        return chr(PREM_CARAC + n%MODULO)

def codage_cle_chiffrement2(chaine_a_coder, cle):
    chaine_chiffree = ""
    i = 0
    for car in chaine_a_coder :
        if car != " ":
            ord_car = car_to_num(car)
            ord_cle = car_to_num(cle[i%len(cle)])
            sum_ord = ord_car + ord_cle
            #print(f"car : {car} - ord_car : {ord_car} - ord_cle : {ord_cle} - sum_ord : {sum_ord} - ")
            car2 = num_to_car(sum_ord)
            i += 1
        else :
            car2 = car
        chaine_chiffree += car2
    return chaine_chiffree

def decodage_cle_chiffrement(chaine_codee, cle):
    chaine_clair = ""
    i = 0
    for car in chaine_codee :
        if car != " ":
            ord_car = ord(car) - PREM_CARAC
            ord_cle = ord(cle[i%len(cle)]) - PREM_CARAC
            sum_ord = ord_car - ord_cle + MODULO
            #print(f"car : {car} - ord_car : {ord_car} - ord_cle : {ord_cle} - sum_ord : {sum_ord} - ")
            if sum_ord <= MODULO :
                car2 = chr(PREM_CARAC + sum_ord)
            else :
                car2 = chr(PREM_CARAC + sum_ord%MODULO)
            i += 1
        else :
            car2 = car
        chaine_clair += car2
    return chaine_clair