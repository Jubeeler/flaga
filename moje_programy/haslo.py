def gen_hasla():

    import string
    import random


    il_znakow = random.randrange(8,21)

    if int(il_znakow) <8:
        print("za malo")
        exit()


    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    specznaki = string.punctuation
    liczby = string.digits
    wszystkie_znaki = lowercase + uppercase +specznaki +liczby

    haslo =random.sample(lowercase,2)+random.sample(uppercase,2)+ \
    random.sample(specznaki,2)+random.sample(liczby,2)

    dodatkowe_znaki =''

    if int(il_znakow) >8:
        roznica = int(il_znakow) - 8
        dodatkowe_znaki = random.sample(wszystkie_znaki,roznica)

    haslo = haslo + dodatkowe_znaki
    random.shuffle(haslo)    

    gotowe_haslo = ''.join(haslo)
    
    return gotowe_haslo
            
