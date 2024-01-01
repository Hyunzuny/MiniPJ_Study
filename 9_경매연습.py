

# name = input('이름이 뭐니?\n')
# money = input('얼마를 입찰할거니?: \n$')
# ask = input('더 할거니? y or n:\n')

# name = '현준'
# money = 321
# ask  = 'y'

# result = {'현준': 123, '지은': 321}

def  win(result):
    n = 0
    for key in result: #{'현준': 123, '지은': 321}
        num = result[key] # 123
        if num > n:
            n = num
    print(f'이긴사람은 {key}이고 금액은 ${n} 이다.')
    


result = {}
game = True
while game:
    name = input('이름이 뭐니?\n')
    money = int(input('얼마를 입찰할거니?: \n$'))
    result[name] = money
    ask = input('더 할거니? y or n:\n')
    if ask =='n':
        game = False
        win(result)
        #승자는 ~고 ~입찰했다.
        print()
    

