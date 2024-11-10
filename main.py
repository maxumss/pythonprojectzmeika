
# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
apple_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
eyeleft_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
eyeright_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

apple_pos.x = random.randint(11, 1269)
apple_pos.y = random.randint(11, 709)



while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("Green")

    pygame.draw.circle(screen, "red", apple_pos, 10 )
    pygame.draw.circle(screen, "dark green", player_pos, 20 )
    pygame.draw.circle(screen, "white", player_pos, 20 )

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos.y > 22 :
            player_pos.y -= 300 * 0.01
    if keys[pygame.K_s]:
        if player_pos.y < 698 :
            player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        if player_pos.x > 22 :
            player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        if player_pos.x < 1258:
            player_pos.x += 300 * dt

    appc = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # flip() the display to put your work on screen
    pygame.display.flip()

    for appcx in appc:
        appcxw = apple_pos.x + appc[appcx]

    for appcy in appc:
        appcyw = apple_pos.y + appc[appcy]

    if appcyw == player_pos.y :
        if appcxw == player_pos.x :
          apple_pos.x = random.randint(11, 1269)
          apple_pos.y = random.randint(11, 709)

    if appcxw == player_pos.x :
        if appcyw == player_pos.y :
          apple_pos.x = random.randint(11, 1269)
          apple_pos.y = random.randint(11, 709)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000



pygame.quit()
