#Caesar Cipher : My Attempt

def shift(char, num):
    alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    length = len(alphas)
    
    for position in range(length):
        if alphas[position] == char:
            shift = (position + num) % length
            return alphas[shift]


def encode(message, num):
    encode = ''
    for char in message:
        if char not in alphabet:
            encode += char
        else:
            encode += shift(char, num)
    return encode

def decode(message, num):
    decode = ''
    num = 26 - num
    for char in message:
        if char not in alphabet:
            decode += char
        else:
            decode += shift(char, num)
    return decode

def take_inputs():
    message = input("Type your message (in just alphabets and no spaces):\n").lower()
    num = int(input("Type the shift number:\n"))
    return message, num

def action():
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    
    if choice == "encode":
        message_to_encrypt, num = take_inputs()
        encode_result = encode(message_to_encrypt, num)
        print(f"Here's the encoded result:  {encode_result}")
        
    elif choice == "decode":
        message_to_decrypt, num = take_inputs()
        decode_result = decode(message_to_decrypt, num)
        print(f"Here's the decoded result:  {decode_result}")
    
    else:
        print("Please type a valid answer.\n")
        action()
        
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    if repeat == "yes":
        action()
    else:
        return None
    

action()


