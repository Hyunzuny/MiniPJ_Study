print('롤러코스터에 오신것을 환영합니다.')
height = int(input('키가 몇이십니까?'))
bill = 0

if height > 120:
    print('어서오세요')
    age = int(input('나이가 어떻게 되세요?'))
    if age < 12:
        bill = 5
        print('%s$ 받겠습니다.' %bill)
    elif age <= 18:
        bill = 7
        print('%s$ 받겠습니다.' %bill)
    else:
        bill = 12
        print('%s$ 받겠습니다.' %bill)
        
        
    pic = input('사진 찍으시겠습니까? Y or N: ')
    if pic == 'y':
        bill += 3
    print('총 내실 금액은 %s$ 입니다.' %bill)
         
else:
    print('입장 못하십니다.')
    

    