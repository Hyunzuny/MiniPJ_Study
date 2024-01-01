#함수뒤에는 괄호()가 붙는다.

def format_name(f_name, l_name):
  """3개의 따옴표는 함수를 설명하는 말로 독스트링이다."""
  if f_name == '' or l_name == '':
      return '조기종료' #조기 함수 종료.
  format_f_name = f_name.title()
  format_l_name = l_name.title()
  return f'Result : {format_f_name} {format_l_name}'
  # result = (f_name+' '+l_name).title()
  # return result

a = format_name(input('이름이뭐야?'),input('성이뭐야?'))
print(a)


#ex
output = len('HyunJun') #output = 출력, len = 함수, ('HyunJun') = 입력.

#따라서 출력을 가진 함수를 만드려면 return 이 중요.
