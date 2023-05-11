def crypto(message, key): 
    key_codes=[ord(letter) for letter in key]
    encrypted=''

    for i, letter in enumerate(message): 
        letter_code=ord(letter)
        key_code=key_codes[i % len(key_codes)]
        encrypted_code=(letter_code + key_code)%128
        encrypted_letter=chr(encrypted_code)
        print(encrypted_letter, encrypted_code)

        encrypted += encrypted_letter
      
    return encrypted

def de_crypto(message, key): 
    key_codes=[ord(letter) for letter in key]
    de_encrypted=''

    for j, letter in enumerate(message): 
        letter_code=ord(letter)
        key_code=key_codes[j % len(key_codes)]
        de_encrypted_code=(letter_code - key_code)%128
        de_encrypted_letter=chr(de_encrypted_code)
        print(de_encrypted_letter, de_encrypted_code)

        de_encrypted += de_encrypted_letter
      
    return de_encrypted


action=int(input('0 per cryptare, 1 per decryptare'))

message=input()
key=input()

if action ==0: 
    encrypted=crypto(message, key)
    print(encrypted)
else:
    de_encrypted=de_crypto(message, key)
    print(de_encrypted)

