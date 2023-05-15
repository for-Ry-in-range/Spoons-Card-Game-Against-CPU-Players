# MADE BY YATIN MARPU AND RYAN WONG @NYU2026

import random
import pygame
from Card import Card
from Deck import Deck

def start_screen():
    exit = False
    pygame.init()  # initializes the game
    canvas = pygame.display.set_mode((1200, 675))  # sets the size of the window

    pygame.display.set_caption("Spoons")  # sets the window’s name

    bg = pygame.image.load("start_screen.png")
    bg_resized = pygame.transform.scale(bg, (1200, 675))
    canvas.blit(bg_resized, (0, 0))

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 170 < pos[0] < 451 and 392 < pos[1] < 497:  # if the user clicks Play
                    playgame(50, 1)
                    exit=True
        pygame.display.update()
        pygame.time.Clock().tick(60)


#checking if cards are similar
def get_similar_card(card1, card2, card3, card4):
    # if 3 cards are the same:
    if card1 == card2 == card3 and card3 != card4:
        return 3, card1
    elif card1 == card2 == card4 and card4 != card3:
        return 3, card1
    elif card4 == card2 == card3 and card3 != card1:
        return 3, card4
    elif card1 == card4 == card3 and card3 != card2:
        return 3, card1
    # if 2 cards are the same:
    elif card1 == card2 and card1 != card3:
        return 2, card1
    elif card1 == card3 and card1 != card2:
        return 2, card1
    elif card1 == card4 and card1 != card3:
        return 2, card1
    elif card2 == card3 and card2 != card4:
        return 2, card2
    elif card2 == card4 and card2 != card3:
        return 2, card2
    elif card3 == card4 and card3 != card2:
        return 2, card3
    return None

# Returns the new deck as a list of strings and a string of the card that will be given to the next player
def ai_decide_card(next_card, card1, card2, card3, card4):
    check_for_similarity = get_similar_card(card1.value, card2.value, card3.value, card4.value)
    hand = [card1, card2, card3, card4]
    dump = next_card
    if check_for_similarity == None:  # if none of their hand is similar
        rand_num = random.randint(0, 19)
        if next_card.value == card1.value:
            return [card1, next_card, card3, card4], card2
        elif next_card.value == card2.value:
            return [next_card, card2, card3, card4], card1
        elif next_card.value == card3.value:
            return [card1, card2, card3, next_card], card4
        elif next_card.value == card4.value:
            return [card1, card2, next_card, card4], card3
        elif rand_num < 4:  # sometimes the bot will randomly swap a card out, even if there's no match
            temp = hand[rand_num]
            hand[rand_num] = next_card
            return hand, temp
        return hand, next_card
    elif check_for_similarity[0] == 2:  # if two cards are similar
        not_in_the_pair = []
        in_the_pair = []
        for i in range(4):
            if hand[i].value != check_for_similarity[1]:
                not_in_the_pair.append(i)
            else:
                in_the_pair.append(i)
        if check_for_similarity[1] == next_card.value:  # if the next card is the same one that the bot has 2 of
            dump = hand[not_in_the_pair[0]]
            hand[not_in_the_pair[0]] = next_card
        elif hand[not_in_the_pair[0]].value == hand[not_in_the_pair[1]].value == next_card.value:  # if the other two cards are the same as next card
            dump = hand[in_the_pair[0]]
            hand[in_the_pair[0]] = next_card
        elif hand[not_in_the_pair[0]].value == next_card.value:
            dump = hand[not_in_the_pair[1]]
            hand[not_in_the_pair[1]] = next_card
        elif hand[not_in_the_pair[1]].value == next_card.value:
            dump = hand[not_in_the_pair[0]]
            hand[not_in_the_pair[0]] == next_card
        return hand, dump
    elif check_for_similarity[0] == 3:  # if 3 cards are the same
        for i in range(4):
            if hand[i].value != check_for_similarity[1]:  # if this card is not the same as the other 3
                i_of_not_the_same = i  # index of the card that's not the same as the other 3
        if check_for_similarity[1] == next_card.value:  # if next card is the same as the other 3 cards
            dump = hand[i_of_not_the_same]
            hand[i_of_not_the_same] = next_card
        return hand, dump


