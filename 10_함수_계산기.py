from art import logo10
print(logo10)

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2


#dic keys : 사칙연산, values : 함수
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div   
}

def calculation():   
    num1 = float(input('첫번째 숫자를 입력하세요.\n'))

    for key in operations:
        print(key)
        
    end_game = True
    while  end_game:
        
        symbol = input('부호를 고르세요: \n')
        o_symbol = operations[symbol]
        num2 = float(input('다음 숫자를 입력하세요:\n'))
        answer = o_symbol(num1, num2)
        print(f'{num1} {symbol} {num2} = {answer}')
        

        ask = input(f'y 면 {answer} 와 같이 계산, n 이면 새로시작.: \n')
        if ask == 'y':
            num1 = answer
        else:
            end_game = False
            calculation()
            
calculation()  #처음으로 돌아가려면 재귀사용.
       

