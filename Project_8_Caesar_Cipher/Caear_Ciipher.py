#Caesar Cipher 
import art_caesar_cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
length_of_alphabet = len(alphabet)

def take_inputs():
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    if action == "encode" or action == "decode":
        message = input("Type your message:\n").lower()
        shift_num = int(input("Type the shift number:\n"))
        #here, some work can also be done to handle cases when a user inputs a non-numeric value in shift_num.
        #I'll do it after I study the chapter about handling exceptions/errors
    else:
        print("Please type a valid option\n")
        action, message, shift_num = take_inputs()
    return action, message, shift_num
        

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount = length_of_alphabet - shift_amount
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % length_of_alphabet
            end_text += alphabet[new_position]
    
    print(f"The {cipher_direction}d text is {end_text}")
    

print(art_caesar_cipher.logo)

repeat = True
while repeat:
    
    direction, text, shift = take_inputs()
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    prompt = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    
    if prompt == "no":
        print("Goodbye")
        repeat = False