# code for the cpu player's logic
def bot_plays(player_num, dealt_cards):
    if dealt_cards[player_num][0].cards != []:
        hand_and_dump = ai_decide_card(dealt_cards[player_num][0].cards[0], dealt_cards[player_num][1], dealt_cards[player_num][2], dealt_cards[player_num][3], dealt_cards[player_num][4])
        dealt_cards[player_num][1] = hand_and_dump[0][0]
        dealt_cards[player_num][2] = hand_and_dump[0][1]
        dealt_cards[player_num][3] = hand_and_dump[0][2]
        dealt_cards[player_num][4] = hand_and_dump[0][3]
        dealt_cards[player_num][0].remove_top_card()
        if player_num + 1 < len(dealt_cards):  # if index in range
            dealt_cards[player_num+1][0].cards.append(hand_and_dump[1])  # add the dump card to the next player's dump
        else:
            dealt_cards[0][0].cards.append(hand_and_dump[1])

# creating a Card class for each card in a standard 52 card deck
twoh = Card("2", "h")
threeh = Card("3", "h")
fourh = Card("4", "h")
fiveh = Card("5", "h")
sixh = Card("6", "h")
sevenh = Card("7", "h")
eighth = Card("8", "h")
nineh = Card("9", "h")
tenh = Card("10", "h")
jh = Card("j", "h")
qh = Card("q", "h")
kh = Card("k", "h")
ah = Card("a", "h")
twod = Card("2", "d")
threed = Card("3", "d")
fourd = Card("4", "d")
fived = Card("5", "d")
sixd = Card("6", "d")
sevend = Card("7", "d")
eightd = Card("8", "d")
nined = Card("9", "d")
tend = Card("10", "d")
jd = Card("j", "d")
qd = Card("q", "d")
kd = Card("k", "d")
ad = Card("a", "d")
twoc = Card("2", "c")
threec = Card("3", "c")
fourc = Card("4", "c")
fivec = Card("5", "c")
sixc = Card("6", "c")
sevenc = Card("7", "c")
eightc = Card("8", "c")
ninec = Card("9", "c")
tenc = Card("10", "c")
jc = Card("j", "c")
qc = Card("q", "c")
kc = Card("k", "c")
ac = Card("a", "c")
twos = Card("2", "s")
threes = Card("3", "s")
fours = Card("4", "s")
fives = Card("5", "s")
sixs = Card("6", "s")
sevens = Card("7", "s")
eights = Card("8", "s")
nines = Card("9", "s")
tens = Card("10", "s")
js = Card("j", "s")
qs = Card("q", "s")
ks = Card("k", "s")
a_s = Card("a", "s")  # as is a keyword

def bet_screen(money_left):
    exit = False
    pygame.init()  # initializes the game
    canvas = pygame.display.set_mode((1200, 675))  # sets the size of the window

    pygame.display.set_caption("Spoons")  # sets the window’s name

    bg = pygame.image.load("bet_screen.png")
    bg_resized = pygame.transform.scale(bg, (1200, 675))

    current_bet = 15

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 501 < pos[0] < 710 and 540 < pos[1] < 618:  # play button
                    return current_bet
                elif 694 < pos[0] < 755 and 335 < pos[1] < 415 and current_bet<money_left:  # increase bet button
                    current_bet += 1
                elif 694 < pos[0] < 755 and 423 < pos[1] < 503 and current_bet > 15:  # decrease bet button
                    current_bet -= 1

        my_font = pygame.font.SysFont('Oswald-VariableFont_wght.ttf', 57, italic=True)
        total_money_text = my_font.render("$" + str(money_left), False, (217, 217, 217))
        my_font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 62)
        bet = my_font.render("$"+str(current_bet), False, (255, 255, 255))
        canvas.blit(bg_resized, (0, 0))
        canvas.blit(total_money_text, (733, 236))
        canvas.blit(bet, (530, 394))
        pygame.display.update()
        pygame.time.Clock().tick(60)


