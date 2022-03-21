import random, pygame, sys
from nltk.corpus import words
from pygame.locals import *
pygame.init()

white = (255,255,255)
yellow = (255,255,102)
green = (0,255,0)
red = (255,0,0)
grey = (211,211,211)
black = (0,0,0)
lightGreen = (153,255,204)

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)\

youWin = bigFont.render("You Win!", True, lightGreen)
youLose = bigFont.render("You Lose!", True, red)
playAgain = bigFont.render("Play Again?", True, lightGreen)

def checkGuess(turns, word, userGuess, window):
    renderList = ["","","","",""]
    spacing = 0
    guessColorCode = [grey,grey,grey,grey,grey]

    for i in range(5):
        if userGuess[i] in word:
            guessColorCode[i] = yellow
        
        if userGuess[i] == word[i]:
            guessColorCode[i] = green

    list(userGuess)

    for i in range(5):
        renderList[i] = font.render(userGuess[i], True, black)
        pygame.draw.rect(window, guessColorCode[i], pygame.Rect(60 + spacing, 50 + (turns * 80), 50, 50))
        window.blit(renderList[i], (70 + spacing, 50 + (turns * 80)))
        spacing += 80

    if guessColorCode == [green, green, green, green, green]:
        return True

def main():
    file = open("wordList.txt", "r")
    wordList = file.readlines()
    for i in range(len(wordList) - 1):
        wordList[i] = wordList[i][:-1]

    word = wordList[random.randint(0, len(wordList) - 1)].upper()

    height = 600
    width = 500

    FPS = 30
    clock = pygame.time.Clock()
    
    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ""

    for i in range(5):
        for j in range(6):
            pygame.draw.rect(window, grey, pygame.Rect(60 + (i * 80), 50 + (j * 80), 50, 50), 2)

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
                        window.blit(font.render("Word not in list", True, red), (140, 10))
                    else:
                        win = checkGuess(turns, word, guess, window)
                        turns += 1
                        guess = ""
                        window.fill(black, (0, 500, 500, 200))

        window.fill(black, (0, 500, 500, 200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))

        if win == True:
            window.fill(black)
            window.blit(youWin, (125, 200))
            window.blit(font.render(f"The word was: {word.strip()}", True, white), (100, 275))
            window.blit(playAgain, (90, 325))

        if turns == 6 and win != True:
            window.fill(black)
            window.blit(youLose, (120, 200))
            window.blit(font.render(f"The word was: {word.strip()}", True, white), (100, 275))
            window.blit(playAgain, (90, 325))
        
        pygame.display.update()
        clock.tick(FPS)

main()

# TODO:
# Find out way to deal with double letters
# Get way to see/copy results
# Show/update keyboard as you guess
# Make UI look better after win/loss