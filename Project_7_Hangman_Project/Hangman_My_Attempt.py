#Hangman Project
#My Attempt

import random

def choose_word():
    '''
    This function chooses a random word from the word list, converts it into a list and stores it in variable `word` of the main function

    Returns
    -------
    word_as_list : TYPE list
    '''
    #word list
    word_list = ["angel", "eyeball", "pizza", "angry", "fireworks", "pumpkin", "baby", "flower", "rainbow", "beard", "recycle", "giraffe", "snowflake", "book", "stairs", "bucket", "starfish", "igloo", "strawberry", "butterfly", "ladybug", "sun", "camera", "lamp", "tire", "lion", "toast", "toilet", "coffee", "nail", "toothbrush", "crayon", "night", "toothpaste", "nose", "truck", "dolphin", "olympics", "egg", "peanut", "wheel"]

    #pick a word randomly from word_list
    word1 = random.choice(word_list)

    #convert the word1 string to list
    word_as_list = list(word1)
    return word_as_list


def make_blanks(word_to_blank):
    '''
    Create as many '_' (blanks) is guess as their are characters in word
    '''
    guess_blanks = []

    for i in range( len(word_to_blank)):
        guess_blanks.append('_')
    return guess_blanks


def guess_print(incoming_guess):
    '''Print guess word'''
    guess_to_print = ''
    for char in incoming_guess:
        guess_to_print += char + ' '
    
    print(guess_to_print)


alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def take_a_guess():
    '''
    this function takes a valid guess from the user

    Returns
    -------
    guessed_letter : TYPE
        DESCRIPTION.

    '''
    guessed_letter = input('\nEnter a letter: ').lower()
    length = len(guessed_letter)
    
    if guessed_letter.isalpha() and length == 1:
        if guessed_letter in alphas:
            #You accept the letter and simultaneously remove the letter from alphas
            #the next time you guess the same letter, it won't be accepted
            alphas.remove(guessed_letter)
        else:
            print(f"You've already chosen {guessed_letter} before. Please choose another letter.")
            guessed_letter = take_a_guess()
    elif guessed_letter.isalpha() and length > 1:
        print("Please enter just one letter")  
        guessed_letter = take_a_guess()
    else:
        print("Please enter an alphabet")
        guessed_letter = take_a_guess()
    return guessed_letter
 
   
def update_guess(original_word, current_guess, current_guessed_letter):
    '''
    When you guess a correct letter, this function update guess variable and fill the corresponding blanks to that letter

    Parameters
    ----------
    original_word : TYPE str
    current_guess : TYPE str
    current_guessed_letter : TYPE str

    Returns
    -------
    current_guess : TYPE str
        DESCRIPTION. returns the updated guess

    '''
    for i in range( len(original_word)):
        if original_word[i] == current_guessed_letter:
            current_guess[i] = current_guessed_letter

    return current_guess  


word = choose_word()
print(f"Chosen word is {word}")

guess = make_blanks(word)

#Set number of lives
life = 5

while (life > 0) and ('_' in guess):
    guess_print(guess)
    print(f"Life: {life}/5")
    
    #guess a letter
    letter = take_a_guess()
    
    #if the guessed letter is in the word,
    #fill the corresponding blanks with that letter
    if letter in word:
        guess = update_guess(word, guess, letter)
        
    #if not, minus one life
    else:
        life -= 1
        print("Uh oh, wrong guess!\n")
        
if life == 0:
    guess_print(word)
    print("You ran out of lives!\n")
    print("\nGame over")

if '_' not in guess:
    print("\nYay! you win")
    guess_print(guess)
    




