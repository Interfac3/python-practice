import random
from hangman_ascii import stages, logo
from hangman_words import word_list
print(logo)
chosen_word = random.choice(word_list)

end_of_game = False
display=[]
lifes=6
for i in chosen_word:
    display.append('_')
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"{guess} cannot select same letter again, please select a new one")
    for letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess
    print(display)
    if guess not in chosen_word:
        lifes-=1
        if lifes==0:
            print("you lose")
            end_of_game=True
    if '_' not in display:
        end_of_game=True
        print("You Win")
    print(stages[lifes])