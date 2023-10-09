from random import choice
from string import ascii_lowercase
from sys import exit

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

print('H A N G M A N')
while True:
    print('Type "play" to play the game, "exit" to quit:')
    user_input = input()
    if user_input == 'play':
        break
    elif user_input == "exit":
        exit()
    else:
        continue

words_list = ['python', 'java', 'coding', 'javascript']
word = choice(words_list)
hidden_word = list('-' * len(word))
lives = 6  # Change the total lives to 6
letter_list = []

while lives > 0:
    if '-' not in hidden_word:
        break
    print(f'\n{" ".join(hidden_word)}')
    print(f'Lives left: {lives}')
    letter = input('Input a letter: ')
    
    if len(letter) != 1 or letter not in ascii_lowercase:
        print('Please enter a single lowercase English letter')
        continue
    
    if letter in letter_list:
        print("You've already guessed this letter")
        continue
    
    letter_list.append(letter)
    
    if letter in set(word):
        for index in find(word, letter):
            hidden_word[index] = letter
    else:
        lives -= 1
        print("That letter doesn't appear in the word")

if '-' not in hidden_word:
    print('You survived!')
else:
    print('You lost!')
