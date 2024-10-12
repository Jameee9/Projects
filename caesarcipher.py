alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stop = False

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

print(r'''

 ______   ________   ______   ______   ________   ______        ______    ________  ______   ___   ___   ______   ______       
/_____/\ /_______/\ /_____/\ /_____/\ /_______/\ /_____/\      /_____/\  /_______/\/_____/\ /__/\ /__/\ /_____/\ /_____/\      
\:::__\/ \::: _  \ \\::::_\/_\::::_\/_\::: _  \ \\:::_ \ \     \:::__\/  \__.::._\/\:::_ \ \\::\ \\  \ \\::::_\/_\:::_ \ \     
 \:\ \  __\::(_)  \ \\:\/___/\\:\/___/\\::(_)  \ \\:(_) ) )_    \:\ \  __   \::\ \  \:(_) \ \\::\/_\ .\ \\:\/___/\\:(_) ) )_   
  \:\ \/_/\\:: __  \ \\::___\/_\_::._\:\\:: __  \ \\: __ `\ \    \:\ \/_/\  _\::\ \__\: ___\/ \:: ___::\ \\::___\/_\: __ `\ \  
   \:\_\ \ \\:.\ \  \ \\:\____/\ /____\:\\:.\ \  \ \\ \ `\ \ \    \:\_\ \ \/__\::\__/\\ \ \    \: \ \\::\ \\:\____/\\ \ `\ \ \ 
    \_____\/ \__\/\__\/ \_____\/ \_____\/ \__\/\__\/ \_\/ \_\/     \_____\/\________\/ \_\/     \__\/ \::\/ \_____\/ \_\/ \_\/ 
                                                                                                                               

''')

while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction)
    exit_program = input("Do you wish to exit the program? If no, It will start over. [y/n]\n").lower()
    if exit_program == "y":
        stop = True
        print(r'''Alrighty then, Keep your secrets
(•_•)
( •_•)>⌐■-■ 
(⌐■_■)
''')
