def caesar(program):
    def encrypt(original_text, shift_amount):
        output = []
        final = ""
        for letter in original_text:
            if letter not in alphabet:
                output.append(letter)
            else:
                index = alphabet.index(letter) + shift_amount
                index = index % len(alphabet)
                output.append(alphabet[index])
        print(f"Your encrypted word/sentence is: {final.join(output)}")

    def decrypt(encrypted_text, shift_amount):
        output = []
        final = ""
        for letter in encrypted_text:
            if letter not in alphabet:
                output.append(letter)
            else:
                index = alphabet.index(letter) - shift_amount
                index = index % len(alphabet)
                output.append(alphabet[index])
        print(f"Your decrypted word/sentence is: {final.join(output)}")

    if program == "encode":
        encrypt(text, shift)
    elif program == "decode":
        decrypt(text, shift)
    else:
        print("Please type a 'encode' or 'decode' correctly")
