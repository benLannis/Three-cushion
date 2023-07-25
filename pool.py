import pygame, sys

# First thing in any pygame program - initializes pygame's internal variables.
pygame.init()

# initialize a window with the screen size you set
size = width, height = 1000, 500
screen = pygame.display.set_mode(size)

# create a clock, which will be used to control the program's frame rate
clock = pygame.time.Clock()

# global variables
cueball_pos = (50, 50)

running = True
while running:
    # tick forward at 60 frames per second
    clock.tick(60)

    # This for loop gets any keyboard, mouse, or other events that happen from user input
    for event in pygame.event.get():
        # The pygame.QUIT event happens when someone tries to close the game window.
        if event.type == pygame.QUIT:
            running = False
        # pygame.MOUSEBUTTONDOWN occurs when the user clicks any mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Events will include what button was pushed, which you can check in if statements
            if event.button == pygame.BUTTON_LEFT:
                print("pressed")
        # if event.type == pygame.KEYDOWN:
        #     # KEYDOWN happens when a keyboard key is pressed. You can check the key with event.key.
        #     if event.key == pygame.K_SPACE:

    # Fill the screen with a solid color
    screen.fill((20, 255, 20))

    # Draw Cue Ball
    pygame.draw.circle(screen, (255, 255, 255), cueball_pos, 20)

    #At the end of each game loop, call pygame.display.flip() to update the screen with what you drew.
    pygame.display.update()
pygame.quit()
