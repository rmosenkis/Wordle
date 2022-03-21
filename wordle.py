import random, pygame, sys
from nltk.corpus import words
from pygame.locals import *
pygame.init()

white = (255,255,255)
yellow = (183,193,1)
green = (0,122,0)
red = (255,0,0)
lightGrey = (160,160,160)
grey = (75,75,75)
black = (0,0,0)
lightGreen = (153,255,204)

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

youWin = bigFont.render("You Win!", True, lightGreen)
youLose = bigFont.render("You Lose!", True, red)
playAgain = bigFont.render("Play Again?", True, lightGreen)

keyboardTopColorCode = [lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey]
keyboardMiddleColorCode = [lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey]
keyboardBottomColorCode = [lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey]

def checkGuess(turns, word, userGuess, window):
    renderList = ["","","","",""]
    spacing = 0
    guessColorCode = [grey,grey,grey,grey,grey]

    global keyboardTopColorCode, keyboardMiddleColorCode, keyboardBottomColorCode
    topRow = "QWERTYUIOP"
    middleRow = "ASDFGHJKL"
    bottomRow = "ZXCVBNM"

    tempWord = userGuess

    for i in range(5):
        if userGuess[i] in word:
            if tempWord.count(userGuess[i]) < word.count(userGuess[i]):
                if userGuess[i] == word[i]:
                    guessColorCode[i] = green
                    for j in range(10):
                        if userGuess[i] == topRow[j]:
                            keyboardTopColorCode[j] = green
                    for k in range(9):
                        if userGuess[i] == middleRow[k]:
                            keyboardMiddleColorCode[k] = green
                    for l in range(7):
                        if userGuess[i] == bottomRow[l]:
                            keyboardBottomColorCode[l] = green
                else:
                    guessColorCode[i] = yellow
                    for j in range(10):
                        if userGuess[i] == topRow[j]:
                            keyboardTopColorCode[j] = yellow
                    for k in range(9):
                        if userGuess[i] == middleRow[k]:
                            keyboardMiddleColorCode[k] = yellow
                    for l in range(7):
                        if userGuess[i] == bottomRow[l]:
                            keyboardBottomColorCode[l] = yellow
                    
            if tempWord.count(userGuess[i]) == word.count(userGuess[i]):
                if userGuess[i] == word[i]:
                    guessColorCode[i] = green
                    for j in range(10):
                        if userGuess[i] == topRow[j]:
                            keyboardTopColorCode[j] = green
                    for k in range(9):
                        if userGuess[i] == middleRow[k]:
                            keyboardMiddleColorCode[k] = green
                    for l in range(7):
                        if userGuess[i] == bottomRow[l]:
                            keyboardBottomColorCode[l] = green
                else:
                    guessColorCode[i] = yellow
                    for j in range(10):
                        if userGuess[i] == topRow[j]:
                            keyboardTopColorCode[j] = yellow
                    for k in range(9):
                        if userGuess[i] == middleRow[k]:
                            keyboardMiddleColorCode[k] = yellow
                    for l in range(7):
                        if userGuess[i] == bottomRow[l]:
                            keyboardBottomColorCode[l] = yellow
            elif tempWord.count(userGuess[i]) > word.count(userGuess[i]):
                tempWord = tempWord[:i] + "." + tempWord[i+1:]
        else:
            for j in range(10):
                if userGuess[i] == topRow[j]:
                    keyboardTopColorCode[j] = grey
            for k in range(9):
                if userGuess[i] == middleRow[k]:
                    keyboardMiddleColorCode[k] = grey
            for l in range(7):
                if userGuess[i] == bottomRow[l]:
                    keyboardBottomColorCode[l] = grey

    list(userGuess)

    # Change colors of guesses for previous guess
    for i in range(5):
        renderList[i] = font.render(userGuess[i], True, white)
        pygame.draw.rect(window, guessColorCode[i], pygame.Rect(160 + spacing, 50 + (turns * 80), 50, 50))
        window.blit(renderList[i], (176.5 + spacing, 62 + (turns * 80)))
        spacing += 80

    for i in range(10):
        pygame.draw.rect(window, keyboardTopColorCode[i], pygame.Rect(55 + (i * 60), 600, 50, 50))
        window.blit(font.render(topRow[i], True, white), (70 + (i * 60), 612))
    for i in range(9):
        pygame.draw.rect(window, keyboardMiddleColorCode[i], pygame.Rect(85 + (i * 60), 660, 50, 50))
        window.blit(font.render(middleRow[i], True, white), (100 + (i * 60), 672))
    for i in range(7):
        pygame.draw.rect(window, keyboardBottomColorCode[i], pygame.Rect(145 + (i * 60), 720, 50, 50))
        window.blit(font.render(bottomRow[i], True, white), (160 + (i * 60), 732))

    if guessColorCode == [green, green, green, green, green]:
        keyboardTopColorCode = [lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey]
        keyboardMiddleColorCode = [lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey]
        keyboardBottomColorCode = [lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey,lightGrey]
        return True

