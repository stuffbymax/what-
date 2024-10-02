import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodger Game")

# Set up clock for controlling frame rate
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Falling object settings
object_width = 50
object_height = 50
object_speed = 5
object_list = []

# Score
score = 0
font = pygame.font.SysFont(None, 35)

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, [x, y, player_width, player_height])

def draw_object(obj):
    pygame.draw.rect(screen, RED, [obj[0], obj[1], object_width, object_height])

def display_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Update falling objects
    if random.randint(1, 20) == 1:  # Randomly add a new object
        object_list.append([random.randint(0, screen_width - object_width), -object_height])
    
    for obj in object_list:
        obj[1] += object_speed
        if obj[1] > screen_height:
            object_list.remove(obj)
            score += 1  # Increment score when object is avoided

    # Collision detection
    for obj in object_list:
        if (player_x < obj[0] < player_x + player_width or player_x < obj[0] + object_width < player_x + player_width) and \
           (player_y < obj[1] < player_y + player_height or player_y < obj[1] + object_height < player_y + player_height):
            running = False  # End game on collision

    # Draw player and objects
    draw_player(player_x, player_y)
    for obj in object_list:
        draw_object(obj)

    # Display score
    display_score(score)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
