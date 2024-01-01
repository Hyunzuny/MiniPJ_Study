
#HINT: You can call clear() to clear the output in the console.

from art import logo9
print(logo9)


end_game = False
bids = {}
winner = ''

def high(record):
  high_num = 0
  for keys in record: #record = {'현준': 123, '지은': 321}
    keys_num = record[keys]
    if keys_num > high_num:
      high_num = keys_num
      winner = keys
      
  print(f'승자는 {winner}이고 ${high_num} 입니다.')
    
    
    
  

while not end_game:
  
  name = input('What\'s your name?: ')
  bid = int(input('What\'s your bid?: $'))
  bids[name] = bid
  
  ask = input('입찷할 사람이 있습니까? yes or no : \n')
  if ask == 'n':
    end_game = True
    high(bids)
  elif ask == 'y':
    end_game
    

    
