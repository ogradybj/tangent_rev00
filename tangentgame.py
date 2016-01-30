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
        self.rect.x = random.randrange(screen_width+10, screen_width+15)
 
    def update(self, speed):
        """ Called each frame. """
        self.dx = speed
        # Move block down one pixel
        self.rect.x -= self.dx
 
        # If block is too far down, reset to top of screen.
        if self.rect.x < -65:
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
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.on = False
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        pygame.draw.circle(self.image, (BLUE), (width/2, height/2), width/2, 5)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100,600)
        self.rect.y = random.randrange(50,350)
        self.xdir = 1
        self.ydir = 1

        self.dx = speed*2
        self.dy = speed*2

        self.theta = 0
        self.thetav = 0

    def update(self, speed):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        #pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        #self.rect.x = pos[0]
        #self.rect.y = pos[1]
        
        self.dx = speed*3
        self.dy = speed*3
        #print(self.on)
        #if self.on == False:    

        if self.rect.x >= 800:
            self.xdir = -1
        elif self.rect.x <= 0:
            self.xdir = 1
        if self.rect.y >= 390:
            self.ydir = -1
        elif self.rect.y <= 0:
            self.ydir = 1


        self.rect.x = self.rect.x+(self.xdir*self.dx)
        self.rect.y = self.rect.y+(self.ydir*self.dy)


    def orbit(self, speed, ballx, bally):
        
        #self.rect.x = self.rect.x-speed

        self.thetav = math.atan(speed/30)
        
        self.theta = math.atan((self.rect.y-bally)/(self.rect.x-ballx))


        self.xdir = 1*math.sin(self.theta)

        self.ydir = 1*math.cos(self.theta)

        self.dx = 30*math.sin(self.thetav)-speed
        self.dy = 30*math.cos(self.thetav)



        self.rect.x = self.rect.x+(self.xdir*self.dx)
        self.rect.y = self.rect.y+(self.ydir*self.dy)

    


        
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
 
for i in range(11):
    # This represents a blall
    ball = Ball(WHITE, 60, 60, speed)
 
    # Set a random location for the block
    ball.rect.x = random.randrange(screen_width/65)*65
    ball.rect.y = random.randrange(screen_height/65)*65
 
    # Add the block to the list of objects
    ball_list.add(ball)
    all_sprites_list.add(ball)
 
# Create a red player block
player = Player(WHITE, 20, 20, speed)
playerGroup = pygame.sprite.Group()
playerGroup.add(player)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
on = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 

 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
    
    time += 1
    if time % 300 == 0:
        speed +=.5
        

    # Calls update() method on every sprite in the list
    ball_list.update(speed)
    ii = 0
    for ball in ball_list:
        if pygame.sprite.collide_rect(player, ball):
            player.orbit(speed, ball.rect.x, ball.rect.y)


        #if pygame.sprite.collide_rect(player, ball):
         #   
          #  ii +=1


    if ii > 0:
        player.orbit(speed)

    else:
        player.update(speed)  



    score = time
    print(score)

 
    # Draw all the sprites
    ball_list.draw(screen)
    playerGroup.draw(screen)
 
    # Limit to 20 frames per second
    clock.tick(20)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
