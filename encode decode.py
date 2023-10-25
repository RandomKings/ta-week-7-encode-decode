alphabet_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}


def encode(word, key):
    numWord = []

    for i in range(len(word)):
        char = word[i]
        if alphabet_dict.get(char) is not None:
            char_value = alphabet_dict[char]

            key_digit = int(key[i % len(key)])

            encoded_char = (char_value + key_digit) 
       
            numWord.append(encoded_char)
        else:
            print(f"'{char}' doesn't exist in the dictionary")

    return numWord

word = input("Enter your string: ")
key = input("Enter your key: ")

def decode(encoded, key):
    decoded_word = ""
    for i in range(len(encoded)):

        char_val = encoded[i]

        key_digit = int(key[i % len(key)])

        decoded_char = char_val - key_digit
        
        for k, v in alphabet_dict.items():
            if v == decoded_char:

                decoded_word += k

    return decoded_word

                



if int(key) > 0:
    encrypted_word = (encode(word,key))

    decode_w = decode(encrypted_word,key)

    print("the encrypted word in a list is :" ,encrypted_word ,"the decoded word is: " + decode_w + " using the key: " + key)


