# Write your code here
import random
import string
print("H A N G M A N")
list1 = ['python', 'java', 'kotlin', 'javascript']
riddle = random.choice(list1)
riddlehype = "-" * (len(riddle))
guessed = list()

counter1 = 8
while True:
    start= input('Type "play" to play the game, "exit" to quit: ')
    if len(start) != 4:
        continue

    if (start != 'exit') and (start != 'play'):
        continue
    if start == 'exit':
        break
    elif start == 'play':
        while counter1 != 0:
            print('')
            print(riddlehype)
            letter = input("Input a letter: ")

            if len(letter) > 1:
                print('You should input a single letter')
                continue
            if letter not in string.ascii_lowercase:
                print('It is not an ASCII lowercase letter')
                continue
            if letter in guessed:
                print("You already typed this letter")
                continue
            else:
                guessed.append(letter)

            if letter not in riddle:
                counter1 -= 1
                print("No such letter in the word")
            elif letter in riddlehype:
                counter1 -= 1
                print('No improvements')
            elif letter not in riddlehype:
                if letter in riddle:
                    riddlehype = list(riddlehype)
                    counter = 0
                    for i in riddle:
                        if letter == i:
                            riddlehype[counter] = letter
                        counter += 1
                    riddlehype = "".join(riddlehype)
                    if riddlehype == riddle:
                        print('')
                        print(f"{riddle}\nYou guessed the word!\nYou survived!")
                        print('')
                        break
        if counter1 == 0:
            print('You lost!')
            print('')
