import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NitroRush")

# Colors
GRASS = (40, 150, 60)
ROAD = (60, 60, 60)
WHITE = (255, 255, 255)

running = True

class Car:
    def __init__(self, name, x_pos, y_pos, speed):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed

    def move_left(self):
        if self.x_pos - 10 >= 200:
            self.x_pos -= 10
            
    def move_right(self):
        if self.x_pos + 10 + 40 <= 600:
            self.x_pos += 10

class Obstacle:
    def __init__(self, x_pos, y_pos, speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed

    def move_down(self):
        self.y_pos += self.speed


# Create game objects
obstacle = Obstacle(350, -50, 3)
c = Car("Player", 200, 200, 5)

while running:
    # Background (Grass)
    screen.fill(GRASS)

    # Road
    pygame.draw.rect(screen, ROAD, (200, 0, 400, 600))

    # Road boundaries
    pygame.draw.line(screen, WHITE, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, WHITE, (600, 0), (600, 600), 5)

    # Center line
    for y in range(0, 600, 60):
        pygame.draw.rect(screen, WHITE, (397, y, 6, 30))

    # CAR (Draw last so it appears on top of the road!)
    pygame.draw.rect(screen, (220, 40, 40), (c.x_pos, c.y_pos, 40, 70))

    # OBSTACLE
    pygame.draw.rect(screen, (30, 30, 30), (obstacle.x_pos, obstacle.y_pos, 40, 40))
    obstacle.move_down()

    # Reset obstacle if it leaves the screen
    if obstacle.y_pos > 600:
        obstacle.y_pos = -50
        obstacle.x_pos = random.randint(200, 560)

    # COLLISION DETECTION
    player_rect = pygame.Rect(c.x_pos, c.y_pos, 40, 70)
    obstacle_rect = pygame.Rect(obstacle.x_pos, obstacle.y_pos, 40, 40)

    if player_rect.colliderect(obstacle_rect):
        print("GAME OVER")
        running = False

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                c.move_left()

            if event.key == pygame.K_RIGHT:
                c.move_right()

    # Update the display every frame outside the event loop
    pygame.display.update()

pygame.quit()
