import pygame
import time
import random
pygame.font.init()

#Window#
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

#background#
BG = pygame.transform.scale(pygame.image.load("BackgroundCloudTest.png"),(WIDTH, HEIGHT))
Coin = pygame.image.load("Coin20.png")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

Coin_Width = 20
Coin_Height = 20

FONT = pygame.font.SysFont("comicsans", 30)

#0,0 = top left, 1000,0 top right etc #

run = True

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "black", star)

    pygame.display.update()



def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)


    #Keeping track of time#
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0


    #storing different stars#
    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        time_score = str(round(elapsed_time, 2))

        if star_count > star_add_increment:
            for _ in range(10):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 25)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            WIN.fill((255, 0, 0))
            end_text = FONT.render("Game Over", 1, "Black")
            time_text = FONT.render("Time:", 1, "Black")
            time_end = FONT.render(str(time_score), 1, "Black")

            WIN.blit(end_text, (400, 325))
            WIN.blit(time_text, (400, 375))
            WIN.blit(time_end, (500, 375))
            pygame.display.update()

            pygame.time.delay(6000)
            break



        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__=="__main__":
    main()
