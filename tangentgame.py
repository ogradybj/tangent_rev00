import pygame
import random
import math


#colors defined
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 220, 0)
RED = (220, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (235, 235, 35)

class Block(pygame.sprite.Sprite):
    """
    This class represents the blocks at either end of the game
    It derives from the "Sprite" class in Pygame
    """
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        #used to be listed as, but is incorrect: super(pygame.sprite.Sprite, self).__init__()
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, fill it with color and create variable for color.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.color = color
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        self.rect = self.image.get_rect()

    def update(self):
        """ as it is hit, it will turn from black to green to yellow to red, once red and is hit the game ends"""
        if self.color == BLACK:
            self.image.fill(GREEN)
            self.color = GREEN
        elif self.color == GREEN:
            self.image.fill(YELLOW)
            self.color = YELLOW
        elif self.color == YELLOW:
            self.image.fill(RED)
            self.color = RED
        elif self.color == RED:
            print("GAME OVER")


class Ball(pygame.sprite.Sprite):
    """
    This class is for the balls that fall across the screen.
    It extends the Sprite class in pygame
    """

    def __init__(self, diameter, speed):
        """ 
        initialize balls
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([diameter, diameter])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, (BLACK), (diameter/2, diameter/2), diameter/2, 6)
        self.rect = self.image.get_rect()
        self.dx = speed

    def reset_pos(self):
        """ Reset position to the right edge of the screen of the screen"""
        self.rect.y = random.randrange(330/65)*65
        self.rect.x = 800

    def update(self, speed):
        """ called each frame to update balls """
        self.dx = speed
        self.rect.x -= self.dx
        self.rect.y = self.rect.y + random.randrange(-2, 3)
        if self.rect.y < 10:
            self.rect.y = self.rect.y + 2
        if self.rect.y > 390:
            self.rect.y = self.rect.y - 2
        if self.rect.x < -80:
            self.reset_pos()

class Player(pygame.sprite.Sprite):
    """This class is the player/character that shows up on the screen
    and is controlled by the user. """
    def __init__(self, diameter, speed):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.Surface([diameter, diameter])
        self.image.fill(WHITE)
        self.on = False


        pygame.draw.circle(self.image, (BLUE), (diameter/2, diameter/2), diameter/2, 5)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 200
        self.xdir = -.707
        self.ydir = .707
        self.ii=0


        self.theta = 0
        self.rotdir = 1
        self.thetad = self.theta+self.rotdir*3.14159/2
        

        self.dx = speed*2*self.xdir
        self.dy = speed*2*self.ydir

    def click(self, click):
        ii = 0
    def update(self, speed, zball=None, cluck=False):

        """ISSUES IN THIS SECTION
        cannot get the orbit to work correctly"""
        if cluck == True:
            ii = self.ii
            if ii ==0:
                #self.theta = math.atan2((self.rect.center[1]-zball.rect.center[1]),(self.rect.center[0]-zball.rect.center[0]))
                ii +=1
            else:
                self.theta = speed + 0.1
            print(self.theta)
            self.rotdir = -1
            self.thetad = self.theta+self.rotdir*3.14159/2
            self.xdir = speed*1*math.cos(self.thetad)
            self.ydir = speed*1*math.sin(self.thetad)
            self.rect.x = zball.rect.center[0]+38*math.cos(self.theta+.1)-10
            self.rect.y = zball.rect.center[1]+38*math.sin(self.theta+.1)-10
            self.theta = self.theta+(self.rotdir*.09)

        
        #self.rect.x = zball.rect.center[0]+30*math.cos(self.theta+.15*self.rotdir)
        #self.rect.y = zball.rect.center[1]+30*math.sin(self.theta+.15*self.rotdir)



        elif cluck == False:
            if self.rect.x >= 770:
                self.xdir = self.xdir*(-1)
            elif self.rect.x <= 10:
                self.xdir = self.xdir*(-1)
            if self.rect.y >= 390:
                self.ydir = self.ydir*(-1)
            elif self.rect.y <= 5:
                self.ydir = self.ydir*(-1)
                self.rect.y = 6

            self.dx = speed*2*self.xdir
            self.dy = speed*2*self.ydir

            self.rect.x = self.rect.x+self.dx
            self.rect.y = self.rect.y+self.dy


#initialize Pygame
pygame.init()

#set screen size
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

time = 0
score = 0
speed = 2

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
ball_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
end1 = Block(BLACK, 12, 400)
end1.rect.x = 0
end1.rect.y = 0
block_list.add(end1)
end2 = Block(BLACK, 12, 400)
end2.rect.x = 788
end2.rect.y = 0
block_list.add(end2)
 #creating all the balls, randomly distributed
for i in range(9):
    # This represents a blall
    ball = Ball(60, speed)
 
    # Set a random location for the block
    ball.rect.x = i*98+screen_width
    ball.rect.y = random.randrange(330/65)*65
 
    # Add the ball to the list of objects
    ball_list.add(ball)
    all_sprites_list.add(ball)


# Create a blue ball for the player
player = Player(20, speed)
playerGroup = pygame.sprite.Group()
#making player group, so that we can simply call
#playerGroup.draw(screen) otherwise if we add player to
#the ball sprite group, it will draw underneath the balls
playerGroup.add(player)
all_sprites_list.add(player)
 
# possibly use these later, still trying to work out orbit
done = False
onball = None
colball = False
off = False
ii = 0
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            onball = None
            colball = False
            off = True
            click = True
            player.click(click)
            #player.update(speed, onball, colball)
 
    # Clear the screen
    screen.fill(WHITE)
    
    #periodically increase the speed to make the game more difficult
    time += 1
    if time % 500 == 0:
        speed +=.25
        

    

    #check to see if player collides with any balls
    for ball in ball_list:
        #if there is a collision start orbiting the ball by
        #calling player.orbit method


        if math.sqrt((player.rect.center[0]-ball.rect.center[0])**2+(player.rect.center[1]-ball.rect.center[1])**2) <=36:#pygame.sprite.collide_rect(player, ball):
            onball = ball
            colball = True
            player.theta = math.atan2((player.rect.center[1]-ball.rect.center[1]),(player.rect.center[0]-ball.rect.center[0]))
        
    for block in block_list:
        if pygame.sprite.collide_rect(player, block):
            block.update()
    # Calls update() method on every ball in the list
    ball_list.update(speed)
    player.update(speed, onball, colball)
        #if no collision keep updating like normal
        # else:
        #   onball = None
        #   colball = False
        #   player.update(speed, onball, colball) 

    score = time
    print(score)

    ball_list.draw(screen)
    block_list.draw(screen)
    playerGroup.draw(screen)
    

    clock.tick(24)

    pygame.display.flip()

pygame.quit()

