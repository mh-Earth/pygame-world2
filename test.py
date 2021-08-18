import pygame, math, sys
 
#Initiation
pygame.init()
screen = pygame.display.set_mode((500, 500))
 
#Constants
get_ticks = pygame.time.get_ticks
clock = pygame.time.Clock()
fps = 60
 
 
class Object():
    def __init__(self, rect):
        self.rect = rect
        self.ticks = 0
 
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
 
    def move(self, angle):
        rectAdd = self.calculate(angle)
        self.rect[0] += rectAdd[0]
        self.rect[1] += rectAdd[1]
         
    def calculate(self, angle):
        angleCheck = [0, 90, 180, 270, 45, 135, 225, 315]
        tanSafeAngle = angle
        while tanSafeAngle > 90:
            tanSafeAngle -= 90
        tanAngle = math.tan(math.radians(tanSafeAngle))
        if angle not in angleCheck:
            movement = [0, 0]
            x, num = self.directionCalculation(angle, 'side')
            movement[x] = num
            self.ticks += 1
            while self.ticks - tanAngle > 0:
                x, num = self.directionCalculation(angle, 'forward')
                movement[x] += num
                self.ticks -= tanAngle
            return movement
        else:
            angleMovement = {0 : (0, -1), 90 : (1, 0), 180 : (0, 1), 270 : (-1, 0),
                             45 : (1, -1), 135 : (1, 1), 225 : (-1, 1), 315 : (-1, -1)}
            return angleMovement[angle]
 
    def directionCalculation(self, angle, direction):
        directionDict = {'side' : {0 : (1, -1), 90 : (0, 1), 180 : (1, 1), 270 : (0, -1)},
                         'forward' : {0 : (0, 1), 90 : (1, 1), 180 : (0, -1), 270 : (1, -1)}}
        count = 0
        for angleComparison in directionDict[direction]:
            if angle > angleComparison and angle < angleComparison + 90:
                return directionDict[direction][angleComparison]


obj = Object([50, 50, 50, 50])
rotation = -100
for x in range(0, 100):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    screen.fill((0, 0, 0))
    obj.move(rotation)
    obj.draw()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
sys.exit()