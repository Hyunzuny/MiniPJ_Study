from art import logo8
print(logo8)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# type = input('e or d: \n' )
# massage = input('메세지를 입력하세요.: \n')
# amount = input('얼마나 이동하시겠습니까?: \n')
# massage = 'aaaa111'  #cccdd 26
# amount = 7
# amount = amount % 26 
# hello - cjgqj - holvo
def cyper(type_, massage_, amount_):
    if type_ == 'd':
        amount_ *= -1
    result = ''

    for i in massage_:
        if i in alphabet:
            now_amount = alphabet.index(i)
            new_amount = now_amount + amount_
            new_alphabet = alphabet[new_amount]
            result += new_alphabet
        else:
            result += i
        
    print(result)

end_game = True
while end_game:    
    type = input('e or d: \n' )
    massage = input('메세지를 입력하세요.: \n')
    amount = int(input('얼마나 이동하시겠습니까?: \n'))
    amount = amount % 26
    
    cyper(type_=type, massage_=massage, amount_=amount)
    ask = input('뒤에 사람이 있습니까? y or n: \n')
    if ask == 'n':
        end_game = False
        print('잘가세요')
        
        
        
