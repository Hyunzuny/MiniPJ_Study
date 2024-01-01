print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0
input('What size pizza do you want? S, M, or L: ')
if size =='s':
    bill += 15
    print(f'{bill}$ 받았습니다.')
    
    input('Do you want pepperoni? Y or N ')
    if add_pepperoni == 'y':
        bill += 2
        print(f'{bill}$ 받았습니다.')
        
elif size == 'm':
    bill += 20
    print(f'{bill}$ 받았습니다.')
    
    input('Do you want pepperoni? Y or N ')
    if add_pepperoni == 'y':
        bill +=3
        print(f'{bill}$ 받았습니다.')
        
else:
    bill += 25
    print(f'{bill}$ 받았습니다.')
    
    input('Do you want pepperoni? Y or N ')
    if add_pepperoni == 'y':
        bill += 3
        print(f'{bill}$ 받았습니다.')

input('Do you want extra cheese? Y or N ')
if extra_cheese == 'y':
    bill += 1
    print(f'{bill}$ 받았습니다.')
    
# #롤러코스터    
# print('롤러코스터에 오신것을 환영합니다.')
# height = int(input('키가 몇이십니까?'))
# bill = 0

# if height > 120:
#     print('어서오세요')
#     age = int(input('나이가 어떻게 되세요?'))
#     if age < 12:
#         bill = 5
#         print('%s$ 받겠습니다.' %bill)
#     elif age <= 18:
#         bill = 7
#         print('%s$ 받겠습니다.' %bill)
#     else:
#         bill = 12
#         print('%s$ 받겠습니다.' %bill)
        
        
#     pic = input('사진 찍으시겠습니까? Y or N: ')
#     if pic == 'y':
#         bill += 3
#     print('총 내실 금액은 %s$ 입니다.' %bill)
         
# else:
#     print('입장 못하십니다.')