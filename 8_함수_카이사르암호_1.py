alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# encode
def encrypt(plain_text, shift_amount):
    result = ''
                
    for i in plain_text:
        position = alphabet.index(i)
        new_position = position + shift_amount
        new_alphabet = alphabet[new_position]
        result += new_alphabet
        if new_position > len(alphabet):
            alphabet*alphabet

    print(f"The encoded text is {result}")      
        
   
def decrypt(cipher_text, shift_amount):
    result=''        
    for i in cipher_text:
        position = alphabet.index(i)
        new_position = position - shift_amount
        new_alphabet = alphabet[new_position]
        result += new_alphabet
                
    print(f'The decoded text is {result}')


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
    
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print('잘못 입력 하셧습니다.')
        


# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = 'hello'
# shift = 5
# #decode

    
# def decrypt(plain_text, shift_amount):
#     result = ''   
#     for i in plain_text:
#         position = alphabet.index(i)
#         new_position = position - shift_amount
#         new_alphabet = alphabet[new_position]
#         result += new_alphabet
    
#     print(result)
        
# decrypt(plain_text=text, shift_amount=shift)
         

        

        