def main():
    file = open("wordList.txt", "r")
    wordList = file.readlines()
    for i in range(len(wordList) - 1):
        wordList[i] = wordList[i][:-1]

    word = wordList[random.randint(0, len(wordList) - 1)].upper()

    height = 900
    width = 700

    FPS = 30
    clock = pygame.time.Clock()
    
    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ""

    # Draw grid of empty boxes
    for i in range(5):
        for j in range(6):
            pygame.draw.rect(window, grey, pygame.Rect(160 + (i * 80), 50 + (j * 80), 50, 50), 2)

    topRow = "QWERTYUIOP"
    middleRow = "ASDFGHJKL"
    bottomRow = "ZXCVBNM"

    # Draw grid of keyboard
    for i in range(10):
        pygame.draw.rect(window, lightGrey, pygame.Rect(55 + (i * 60), 600, 50, 50))
        window.blit(font.render(topRow[i], True, white), (70 + (i * 60), 612))
    for i in range(9):
        pygame.draw.rect(window, lightGrey, pygame.Rect(85 + (i * 60), 660, 50, 50))
        window.blit(font.render(middleRow[i], True, white), (100 + (i * 60), 672))
    for i in range(7):
        pygame.draw.rect(window, lightGrey, pygame.Rect(145 + (i * 60), 720, 50, 50))
        window.blit(font.render(bottomRow[i], True, white), (160 + (i * 60), 732))
    
    pygame.display.set_caption("Wordle!")

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                window.fill(black, (0, 0, width, 50))
                if event.key == pygame.K_RETURN and win == True:
                    main()
                
                if event.key == pygame.K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE:
                    guess = guess[:-1]
                elif len(guess) == 5:
                    pass
                elif event.key == pygame.K_RETURN:
                    pass
                else:
                    guess += event.unicode.upper()

                if event.key == pygame.K_RETURN and len(guess) == 5:
                    if guess.lower() not in words.words():
                        window.blit(font.render("Word not in list", True, red), (240, 10))
                    else:
                        win = checkGuess(turns, word, guess, window)
                        turns += 1
                        guess = ""

        renderList = ["","","","",""]
        spacing = 0
        userGuess = guess
        list(userGuess)

        # Reset input boxes
        for i in range(5):
            pygame.draw.rect(window, black, pygame.Rect(162 + (i * 80), 52 + (turns * 80), 46, 46))

        # Types user input into boxes
        for i in range(len(userGuess)):
            renderList[i] = font.render(userGuess[i], True, white)
            window.blit(renderList[i], (176.5 + spacing, 62 + (turns * 80)))
            spacing += 80

        if win == True:
            window.fill(black)
            window.blit(youWin, (225, 200))
            window.blit(font.render(f"The word was: {word.strip()}", True, white), (200, 275))
            window.blit(playAgain, (190, 325))

        if turns == 6 and win != True:
            window.fill(black)
            window.blit(youLose, (220, 200))
            window.blit(font.render(f"The word was: {word.strip()}", True, white), (200, 275))
            window.blit(playAgain, (190, 325))
        
        pygame.display.update()
        clock.tick(FPS)

main()

# TODO:
# Get way to see/copy results
# Make 6x5 grid closer together with bigger boxes/bigger text
# Make UI look better after win/loss