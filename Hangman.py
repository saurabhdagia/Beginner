import random

let_distinct = []
let_correct = []
let_incorrect = []
user_input = ""
guess_count = 0
guess_target = 25
letters_complete = False

def generate ():
    global word
    global l
    with open('sowpods.txt') as f:
        words = list(f)
    word = random.choice(words).lower().strip()
    l = len(word)
    print("This is a " + str(l) + " leter word")
    i = 0
    while i < l:
        let = word[i]
        if let not in let_distinct:
            let_distinct.append(let)
        i += 1
#    print(word)
#    print(let_distinct)

def letters(lc,li):
    print("The correct letters are " + str(sorted(lc)))
    print("The incorrect letters are :" + str(sorted(li)))

def display(wd,lc,l1):
    j = 0
    word2 = ""
    let2 = ""
    while j < l:
        let2 = wd[j]
        if let2 not in lc:
            word2 = word2 + " _"
        else:
            word2 = word2 + " " + let2
        j += 1
    print(word2)


def game():
    global guess_count
    global letters_complete
    global word2
    generate()
    while guess_count < guess_target and letters_complete is False:
        user_input = input("Choose a letter: ").lower()
        if not(user_input.isalpha()) or not(len(user_input) == 1):
            print("Please provide a single alphabet as input")
        elif (user_input in let_correct or user_input in let_incorrect):
            print("You already tried this alphabet. Try a new one")
        elif user_input in word:
            print("There are " + str(word.count(user_input)) +" instances of the letter " + user_input )
            let_correct.append(user_input)
            display(word,let_correct,l)
            letters(let_correct,let_incorrect)
            if sorted(let_correct) == sorted(let_distinct):
                letters_complete = True
            guess_count += 1
        elif user_input not in word:
            print("Sorry, this letter does not exist")
            let_incorrect.append(user_input)
            display(word,let_correct,l)
            letters(let_correct,let_incorrect)
            guess_count += 1

game()
print ("The word is " + word )
if letters_complete:
    print ("Congratulations!! You did it")
else:
    print ("You ran out of chances!! Better luck next time")
    