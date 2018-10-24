from random import randint
import os
import sys
def rhyme():
    print("I want to test your mental ability before you proceed")
    print("I'm going to give you a sentence, and you have to reuturn the words to me that rhyme, in the order you see them!")
    print("A tisket, a tasket, here is the ryhming basket. After the fifteenth hour, grows the flower")
    user_input = str(input())
    complete = False
    user_input = user_input.replace(" ", "")
    user_input = user_input.lower()
    print(user_input)
    if user_input == "tasketbaskethourflower":
        complete = True
        print("you got that correct, Congrats")
    else:
        complete = False
        print("i'm sorry that's not right")

    return complete


def number():
    print("I want to test your mental ability before you proceed")
    print("I am going to pick a number from 1 to 100, you have 5 guesses to get the number")
    print("what is your first guess")
    count = 4
    choice = randint(0, 100)
    complete = False
    while complete == False or count != 0:
        if count == -1:
            break
        user_input = int(input())
        if choice == user_input:
            print("you got it correct in " + str(5 - count))
            complete = True
            break
        elif user_input > choice:
           print("sorry, that's too high")
           print("you have " + str(count) + " tries left")
           count = count - 1
           complete = False
        elif user_input < choice:
            print("sorry, that's too low")
            print("you have " + str(count) + " tries left")
            count = count - 1
            complete = False
        elif user_input < 0 or user_input > 100:
            print("please input a number between 1 and 100")
    if count == 0:
        print("I am sorry you didn't manage to guess the number")
    
    return complete

def colour():
    colours = ['black','blue','green','gray','red','purple','yellow','white','orange']
    os_colours= [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e']
    incorrect = 3
    score = 0
    rand_colour = 0
    rans_word = 0
    print("I want to test your mental ability before you proceed")
    print("I am going to show you some colours in different colour text, I want you to type in the colour of the word, not the text")
    os.system('pause')
    complete = False
    
    while incorrect != 0:
        rand_colour = randint(0, 14)
        rand_word = randint(0, 8)
        if rand_colour == 0:
            rand_colour = 1
        if rand_word == 3:
            rand_word + 1
        os.system('cls')
        os.system('color '+ str(os_colours[rand_colour]))
        print(str(colours[rand_word]))
        os.system('color')
        user_input = str(input())
        user_input = user_input.strip()
        if str(user_input) == str(colours[rand_word]):
            print("correct")
            score = score + 1
            print('score = ' + str(score))
            os.system('pause')
            if score == 3:
                print("congrats you complete the game and got max score")
                complete = True
                break
            elif incorrect == 0:
                print("I'm sorry, you hyave failed")
                complete = False
                break
        elif str(user_input) != str(colours[rand_word]):
            incorrect = incorrect - 1
            print("incorrect,you have " + str(incorrect) + " wrong guesses left")
            os.system('pause')
            if score == 3:
                print("congrats you complete the game and got max score")
                complete = True
                break
            elif incorrect == 0:
                print("I'm sorry, you hyave failed")
                complete = False
                break
    os.system('color 7')    
    return complete

#puzzles = {
#    "first puzzle":rhyme(),
#    "second puzzle":number(),
#    "third puzzle":colour()
#}