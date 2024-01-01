#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
result = []
for i in range(len(chosen_word)):
    result +='_'
print(result)





end_of_game = False
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    
    for i in range(len(chosen_word)):
        k = chosen_word[i] #a
        if guess == k: #a
            result[i] = k
            
    print(result)
    
    if '_' not in result:
        end_of_game = True
        print('you win')

