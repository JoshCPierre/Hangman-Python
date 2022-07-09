import random
# Feb 20 2022
# Feb 28 2022

attempt_limit = 6
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w","y", "x", "z"]
word = ""
guess = ""
letters_correct  = 0
list_of_words = ["character", "astronaut", "car", "python", "programming"]
correct_word = random.choice(list_of_words)


#making a copy of list letters so i can remove values later
letters2 = letters.copy()


#drawing of hangman
def case_0():
    print("---------\n|       |\n|       \n|       \n|       \n|\n|")

def case_1():
    print("---------\n|       |\n|       O\n|       \n|       \n|\n|")

def case_2():
    print("---------\n|       |\n|       O\n|       |\n|       \n|\n|")

def case_3():
    print("---------\n|       |\n|       O\n|      \|\n|       \n|\n|")

def case_4():
    print("---------\n|       |\n|       O\n|      \|/\n|       \n|\n|")

def case_5():
    print("---------\n|       |\n|       o\n|      /|\\\n|       /\n|\n|\n")

def case_6():
    print("---------\n|       |\n|       O\n|      \|/\n|      /\\\n|\n|\n")

        
while attempt_limit > 0 and letters_correct != len(correct_word):
    if attempt_limit == 6:
        case_0()
    #not part of if loop
    guess = input("Enter a letter : ")

    #in case user tries input letter that they have already used
    if guess.lower() not in letters:
        print("Enter a correct value")
    elif guess.lower() not in letters2:
        print("You have already guessed this letter")

    elif guess.lower() in correct_word:
        #in case there are the same letter in same word, increase number of letters correct based on amount of letters(2 As, increase by 2)
        for letter in correct_word:
            if letter == guess:
                letters_correct += 1  

        if letters_correct == len(correct_word):
            break

        print(guess + " is in the letter!")  
        print("You guessed " + str(letters_correct) + " letter(s) correct")
        print("These letters are remaining: ")
        #remove letter from list of letters remaining
        letters2.remove(guess.lower())
        print(letters2)
    
    else:
        attempt_limit -=1
        if attempt_limit == 0:
            break
        print("Wrong guess")
        print ("You have " + str(attempt_limit) + " attempts left" )
        print("These letters are remaining: ")
        #remove letter from list of letters remaining
        letters2.remove(guess.lower())
        print(letters2)
        
    #drawing hangman based on number of attempts left
    if attempt_limit == 5:
        case_1()
    elif attempt_limit == 4:
        case_2()
    elif attempt_limit == 3:
        case_3()
    elif attempt_limit == 2:
        case_4()
    elif attempt_limit == 1:
        case_5()
        
    for letter in correct_word:
        #creating a blank variable that adds guess of user if letter is in correct word
        word = guess + word

        if letter in word.lower():
            print(letter, end=" ")
        else:
            print("_ ", end="")


if attempt_limit == 0:
    case_6()
    print("You guessed the word incorrectly too many times, you ran out of attempts")
    print("The correct word was " + correct_word)
else: 
    print("You guessed the word " + correct_word + " correctly!")


#use try/except

