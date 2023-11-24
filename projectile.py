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
    
    def erase_projectile(self, x, y):
        pygame.draw.circle(screen, (0, 255, 0), (x, y), 10, 0)

    def move_along_x(self):
        velx = self.velocity * math.cos(self.angle)
        self.erase_projectile(self.x, self.y)
        self.x += velx 
        self.draw_projectile()

    def find_range(self):
        ang = self.angle * math.pi/180
        return (self.velocity ** 2) * math.sin(2 * ang)/10
    
    def find_max_height(self):
        ang = self.angle * math.pi/180
        maxheight = (self.velocity * math.sin(ang)) ** 2
        return maxheight/20
    
    def move(self):
        # calculate parabolic motion equation
        range = self.find_range()
        maxheight = self.find_max_height()
        h, k = 100 + range/2, maxheight + dimension - 400
        a = (dimension - 400 - k)/((100 - h) ** 2)
        
        # continuously move the projectile
        velx = self.velocity * math.cos(self.angle)
        self.erase_projectile(self.x, self.y)
        self.x += velx/2
        init_y = (a * ((self.x - h) ** 2)) + maxheight
        self.y += 800 - init_y
        self.draw_projectile()
        

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
    vbutton = Button("Increase Initial Velocity", (255, 255, 255), 100, 500, 175, 25)
    angbutton = Button("Increase Initial Angle", (255, 255, 255), 300, 500, 160, 25)
    vbutton2 = Button("Decrease Initial Velocity", (255, 255, 255), 100, 550, 175, 25)
    angbutton2 = Button("Decrease Initial Angle", (255, 255, 255), 300, 550, 160, 25)
    runbutton = Button("Run Simulation", (255, 255, 255), 300, 100, 120, 25)
    buttons = [vbutton, angbutton, vbutton2, angbutton2, runbutton]
    running = True 
    velocity = 0
    angle = 0
    proj = Projectile(velocity, angle)
    while running:
        # Draw TextBox to get User input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if the button1 is clicked
                for i in range(len(buttons)):
                    if mouse[0] >= buttons[i].left and mouse[0] <= buttons[i].left + buttons[i].width:
                        if mouse[1] >= buttons[i].top and mouse[1] <= buttons[i].top + buttons[i].height:
                            if i == 0 and velocity < 100:
                                velocity += 5
                            elif i == 1 and angle <= 90:
                                angle += 5
                            elif i == 2 and velocity > 0:
                                velocity -= 5
                            elif i == 3 and angle > 0:
                                angle -= 5
                            elif i == 4:
                                if velocity == 0:
                                    pass
                                else:
                                    proj.velocity = velocity
                                    proj.angle = angle
                                    while proj.x < proj.find_range():
                                        proj.move()
                                        pygame.display.update()
                                        clock.tick(10)
                                        
        instructions = [f"Initial Velocity: {velocity}", f"Initial Angle: {angle}"]
        font = pygame.font.SysFont('Times New Roman', 18)
        labels = [
            font.render(instructions[i], 1, (0, 0, 0)) for i in range(len(instructions))
        ]

        screen.fill((0, 255, 0))
        proj.draw_projectile()
        for button in buttons:
            button.draw_button()

        for i in range(len(labels)):
            screen.blit(labels[i], (10, 100 + (i * 20)))
        
        mouse = pygame.mouse.get_pos()

        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()