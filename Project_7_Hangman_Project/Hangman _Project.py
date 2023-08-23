#Hangman Project : Challenge 2

import random
import hangman_art
import hangman_words
from replit import clear

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lives = 6

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
     
    guess = input("Guess a letter: ").lower()
    
    clear()
    
    if guess in alphabets:
        if guess in chosen_word:
            #Check guessed letter
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
        else:
            lives -= 1
            print(f"\n{guess} is not in the word.")
            if lives == 0:
                end_of_game = True
                print("You lose!")
        alphabets.remove(guess)
    else:
        print(f"\nYou've chosen {guess} before. Please choose another alphabet.")

    #Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("Yay! You win!")
        
    print(hangman_art.stages[lives])
    
    
    
    
    
    
    