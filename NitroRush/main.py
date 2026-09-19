import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
ROAD_LEFT, ROAD_RIGHT = 200, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NitroRush")

clock = pygame.time.Clock()


class Car:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.width = 40
        self.height = 70

    def left(self):
        self.x -= self.speed

    def right(self):
        self.x += self.speed

    def draw(self):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.height)
        )

        # window
        pygame.draw.rect(
            screen,
            (100, 200, 230),
            (self.x + 7, self.y + 10, 26, 20)
        )

        # wheels
        pygame.draw.rect(
            screen, (20, 20, 20),
            (self.x - 4, self.y + 10, 5, 18)
        )

        pygame.draw.rect(
            screen, (20, 20, 20),
            (self.x + 39, self.y + 10, 5, 18)
        )

    def rect(self):
        return pygame.Rect(
            self.x, self.y,
            self.width, self.height
        )

class Enemy(Car):
    def move(self):
        self.y += self.speed

        if self.y > HEIGHT:
            self.reset()

    def reset(self):
        self.x = random.randint(
            ROAD_LEFT + 10,
            ROAD_RIGHT - self.width - 10
        )
        self.y = random.randint(-300, -100)


class Game:
    def __init__(self):
        self.player = Car(
            380, 480,
            (220, 40, 40),
            7
        )
        self.enemy = Enemy(
            350, -100,
            (40, 40, 40),
            5
        )
        self.score = 0
        self.running = True

        self.font = pygame.font.SysFont(
            "Arial", 28
        )

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.left()

        if keys[pygame.K_RIGHT]:
            self.player.right()

        # keep player on road
        self.player.x = max(
            ROAD_LEFT,
            min(
                self.player.x,
                ROAD_RIGHT - self.player.width
            )
        )

    def update(self):
        self.enemy.move()
        # score when enemy passes
        if self.enemy.y == self.enemy.speed - 100:
            self.score += 1

        # collision
        if self.player.rect().colliderect(
            self.enemy.rect()
        ):
            self.running = False


    def draw(self):
        # grass
        screen.fill((40, 150, 60))
        # road
        pygame.draw.rect(
            screen,
            (60, 60, 60),
            (ROAD_LEFT, 0, 400, HEIGHT)
        )

        # road borders
        pygame.draw.line(
            screen, "white",
            (ROAD_LEFT, 0),
            (ROAD_LEFT, HEIGHT), 5
        )

        pygame.draw.line(
            screen, "white",
            (ROAD_RIGHT, 0),
            (ROAD_RIGHT, HEIGHT), 5
        )

        # moving center line
        for y in range(0, HEIGHT, 80):
            pygame.draw.rect(
                screen,
                "white",
                (397, y, 6, 40)
            )
        # cars
        self.player.draw()
        self.enemy.draw()

        # score
        text = self.font.render(
            f"Score: {self.score}",
            True,
            "white"
        )
        screen.blit(text, (20, 20))
        pygame.display.update()

    def run(self):
        while self.running:
            clock.tick(60)

            self.events()
            self.update()
            self.draw()

        pygame.quit()

Game().run()

