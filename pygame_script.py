import pygame as p

# Engine init.
p.init()

# Display / display settings.
res = (800, 600)
screen = p.display.set_mode(res)
p.display.set_caption("Tic Tac Toe")
back_color = (255, 255, 255)
light_color = (170, 170, 170)
dark_color = (100, 100, 100)
width = screen.get_width()
height = screen.get_height()
small_button_font = p.font.SysFont('Corbel', 15)
large_button_font = p.font.SysFont('Corbel', 40)
choose_symbol = p.font.SysFont('Arial', 80)
play_symbol = p.font.SysFont('Arial', 200)
board_img = p.image.load('Images/tic_tac_toe_temp.png')

# Render contents contents.
one_player = small_button_font.render('One Player', False, (255, 255, 255))
two_players = small_button_font.render('Two Players', False, (255, 255, 255))
quit_button = large_button_font.render("Quit", False, (255, 255, 255))
single_text = small_button_font.render("Single Player Options:", False, (0, 0, 0))
x_select = choose_symbol.render("X", False, (0, 0, 0))
y_select = choose_symbol.render('Y', False, (0, 0, 0))


# Init game loop.
game_running = True
while game_running:

    mouse = p.mouse.get_pos()

    for event in p.event.get():
        # Exit the game with window button.
        if event.type == p.QUIT:
            p.quit()

        if event.type == p.MOUSEBUTTONDOWN:
            if 610 <= mouse[0] <= 690 and 10 <= mouse[1] <= 90:
                print("single player")
            elif 710 <= mouse[0] <= 790 and 10 <= mouse[1] <= 90:
                print("two player")
            elif 610 <= mouse[0] <= 790 and 505 <= mouse[1] <= 585:
                print('cya')
                p.quit()

    screen.fill((255, 255, 255))
    screen.blit(board_img, (0, 0))

    # Render player and quit buttons.
    if 610 <= mouse[0] <= 690 and 10 <= mouse[1] <= 90:
        p.draw.rect(screen, dark_color, [610, 10, 80, 80])
    else:
        p.draw.rect(screen, light_color, [610, 10, 80, 80])
    screen.blit(one_player, (615, 45))

    if 710 <= mouse[0] <= 790 and 10 <= mouse[1] <= 90:
        p.draw.rect(screen, dark_color, [710, 10, 80, 80])
    else:
        p.draw.rect(screen, light_color, [710, 10, 80, 80])
    screen.blit(two_players, (715, 45))

    if 610 <= mouse[0] <= 790 and 505 <= mouse[1] <= 585:
        p.draw.rect(screen, dark_color, [610, 505, 180, 80])
    else:
        p.draw.rect(screen, light_color, [610, 505, 180, 80])
    screen.blit(quit_button, (675, 530))

    # Render selection and difficulty buttons.
    if 610 <= mouse[0] <= 690 and 150 <= mouse[1] <= 240:
        p.draw.rect(screen, light_color, [610, 150, 80, 80])
    else:
        p.draw.rect(screen, (255, 255, 255), [610, 150, 80, 80])
    screen.blit(x_select, (628, 145))

    if 710 <= mouse[0] <= 790 and 150 <= mouse[1] <= 240:
        p.draw.rect(screen, light_color, [710, 150, 80, 80])
    else:
        p.draw.rect(screen, (255, 255, 255), [710, 150, 80, 80])
    screen.blit(y_select, (728, 145))

    # Render Text:
    screen.blit(single_text, (630, 110))

    p.display.update()
