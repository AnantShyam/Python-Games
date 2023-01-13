import pygame
import sys
import random

class Ball:
    def __init__(self):
        self.x = 300
        self.y = 300

    def draw_ball(self):
        pygame.draw.circle(screen, (0, 255, 0), 
        (self.x, self.y), 100, 20)

class Goal:
    def __init__(self):
        self.x = 200
        self.y = 100
        self.rect = None
    
    def draw_goal(self, y = 0):
        self.rect = pygame.Rect(self.x, y, 200, 20)
        pygame.draw.rect(screen, (255, 0, 255), self.rect)

class Defender:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = None
    
    def draw_defender(self, y = 40, x = 275):
        self.rect = pygame.Rect(x, y, 50, 20)
        pygame.draw.rect(screen, (255, 255, 0), self.rect)
        

        
pygame.init()

dimension = 600

screen = pygame.display.set_mode((dimension, dimension))
clock = pygame.time.Clock()

def update(rect):
    rect.x = 300
    rect.y = 300
    pygame.draw.rect(screen, (255, 0, 0), rect)
    pygame.display.update()

def main():
    ball = Ball()
    goal = Goal()
    goal2 = Goal()
    defender = Defender(275, 150)
    defender2 = Defender(275, 540)

    x = defender2.x
    x0 = defender.x

    ball_delt_x = 300
    ball_delt_y = 300

    score = [0, 0]

    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                sys.exit()
                
        screen.fill((0, 0, 0))
        ball.draw_ball()
        goal.draw_goal()
        goal2.draw_goal(dimension - 20)

        instructions = [
            "Instructions: Try to prevent the red ball from hitting your goal!",
            "Use the Left-Right Arrows and A-D keys to defend the goals",
            f"Score: {score[0]} - {score[1]}"
        ]

        font = pygame.font.SysFont("monospace", 15)

        labels = [
            font.render(instructions[i], 1, (255, 255, 0)) for i in range(len(instructions))
        ]
        for i in range(len(labels)):
            screen.blit(labels[i], (10, 100 + (i * 20)))

        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_LEFT] and x > 0:
            x-= 10
        if keys[pygame.K_RIGHT] and x < dimension - 51:
            x+= 10
        if keys[pygame.K_a] and x0 > 0:
            x0 -= 10
        if keys[pygame.K_d] and x0 < dimension - 51:
            x0 += 10

        slope = random.uniform(-1, 1)
        deltx = random.randint(-1, 1)
        if deltx == 0:
            deltx = -1

        # if the ball is in bounds
        x_in = ball_delt_x > 0 and ball_delt_x <= dimension - 25
        y_in = ball_delt_y > 0 and ball_delt_y <= dimension - 25

        if x_in and y_in:
            ball_delt_x += (50 * deltx)
            ball_delt_y += (50 * slope)
        else:
            if x_in and not y_in:
                ball_delt_y = 0 if ball_delt_y < 0 else dimension - 25
            elif not x_in and y_in:
                ball_delt_x = 0 if ball_delt_x < 0 else dimension - 25
            else:
                ball_delt_x = 300
                ball_delt_y = 300

            # continously keep updating slope
            slope = random.uniform(-1, 1)

        rect = pygame.Rect(ball_delt_x, ball_delt_y, 20, 20)
        pygame.draw.rect(screen, (255, 0, 0), rect)

        defender.draw_defender(40, x0)
        defender2.draw_defender(defender2.y, x)
        pygame.display.update()

        if rect.colliderect(defender) or rect.colliderect(defender2):
            rect.x = 300
            rect.y = random.randint(150, 540)
            pygame.draw.rect(screen, (255, 0, 0), rect)
            pygame.display.update()

        #check for a point being scored
        if rect.colliderect(goal.rect):
            score[0] += 1
            update(goal.rect)
        elif rect.colliderect(goal2.rect):
            score[1] += 1
            update(goal2.rect)

        clock.tick(10)

if __name__ == "__main__":
    main()