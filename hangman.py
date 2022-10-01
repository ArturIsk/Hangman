import random

pos = False
wins = 0
los = 0

while pos is False:
    print("H A N G M A N")
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if choice == "play":
        pos = True
        guessed = []
        words = ["python", "java", "swift", "javascript"]
        the_word = random.choice(words)  # str
        covered = "-" * len(the_word)  # str
        z = 0  # int
        counter = int(0)  # int

        while pos == True:
            z = 0  # use if a letter appears multiple times in the_word
            print(f'\n{covered}')
            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("Please, input a single letter.")
            elif letter.islower() is False or letter.isalpha() is False:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter in guessed:
                print("You've already guessed this letter.")
            elif letter in the_word and letter not in covered:
                z = the_word.find(letter, z)
                a = the_word.count(letter)  # detects the position to replace in covered
                for i in range(a):
                    covered = covered[: z] + letter + covered[z + 1:]
                    z = the_word.find(letter, z + 1)
                    i += 1
                    if "-" not in covered:
                        wins += 1
                        print(f'\n{covered} \nYou guessed the word {the_word}!\nYou survived!')
                        pos = False
                        break
                    else:
                        pass
                    guessed.append(letter)
            else:
                print(f'That letter doesn\'t appear in the word.')
                counter += 1
                guessed.append(letter)

            if counter == 8:
                los += 1
                print("\nYou lost!")
                pos = False

    elif choice == "results":
        # pos = True
        print(f'You won: {wins} times')
        print(f'You lost: {los} times')
    elif choice == "exit":
        pos = True
        break
    else:
        pos = False