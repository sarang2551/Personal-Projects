
import pygame,sys,random

pygame.init()
game_state = True
screen = pygame.display.set_mode((512,512))
clock = pygame.time.Clock()
pole = pygame.image.load('C:/Users/saran/OneDrive/Desktop/NirwanaWarehouse/Website stuff/images/Hangman/pole.png').convert()
bg_surface = pygame.image.load('C:/Users/saran/OneDrive/Desktop/NirwanaWarehouse/Website stuff/images/Hangman/bg_image.jfif').convert()
bg_surface = pygame.transform.scale(bg_surface,(512,512))


#Words section
list_words = ['condition','dinosaur','innocent','telephone','global','portable']
#window name
pygame.display.set_caption('Hangman')
word = random.choice(list_words)
#selecting font
font = pygame.font.Font('freesansbold.ttf', 16)
blanks = '#' * len(word)
black = (0,0,0)
white = (255,255,255)
text = font.render('The word is ' + str(len(word)) + ' letters long', True, black)
head = pygame.image.load('C:/Users/saran/OneDrive/Desktop/NirwanaWarehouse/Website stuff/images/Hangman/head.jfif').convert_alpha()
head = pygame.transform.scale(head, (50, 50))
alphabets_used = ''
text2 = font.render('Alphabets guessed: '+alphabets_used, True, black)
text3 = font.render('Enter alphabet: ', True, black)
blanks_display = font.render(blanks, True, black)
winning = font.render('YOU WIN THE GAME!!', True, black)
user_input = ''
#conditions for showing body parts
show_head = False
show_body = False
show_left_arm = False
show_right_arm = False
show_left_leg = False
show_right_leg = False
you_won = False
errors = 0

#Game Loop
while (True):
    screen.fill(white)
    screen.blit(text, (0, 0))
    screen.blit(text2 , (0,350))
    screen.blit(text3, (0,250))
    screen.blit(blanks_display, (0, 150))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and game_state == True: #just to check if any button was pressed
            if event.key == pygame.K_BACKSPACE: #happens when you press backspace
                user_input = user_input[0:-1] #going from the first character to the one character before the last
            else:
                user_input += event.unicode #essentially adding any alphabet into the user text
            if event.key == pygame.K_KP_ENTER: #submission of word using the 'enter key' on the numpad
                position = word.find(user_input)
                if position != -1:  # if the user input is in the word
                    word = word[:position] + '_' + word[position + 1:]
                    blanks = blanks[:position] + user_input + blanks[position + 1:]
                    blanks_display = font.render(blanks, True, black)
                    screen.blit(blanks_display, (0, 150))
                    user_input = ''
                    if '#' not in blanks: #check if the winning condition is satisfied
                      you_won = True
                      game_state = False
                else:  # if the user input is not in the word
                    errors += 1
                    alphabets_used += user_input + ','
                    #updatting the words used
                    text2 = font.render('Alphabets used up: ' + alphabets_used , True, black)
                    screen.blit(text2, (0, 350))
                    #resetting the user input so that i dont have to press backspace again in order to add a new input
                    user_input = ''
                    #subsequent errors and the body being slowly built
                    if errors == 1:
                     show_head = True
                    if errors == 2:
                     show_body = True
                    if errors == 3:
                        show_left_arm = True
                    if errors == 4:
                        show_right_arm = True
                    if errors == 5:
                        show_left_leg = True
                    if errors == 6:
                        show_right_leg = True
                        game_state = False


    user_input_surface = font.render(user_input, True, black)
    screen.blit(user_input_surface, (150,250))
    screen.blit(pole,(250,0))
    if show_head == True:
     screen.blit(head, (400, 25))
    if show_body == True:
        pygame.draw.line(screen, black,[425,75],[425,175],2)
    if show_left_arm == True:
        pygame.draw.line(screen, black, [425,75],[400,150],2)
    if show_right_arm == True:
        pygame.draw.line(screen, black, [425, 75], [450, 150], 2)
    if show_left_leg == True:
        pygame.draw.line(screen, black, [425, 175], [400, 250], 2)
    if show_right_leg == True:
        pygame.draw.line(screen, black, [425, 175], [450, 250], 2)
    if you_won == True:
       screen.blit(winning, (0, 75))


    pygame.display.update()
    clock.tick(120)
