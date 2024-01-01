# 소수 구하기.
n = int(input()) 
def prime_checker(n):
    
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            
    if is_prime:
        print('It is Prime')
    else:
        print('It is not Prime')

            
prime_checker(n)





    