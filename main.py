import random
guesslist = []
#ask user for length of words
def game_start():
    game_start.wordlen = int(input('Enter length of word between [4-16]: '))
    if  game_start.wordlen not in range(4,17):
        print('Enter valid  length of word.')
    elif game_start.wordlen in range(4,17):
        print(f'Word of length {game_start.wordlen} generated.')


#generate word of length mentioned by user
def word_gen():
    word = open("G:\pythin course\Hangman\words.txt").readlines()
    word_gen.new_word = random.choice(word)
    if len(word_gen.new_word) == game_start.wordlen + 1:
        word_gen.wordList = list(word_gen.new_word.strip())
        print(word_gen.wordList)
        for i in word_gen.wordList:
            guesslist.append('_')
    else:
        word_gen()



#ask  nummber of attempts
def attempt_chk():
    attempt = 0
    attempt_chk.user_atmpt = int(input('Choose the number of attempts between ~ [5-10]: '))
    if  attempt_chk.user_atmpt not in range(1,17):
        print('Enter valid  attempts.')
    elif attempt_chk.user_atmpt in range(1,17):
        print(f'{attempt_chk.user_atmpt} attempts remaining.')

#print answer
def ans_print():
    print(''.join(guesslist))
    if guesslist != word_gen.wordList:
        let_chk()
    else:
        win()

#guess letter and check
def let_chk():
    let_chk.userin = str(input('\nGuess a letter. '))
    if let_chk.userin in word_gen.wordList:
        for i in range(len(word_gen.wordList)):
            if let_chk.userin == word_gen.wordList[i]:
                lettrindex = i
                guesslist[lettrindex] = let_chk.userin
        ans_print()
    else:
        w_userin()


#if wrong decrement attempts
def w_userin():
    print('Wrong Letter! \nTry Again!')
    attempt_chk.user_atmpt -= 1
    if attempt_chk.user_atmpt > 0:
        print(f'{attempt_chk.user_atmpt} attempts remaining.')
        let_chk()
    else:

        lose()





    let_chk()
#When won
def win():
    print('win')
    str(input('Do you want to play again?"Y" OR "N"'))
    if "Y":
        game_start()
    else:
        exit()

#When Lost
def lose():
    print('You Loose! \nBetter Luck  Next Time')
    print('The  correct word is:',word_gen.new_word)
    str(input('Do you want to play again?"Y" OR "N"'))
    if "Y":
        game_start()
    else:
        exit()




#Invoke all the functions
game_start()
word_gen()
attempt_chk()
ans_print()