import pygame 
import math
import sys

class Projectile:

    def __init__(self, velocity, angle):
        self.velocity = velocity
        self.angle = angle
        self.x = 100
        self.y = 400
    
    def draw_projectile(self):
        pygame.draw.circle(screen, (255, 0, 255), (self.x, self.y), 10, 0)

class Button:

    def __init__(self, text, color, left, top, width, height):
        self.color = color
        self.text = pygame.font.SysFont('Times New Roman', 18).render(text, True, (0, 0, 0))
        self.left = left
        self.top = top 
        self.width = width
        self.height = height 
        self.button = pygame.Rect(self.left, self.top, self.width, self.height)
    
    def draw_button(self):
        pygame.draw.rect(screen, self.color, self.button)
        screen.blit(self.text, (self.left, self.top + (self.height/8)))

pygame.init()
dimension = 600

screen = pygame.display.set_mode((dimension, dimension))
clock = pygame.time.Clock()

def main():
    proj = Projectile(10, math.pi)
    button1 = Button("Increase Initial Velocity", (255, 255, 255), 100, 500, 175, 25)
    running = True 
    clicked = False
    velocity = 0
    while running:
        # Draw TextBox to get User input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        screen.fill((0, 255, 0))
        proj.draw_projectile()
        button1.draw_button()

        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()