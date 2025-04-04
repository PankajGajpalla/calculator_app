import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 69, 19)

# Dino properties
dino_width, dino_height = 60, 80
dino_x = 50
dino_y = HEIGHT - dino_height - 50
dino_velocity = 0
gravity = 1
jump_strength = -20

try:
    dino_img = pygame.image.load("dino.png")
    dino_img = pygame.transform.scale(dino_img, (dino_width, dino_height))
except pygame.error:
    print("Error: dino.png not found. Using a red rectangle as a placeholder.")
    dino_img = pygame.Surface((dino_width, dino_height))
    dino_img.fill(RED)

# Obstacle properties
obstacle_width, obstacle_height = 40, 60
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 50
obstacle_speed = 8

try:
    obstacle_img = pygame.image.load("cactus.png")
    obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_width, obstacle_height))
except pygame.error:
    print("Error: cactus.png not found. Using a red rectangle as a placeholder.")
    obstacle_img = pygame.Surface((obstacle_width, obstacle_height))
    obstacle_img.fill(RED)

# Cloud properties
cloud_width, cloud_height = 80, 40
cloud_x = WIDTH
cloud_y = 50
cloud_speed = 2

try:
    cloud_img = pygame.image.load("cloud.png")
    cloud_img = pygame.transform.scale(cloud_img, (cloud_width, cloud_height))
except pygame.error:
    print("Error: cloud.png not found. Using a white rectangle as a placeholder.")
    cloud_img = pygame.Surface((cloud_width, cloud_height))
    cloud_img.fill(WHITE)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game states
game_over = False

# Function to draw dino
def draw_dino(x, y):
    screen.blit(dino_img, (x, y))

# Function to draw obstacle
def draw_obstacle(x, y):
    screen.blit(obstacle_img, (x, y))

#Function to draw cloud
def draw_cloud(x,y):
    screen.blit(cloud_img, (x,y))

# Function to display score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Function to display game over message
def display_game_over():
    game_over_text = font.render("Game Over! Press SPACE to restart.", True, RED)
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, text_rect)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                if dino_y == HEIGHT - dino_height - 50:
                    dino_velocity = jump_strength
            elif event.key == pygame.K_SPACE and game_over:
                game_over = False
                score = 0
                obstacle_x = WIDTH
                cloud_x = WIDTH
                dino_y = HEIGHT - dino_height - 50
                dino_velocity = 0

    if not game_over:
        # Background
        screen.fill(SKY_BLUE)
        pygame.draw.rect(screen, GROUND_BROWN, (0, HEIGHT - 50, WIDTH, 50))

        # Dino movement
        dino_y += dino_velocity
        dino_velocity += gravity
        if dino_y > HEIGHT - dino_height - 50:
            dino_y = HEIGHT - dino_height - 50
            dino_velocity = 0

        # Obstacle movement
        obstacle_x -= obstacle_speed
        if obstacle_x < -obstacle_width:
            obstacle_x = WIDTH + random.randint(100, 500)
            score += 1
            obstacle_speed += 0.2

        # Cloud Movement
        cloud_x -= cloud_speed
        if cloud_x < -cloud_width:
            cloud_x = WIDTH + random.randint(100, 500)
            cloud_y = random.randint(20,100)

        # Collision detection
        dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        if dino_rect.colliderect(obstacle_rect):
            game_over = True

        # Draw objects
        draw_dino(dino_x, dino_y)
        draw_obstacle(obstacle_x, obstacle_y)
        draw_cloud(cloud_x, cloud_y)
        display_score(score)

    else:
        display_game_over()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()