import random
filename = "words.csv"
file = open(filename)
for line in file:
    print(line)


def start():
    print("Want to play hangman?\n")


while True:
    pick = input("Yes or No?\n").upper()
    if pick == "yes":
        break
    elif pick == "no":
        print("Okay bye!")
        continue
start()


def hangman():
    gallows = [',--;-', '| ', '| ', '| ', '| ', '| ', '|_____']
    parts = iter([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])
    sequence = [1, 3, 1, 1, 2]
    for i, v in enumerate(sequence, start=1):
        for k in range(v):
            gallows[i] += next(parts)
            yield '\n'.join(gallows)
    raise StopIteration


def parts():
    parts = iter([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])


def guess():
    guess_word = []
    words = random.choice(file)
    alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    used_letters = []


def play():
    guesses = 1
    guess = input("choose any letter you want\n").lower()


if guess not in used_letters:
    print("These are the letters you have already used!")
while True:
        if guess in words:
            print("Your letter is right!")
        if words in words:
            print("You won!")
            break


while False:
            print("oops try again!")
            for wrong_guesses in words:
                guesses += 1
            gallows + parts([' 0 ', '/', '|', '\\', ' | ', ' A ', '/ ', '\\'])
            if guesses == 9:
                print("Game over!")


def game_over():
    if game_over:
        print("Do you want to play again? Type 1 for yes or type 2 for no?")
        for again in game_over:
           again = type(1)
        for over in game_over:
            over = type(2)



