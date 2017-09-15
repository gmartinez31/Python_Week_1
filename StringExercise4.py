word = raw_input("Say a sentence! ").upper()

word = word.replace('A', '4')
word = word.replace('E', '3')
word = word.replace('G', '6')
word = word.replace('I', '1')
word = word.replace('O', '0')
word = word.replace('S', '5')
word = word.replace('T', '7')

print word

#Caesar Cipher
crypt = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
# secret = "hello"
alphabet = 'abcdefghijklmnopqrstuvwxyz'
decrypted = ''

for x in crypt:
    ascii_code = ord(x)
    is_uppercase = ascii_code >= 65 and ascii_code <= 90
    x = x.lower()
    if x not in alphabet:
        new_char = x
    else:
        idx = alphabet.find(x)
        new_idx = idx + 13
        if new_idx > 25:
            new_idx = new_idx - 26
        new_char = alphabet[new_idx]
        if is_uppercase:
            new_char = new_char.upper()
    decrypted += new_char

print(decrypted)
