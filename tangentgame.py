"""
This is an iteration of the tangent game, using pygame and
Sprites
"""
 
import pygame
import random
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = ( 0,  0, 255)
 
 
class Ball(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    It is for the balls that will go across the screen
    """
    def __init__(self, color, width, height, speed):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        #super(pygame.sprite.Sprite, self).__init__()
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        pygame.draw.circle(self.image, (BLACK), (width/2, height/2), width/2, 5)
        self.rect = self.image.get_rect()
        self.dx= speed
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(screen_height/65)*65
        self.rect.x = random.randrange(screen_width*2+10, screen_width*2+15)
 
    def update(self, speed):
        """ Called each frame. """
        self.dx = speed
       
        self.rect.x -= self.dx
 
        # If ball has moved off screen, reset to new position
        if self.rect.x < -100:
            self.reset_pos()
 
 
class Player(Ball):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def __init__(self, color, width, height, speed):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        #super(pygame.sprite.Sprite, self).__init__()
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the ball, and fill it with a color.
        # May make sense to make an image later on
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.on = False
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        pygame.draw.circle(self.image, (BLUE), (width/2, height/2), width/2, 5)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(350,450)
        self.rect.y = random.randrange(175,225)
        self.xdir = 1 #math.sin(3.14159/4)
        self.ydir = 1 #math.cos(3.14159/4)

        self.dx = speed*1
        self.dy = speed*1

        self.theta = 0
        self.thetav = 0

    def update(self, speed, zball=None, cluck=False):
        
        




        if cluck == True:

            self.thetav = 0.033345*speed 
        
            self.theta = math.tan((self.rect.y-(zball.rect.center[1]))/(self.rect.x-(zball.rect.center[0])))

            
            #self.xdir = 1*math.sin(self.theta)
            #self.ydir = 1*math.cos(self.theta)
        

            #self.dx = 30*math.sin(self.thetav)-speed
            #self.dy = 30*math.cos(self.thetav)
            self.xdir = -1
            self.ydir = 0

        else:

            if self.rect.x >= 790:
                self.xdir = self.xdir*(-1)
            elif self.rect.x <= 10:
                self.xdir = self.xdir*(-1)
            if self.rect.y >= 390:
                self.ydir = self.ydir*(-1)
            elif self.rect.y <= 10:
                self.ydir = self.ydir*(-1)


        self.dx = speed*1*self.xdir
        self.dy = speed*1*self.ydir

        self.rect.x = self.rect.x+self.dx
        self.rect.y = self.rect.y+self.dy


    


        
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
score = 0
time = 0
speed = 1 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
ball_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
 #creating all the balls, randomly distributed
for i in range(15):
    # This represents a blall
    ball = Ball(WHITE, 60, 60, speed)
 
    # Set a random location for the block
    ball.rect.x = random.randrange(screen_width*2/65)*65+screen_width
    ball.rect.y = random.randrange(screen_height/85)*85
 
    # Add the ball to the list of objects
    ball_list.add(ball)
    all_sprites_list.add(ball)
 
# Create a blue ball for the player
player = Player(WHITE, 20, 20, speed)
playerGroup = pygame.sprite.Group()
#making player group, so that we can simply call
#playerGroup.draw(screen) otherwise if we add player to
#the ball sprite group, it will draw underneath the balls
playerGroup.add(player)
all_sprites_list.add(player)
 
# possibly use these later, still trying to work out orbit
done = False
on = None
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 

 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:# & guy.on == True:
            
            player.update(speed, on, False)
 
    # Clear the screen
    screen.fill(WHITE)
    
    #periodically increase the speed to make the game more difficult
    time += 1
    if time % 300 == 0:
        speed +=.5
        

    # Calls update() method on every ball in the list
    ball_list.update(speed)

    #check to see if player collides with any balls
    for ball in ball_list:
        #if there is a collision start orbiting the ball by
        #calling player.orbit method
        if pygame.sprite.collide_rect(player, ball):
            on = ball
            player.update(speed, on, True)
            print(ball.rect.center[0])
            print(ball.rect.center[1])


        #if no collision keep updating like normal
        else:
            player.update(speed)  


    #players score is simply amount of time they have survived
    score = time
    #print(score)
    #print(speed)
    #print(player.ydir)
    #print(player.xdir)


 
    # Draw all the sprites
    ball_list.draw(screen)
    playerGroup.draw(screen)
 
    # Limit to 20 frames per second
    clock.tick(24)
 
    #update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
