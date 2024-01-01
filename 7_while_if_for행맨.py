import random

from hangman_art import logo, stages
print(logo)

from hangman_words import word_list



word = random.choice(word_list)
life = 6

result = []
for i in range(len(word)):
    result += '_'
#['_', '_', '_', '_', '_', '_']

end_game = False
while not end_game:
    
    guess = input(f'Guess a letter {word} : ')
    
    if guess in result:
        print('이미 입력하였습니다.')
    
    
    for i in range(len(word)):
        #i = 0 , k = a
        new_word = word[i]
        if guess == new_word:
            result[i] = new_word
         
    if guess not in word:
        life -=1
        print(f'생명이 {life} 남았습니다.')
       
            
    if '_' not in result:
        end_game = True
        print("YOU WIN!!")
    elif life == 0:
        end_game =True
        print('GAME OVER!')
   
            
    print(''.join(result))
    print(stages[life])