def playgame(money_left, round_num):
    if money_left < 15:
        exit = False
        pygame.init()  # initializes the game
        canvas = pygame.display.set_mode((1200, 675))  # sets the size of the window

        pygame.display.set_caption("Spoons")  # sets the window’s name

        bg = pygame.image.load("game_over.png")
        bg_resized = pygame.transform.scale(bg, (1200, 675))
        my_font = pygame.font.Font('Caveat-VariableFont_wght.ttf', 35)
        roundslasted_text = my_font.render('You lasted ' + str(round_num-1) + " rounds!", False, (255, 255, 255))
        canvas.blit(bg_resized, (0, 0))
        canvas.blit(roundslasted_text, (490, 325))


        while not exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 450 < pos[0] < 773 and 410 < pos[1] < 514:  # if the user clicks Play
                        playgame(50, 1)
                        exit = True
            pygame.display.update()
            pygame.time.Clock().tick(60)


    bet = bet_screen(money_left)
    money_left -= bet
    exit = False
    gamedeck = Deck()
    deck = [twoh, threeh, fourh, fiveh, sixh, sevenh, eighth, nineh, tenh, jh, qh, kh, ah, twod, threed, fourd, fived,
            sixd, sevend, eightd, nined, tend, jd, qd, kd, ad, twoc, threec, fourc, fivec, sixc, sevenc, eightc, ninec,
            tenc, jc, qc, kc, ac, twos, threes, fours, fives, sixs, sevens, eights, nines, tens, js, qs, ks, a_s]
    gamedeck.create(deck)  # Creating deck
    gamedeck.shuffle()  # Shuffling deck

    players = 4
    dealt_cards = gamedeck.deal(players)
    slide_card = False
    next_card_x = 990
    player = 0
    nextplayer = 1
    finished =  False
    first = False
    second = False
    third = False
    Fourth = False
    bot_speeds = []
    took_spoon = []
    spoon_available = False
    check_spoons = []
    frame = 0
    spoons_left = players - 1
    award_money = False
    played_a_card = False
    mouse_pos = [-1,-1]
    frames_since_card_pressed = 0

    for i in range(players - 1):
        check_spoons.append(random.randrange(180, 360))

    for i in range(players):
        took_spoon.append(False)

    for i in range(players - 1):
        bot_speeds.append(random.randrange(20, 40))

    pygame.init()  # initializes the game

    canvas = pygame.display.set_mode((1200, 675))  # sets the size of the window
    my_font = pygame.font.Font('Pacifico.ttf', 50)
    text_surface = my_font.render('Spoons', False, (255, 255, 255))
    my_font = pygame.font.Font('Caveat-VariableFont_wght.ttf', 25)
    bet_text = my_font.render('Bet placed: $'+str(bet), False, (255, 255, 255))
    round_text = my_font.render('Round #'+str(round_num), False, (255,255,255))
    moneyleft_text = my_font.render('Money left: $' + str(money_left), False, (255,255,255))
    my_font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 25)
    play_warning = my_font.render('CLICK A CARD - THE OTHER PLAYERS ARE WAITING FOR CARDS', False, (214, 198, 188))
    my_font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 23)
    empty_pile = my_font.render('YOUR PILE IS CURRENTLY EMPTY. THE OTHER PLAYERS ARE STILL GOING THROUGH THEIR CARDS', False, (214, 198, 188))

    pygame.display.set_caption("Spoons")  # sets the window’s name

    # Images:
    bg = pygame.image.load("background.png")
    playagain = pygame.image.load("play_again.png")
    playagain_resized = pygame.transform.scale(playagain, (1200, 675))
    foursame = False

    # Creating a waiting deck at the 0th index of each list in dealt_cards
    dealt_cards[0].insert(0, gamedeck)
    for x in range(1, players):
        dealt_cards[x].insert(0, Deck())

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if finished and 469 < pos[0] < 745 and 371 < pos[1] < 473:
                    round_num+=1
                    playgame(money_left, round_num)
                    exit = True
                elif not finished and 1153 > pos[0] > 991 and 382 > pos[1] > 152 and len(dealt_cards[0][0].cards) != 0:  # next card up
                    x = gamedeck.draw()
                    dealt_cards[nextplayer][0].addcard(x)
                    mouse_pos = [-1,-1]
                    frames_since_card_pressed = 0
                elif not finished and 451 < pos[0] < 612 and 400 < pos[1] < 631 and len(dealt_cards[0][0].cards) != 0:  # first card
                    x = dealt_cards[0][1]
                    dealt_cards[0][1] = gamedeck.draw()
                    dealt_cards[nextplayer][0].addcard(x)
                    mouse_pos = [-1, -1]
                    frames_since_card_pressed = 0
                elif not finished and 630 < pos[0] < 791 and 402 < pos[1] < 633 and len(dealt_cards[0][0].cards) != 0:  # second card
                    x = dealt_cards[0][2]
                    dealt_cards[0][2] = gamedeck.draw()
                    dealt_cards[nextplayer][0].addcard(x)
                    mouse_pos = [-1, -1]
                    frames_since_card_pressed = 0
                elif not finished and 811 < pos[0] < 971 and 402 < pos[1] < 632 and len(dealt_cards[0][0].cards) != 0:  # third card
                    x = dealt_cards[0][3]
                    dealt_cards[0][3] = gamedeck.draw()
                    dealt_cards[nextplayer][0].addcard(x)
                    mouse_pos = [-1, -1]
                    frames_since_card_pressed = 0
                elif not finished and 990 < pos[0] < 1152 and 402 < pos[1] < 631 and len(dealt_cards[0][0].cards) != 0:  # fourth card
                    x = dealt_cards[0][4]
                    dealt_cards[0][4] = gamedeck.draw()
                    dealt_cards[nextplayer][0].addcard(x)
                    mouse_pos = [-1, -1]
                    frames_since_card_pressed = 0
                elif not finished and 14 < pos[0] < 143 and 16 < pos[1] < 114 and (foursame or spoon_available):  # spoons
                    spoons_left-=1
                    award_money = True
                    foursame = False
                    took_spoon[0] = True

        frame += 1  # counts frame number
        frames_since_card_pressed += 1

        if dealt_cards[1][0].cards != []:
            played_a_card = True

        for taken_spoon in took_spoon:
            if taken_spoon:
                spoon_available = True

        for i in range(players-1):
            if frame % bot_speeds[i] == 0:
                if not took_spoon[i+1] and dealt_cards[i + 1][1].value == dealt_cards[i + 1][2].value == dealt_cards[i + 1][3].value == dealt_cards[i + 1][4].value:
                    spoons_left -= 1
                    took_spoon[i+1] = True
                else:
                    bot_plays(i+1, dealt_cards)
            if frame % check_spoons[i] == 0:
                if spoon_available:
                    took_spoon[i+1] = True
                    spoons_left -= 1

        if dealt_cards[0][1].value == dealt_cards[0][2].value == dealt_cards[0][3].value == dealt_cards[0][4].value:
            foursame = True

        if took_spoon[0] and spoons_left == 2:
            finished = True
            first = True
            if award_money:
                money_left += bet*2
                award_money = False
        elif took_spoon[0] and spoons_left == 1:
            finished = True
            second = True
            if award_money:
                money_left += bet
                award_money = False
        elif took_spoon[0] and spoons_left == 0:
            finished = True
            third = True
            if award_money:
                money_left += bet//2
                award_money = False
        elif spoons_left == 0:
            finished = True
            fourth = True

        spoon = pygame.image.load("spoon.png")
        lighter_spoon = pygame.image.load("lighter_spoon.png")
        if finished == False:
            canvas.blit(bg, (0, 0))
            canvas.blit(text_surface, (540, 10))
            canvas.blit(bet_text, (1020, 50))
            canvas.blit(round_text, (10, 630))
            canvas.blit(moneyleft_text, (1020, 20))
            if 451 < mouse_pos[0] < 612 and 400 < mouse_pos[1] < 631:  # hovering over first card
                card1 = pygame.transform.scale(dealt_cards[0][1].image, (151, 214))
                canvas.blit(card1, (455, 408))
            else:
                card1 = pygame.transform.scale(dealt_cards[0][1].image, (161, 230))
                canvas.blit(card1, (450, 400))
            if 630 < mouse_pos[0] < 791 and 402 < mouse_pos[1] < 633:  # hovering over second card
                card2 = pygame.transform.scale(dealt_cards[0][2].image, (151, 214))
                canvas.blit(card2, (635, 408))
            else:
                card2 = pygame.transform.scale(dealt_cards[0][2].image, (161, 230))
                canvas.blit(card2, (630, 400))
            if 811 < mouse_pos[0] < 971 and 402 < mouse_pos[1] < 632:  # hovering over third card
                card3 = pygame.transform.scale(dealt_cards[0][3].image, (151, 214))
                canvas.blit(card3, (815, 408))
            else:
                card3 = pygame.transform.scale(dealt_cards[0][3].image, (161, 230))
                canvas.blit(card3, (810, 400))
            if 990 < mouse_pos[0] < 1152 and 402 < mouse_pos[1] < 631:  # hovering over fourth card
                card4 = pygame.transform.scale(dealt_cards[0][4].image, (151, 214))
                canvas.blit(card4, (995, 408))
            else:
                card4 = pygame.transform.scale(dealt_cards[0][4].image, (161, 230))
                canvas.blit(card4, (990, 400))
            if 14 < mouse_pos[0] < 143 and 16 < mouse_pos[1] < 114:
                for i in range(spoons_left):
                    canvas.blit(lighter_spoon, (22 + i * 30, 22))
            else:
                for i in range(spoons_left):
                    canvas.blit(spoon, (22 + i * 30, 22))
            if not played_a_card and frame > 200:
                canvas.blit(play_warning, (335,270))
            elif frames_since_card_pressed > 200:
                canvas.blit(play_warning, (335,270))
            if dealt_cards[0][0].cards == []:  # if there's no new card for the user to look at
                canvas.blit(empty_pile, (220, 270))
            else:
                if 1153 > mouse_pos[0] > 991 and 382 > mouse_pos[1] > 152:  # hovering over next card up
                    next_card = pygame.transform.scale(dealt_cards[0][0].cards[0].image, (151, 214))
                    canvas.blit(next_card, (995, 155))
                else:
                    next_card = pygame.transform.scale(dealt_cards[0][0].cards[0].image, (161, 230))
                    canvas.blit(next_card, (990, 150))
        elif first:
            canvas.blit(playagain_resized, (0, 0))
            my_font = pygame.font.SysFont('Oswald-VariableFont_wght.ttf', 50, italic=True)
            spoon_number = my_font.render('YOU GOT THE FIRST SPOON!', False, (217, 217, 217))
            canvas.blit(spoon_number, (363, 230))
            my_font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 56)
            won_back = my_font.render('With your $'+str(bet)+' bet, you won $'+str(bet*2)+' back', False, (255, 255, 255))
            canvas.blit(won_back, (220, 282))
            my_font = pygame.font.Font('Caveat-VariableFont_wght.ttf', 25)
            money_left_text = my_font.render('Money left: $' + str(money_left), False, (255,255,255))
            canvas.blit(money_left_text, (1020, 20))
        elif second:
            canvas.blit(playagain_resized, (0, 0))
            my_font = pygame.font.SysFont('Oswald-VariableFont_wght.ttf', 50, italic=True)
            spoon_number = my_font.render('YOU GOT THE SECOND SPOON!', False, (217, 217, 217))
            canvas.blit(spoon_number, (358, 230))
            my_font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 56)
            won_back = my_font.render('With your $' + str(bet) + ' bet, you won $' + str(bet) + ' back', False, (255, 255, 255))
            canvas.blit(won_back, (220, 282))
            my_font = pygame.font.Font('Caveat-VariableFont_wght.ttf', 25)
            money_left_text = my_font.render('Money left: $' + str(money_left), False, (255, 255, 255))
            canvas.blit(money_left_text, (1020, 20))
        elif third:
            canvas.blit(playagain_resized, (0, 0))
            my_font = pygame.font.SysFont('Oswald-VariableFont_wght.ttf', 50, italic=True)
            spoon_number = my_font.render('YOU GOT THE THIRD SPOON!', False, (217, 217, 217))
            canvas.blit(spoon_number, (363, 230))
            my_font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 56)
            won_back = my_font.render('With your $' + str(bet) + ' bet, you won $' + str(bet//2) + ' back', False, (255, 255, 255))
            canvas.blit(won_back, (220, 282))
            my_font = pygame.font.Font('Caveat-VariableFont_wght.ttf', 25)
            money_left_text = my_font.render('Money left: $' + str(money_left), False, (255, 255, 255))
            canvas.blit(money_left_text, (1020, 20))
        elif fourth:
            canvas.blit(playagain_resized, (0, 0))
            my_font = pygame.font.SysFont('Oswald-VariableFont_wght.ttf', 50, italic=True)
            spoon_number = my_font.render('ALL 3 SPOONS WERE TAKEN!', False, (217, 217, 217))
            canvas.blit(spoon_number, (353, 230))
            my_font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 56)
            won_back = my_font.render('You lost your whole $'+str(bet)+' bet', False, (255, 255, 255))
            canvas.blit(won_back, (320, 282))
            my_font = pygame.font.Font('Caveat-VariableFont_wght.ttf', 25)
            money_left_text = my_font.render('Money left: $' + str(money_left), False, (255, 255, 255))
            canvas.blit(money_left_text, (1020, 20))
        pygame.display.update()
        pygame.time.Clock().tick(60)

start_screen()
