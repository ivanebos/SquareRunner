'''
Super Crate Box Remake 2
By: Ivan Ebos

ToDo:
- Make update funtion loop
- Make gifs
- Add gif for each gun
- Randomize enemy spwn
- Bigger slower enemy
- If enemy reaches bottom respsond at top 100% faster
- End screen




Fix Bugs:
- Disk gun freezing
- Granade not bouncing
- Player falling too fast not on jump

Guns:
0 = pistol
1 = dual pistols
2 = revolor
3 = mechine gun
4 = mini gun
5 = mines
6 = granad langer
7 = rpg
8 = laser gun
9 = katana
10 = disk gun
11 = flamthrower
'''

#import libraries
import pygame
import random


#init
pygame.init()
win_height = 250
win_width = 550

#set window
window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Game")


#object enemys
class enemy:

    #init function
    def __init__(self):

        #position
        self.posx = random.randint(win_width/2- 10,win_width/2 + 10)
        self.posy = 0

        #speed
        self.vely = 0.1
        self.grav = 0.01
        self.velx = 0
           


        #atributes
        self.dim = 10
        self.drop = True
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)
        self.hit = False
        self.bottem = pygame.Rect(self.posx, self.posy + self.dim,self.dim,2)
        self.hit_right = pygame.Rect(self.posx + self.dim, self.posy, 2,self.dim)
        self.hit_left = pygame.Rect(self.posx,self.posy,2,self.dim)
        self.side = False
        self.start = True


    #update function
    def date(self):

        #check if object is droping
        if self.drop:
            
            #drop enemy
            self.posy += self.vely
            
            self.vely += self.grav

        
        self.posx += self.velx
        



        #draw hitbox
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)
        pygame.draw.rect(window,(0,0,0),self.hitbox)


        pygame.draw.rect(window, (255,0,0),self.hitbox,2)


        self.bottem = pygame.Rect(self.posx, self.posy + self.dim,self.dim,2)
        self.hit_right = pygame.Rect(self.posx + self.dim, self.posy, 2,self.dim)
        self.hit_left = pygame.Rect(self.posx,self.posy,2,self.dim)

        pygame.draw.rect(window,(0,255,0),self.bottem,2)
        pygame.draw.rect(window,(0,0,0),self.hit_right,2)
        pygame.draw.rect(window,(0,0,255),self.hit_left,2)


        #enemy hit side
        if self.posx  < 0 or self.posx + self.dim > win_width:
            self.change_dir()
            
            
        #enemy gets hit
        if self.hit:
            return True


    def change_dir(self):
        self.velx *= -1

    def move(self):

        if self.start:
            if random.randint(0,1) == 0:
                self.velx = -0.1
            else:
                self.velx = 0.1
            self.start = False
            
        

#BORDER CLASS
class border:

    #init function
    def __init__(self,posx,posy,height,width):

        #dimention
        self.posx = posx
        self.posy = posy
        self.height = height
        self.width = width

        #hit boxes
        self.hitbox = pygame.Rect(self.posx,self.posy, self.width,self.height)
        self.top = pygame.Rect(self.posx,self.posy,self.width,2)
        self.bottem = pygame.Rect(self.posx, self.posy + self.height,self.width,2)
        self.right = pygame.Rect(self.posx + self.width, self.posy, 2,self.height)
        self.left = pygame.Rect(self.posx,self.posy,2,self.height)

        #attributes
        self.color = (71, 255, 243)

    def draw(self):

        #draw boarder
        pygame.draw.rect(window,self.color,self.hitbox)

        #draw hit boxes
        pygame.draw.rect(window,(255,0,0),self.top,2)
        pygame.draw.rect(window,(0,255,0),self.bottem,2)
        pygame.draw.rect(window,(0,0,0),self.right,2)
        pygame.draw.rect(window,(0,0,255),self.left,2)

        
    
#player object
class player:

    #init player
    def __init__(self,posx,posy):

        #position
        self.posx = posx
        self.posy = posy
        
        #speed
        self.velocity = 0
        self.grav = 0.01

        #attributes
        self.dim = 20
        self.up = False
        self.right = True
        self.left = True
        self.is_right = False
        self.gun = 0
        self.move = False

        #hitboxes
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)
        self.top = pygame.Rect(self.posx,self.posy,self.dim,2)
        self.bottem = pygame.Rect(self.posx, self.posy + self.dim,self.dim,2)
        self.hit_right = pygame.Rect(self.posx + self.dim, self.posy, 2,self.dim)
        self.hit_left = pygame.Rect(self.posx,self.posy,2,self.dim)


    #draw player
    def draw(self):

        #set hitbox
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)
        self.top = pygame.Rect(self.posx,self.posy,self.dim,2)
        self.bottem = pygame.Rect(self.posx, self.posy + self.dim,self.dim,2)
        self.hit_right = pygame.Rect(self.posx + self.dim, self.posy, 2,self.dim)
        self.hit_left = pygame.Rect(self.posx,self.posy,2,self.dim)


        #draw body
        pygame.draw.rect(window,(128,0,0),self.hitbox)

        #draw hitbox
       # pygame.draw.rect(window,(255,0,0),self.hitbox,2)
        pygame.draw.rect(window,(255,0,0),self.top,2)
        pygame.draw.rect(window,(0,255,0),self.bottem,2)
        pygame.draw.rect(window,(0,0,0),self.hit_right,2)
        pygame.draw.rect(window,(255,0,255),self.hit_left,2)


        #draw pistol
        if self.gun == 0:
            
            #facing left
            if not self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx-5,self.posy + self.dim/2,15,2))
                
            #facing right
            elif self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx+ + 10,self.posy + self.dim/2,15,2))

        #draw dual pistl 
        elif self.gun == 1:
            pygame.draw.rect(window,(0,0,0),(self.posx-5,self.posy + self.dim/2,15,2))
            pygame.draw.rect(window,(0,0,0),(self.posx+ + 10,self.posy + self.dim/2,15,2))

        #draw revolvor
        elif self.gun == 2:

            #facing left
            if not self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx-5,self.posy + self.dim/2,15,4))

            #facing right
            elif self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx+ + 10,self.posy + self.dim/2,15,4))

        #draw mechine gun
        elif self.gun == 3:

            #facing left
            if not self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx-5,self.posy + self.dim/2,15,3))

            #facing right
            elif self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx+ + 10,self.posy + self.dim/2,15,3))

        #draw mini gun
        elif self.gun == 4:

            #facing left
            if not self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx-5,self.posy + self.dim/2,10,6))

            #facing right
            elif self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx+ + 10,self.posy + self.dim/2,10,6))

        elif self.gun == 5:

            #facing left
            if not self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx-5,self.posy + self.dim/2,10,6))

            #facing right
            elif self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx+ + 10,self.posy + self.dim/2,10,6))

        elif self.gun == 6:

            #facing left
            if not self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx-5,self.posy + self.dim/2,10,6))

            #facing right
            elif self.is_right:
                pygame.draw.rect(window,(0,0,0),(self.posx+ + 10,self.posy + self.dim/2,10,6))

                
    #move player right
    def move_right(self):
        if self.right:
            self.posx += 0.5

    #move player left
    def move_left(self):
        if self.left:
            self.posx += -0.5

    #player jumps
    def jump(self):
        self.velocity = 1.2
        self.up = True


    #player acted gravity
    def gravity(self):
        
        #if jumping
        if self.posy + self.dim < win_height and self.up:
            self.velocity -= self.grav
            self.posy -= self.velocity

        else:
            self.up = False

        if self.move:
            self.velocity = 0
            self.move = False


        

#pistol object
class pistol:

    #init pistol
    def __init__(self,direction,posx,posy):

        #speed
        self.velx = 0.8 * direction

        #position
        self.posx = posx
        self.posy = posy

        #atribults
        self.dim = 3
        self.color = (0,0,0)
        self.time = 150
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)
        self.hit = False
        self.col = False



    #draw function
    def draw(self):

        #draw hit box
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)

        #draw bullet
        pygame.draw.circle(window, self.color, (self.posx,self.posy), self.dim)
    


    #update function
    def date(self):

        #move bullet
        self.posx += self.velx

        #draw bullet
        self.draw()

        #check if bullet is out of screen
        if self.posx + self.dim > win_width or self.posx < 0 or self.hit or self.col:
            return True
       


#DUAL PISTOL CLASS
class dual_pistol:

    #init function
    def __init__(self,direction,posx,posy):

        #speed
        self.velx = 0.8 * direction

        #positions
        self.posx = posx
        self.posy = posy

        #atributes
        self.dim = 3
        self.color = (0,0,0)
        self.time = 150
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)
        self.hit = False
        self.col = False



    #draw function
    def draw(self):

        #draw hit box
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)
        
        #draw bullet
        pygame.draw.circle(window, self.color, (self.posx,self.posy), self.dim)
        
    #update bullet function
    def date(self):

        #move bullet
        self.posx += self.velx

        #draw bullet
        self.draw()

        #check if bullet out of screen
        if self.posx + self.dim > win_width or self.posx < 0 or self.hit or self.col:
            return True
       

#REVOLVER CLASS
class revolver:

    #init function
    def __init__(self,direction,posx,posy):

        #velocity
        self.velx = 1 * direction

        #position
        self.posx = posx
        self.posy = posy

        #attributs
        self.time = 150
        self.dim = 3.5
        self.color = (0,0,0)
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)
        self.hit = False
        self.col = False


    
    #draw funtion
    def draw(self):

        #draw hitbox
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)


        #draw bullet
        pygame.draw.circle(window, self.color, (self.posx,self.posy), self.dim)


     #update bullet function
    def date(self):

        #move bullet
        self.posx += self.velx

        #draw bullet
        self.draw()

        #check if bullet out of screen
        if self.posx + self.dim > win_width or self.posx < 0 or self.hit or self.col:
            return True

        
#MACHINE GUN CLASS
class machine:

    #init funtion
    def __init__(self,direction,posx,posy):

        #speed
        self.velx = 1 * direction

        #possition
        self.posx = posx
        self.posy = posy

        #attributs
        self.dim = 3
        self.time = 50
        self.color = (0,0,0)
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
        self.hit = False
        self.col = False


    #draw function        
    def draw(self):

        #draw hit box
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)

        #draw bullet
        pygame.draw.circle(window, self.color, (self.posx,self.posy), self.dim)

        
     #update bullet function
    def date(self):

        #move bullet
        self.posx += self.velx

        #draw bullet
        self.draw()

        #check if bullet out of screen
        if self.posx + self.dim > win_width or self.posx < 0 or self.hit or self.col:
            return True


#MINI GUN CLASS
class mini:

    #init function
    def __init__(self,direction,posx,posy):

        #position
        self.posx = posx
        self.posy = posy

        #atributs
        self.dim = 3
        self.time = 20
        self.hit = False
        self.col = False


        
        #velocity
        self.velx = 1 * direction
        self.vely = random.random()/3
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
        #random direction for vely
        if random.randint(0,1) == 0:
            self.vely *= -1

    #draw function  
    def draw(self):
        
        #draw hit box
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)


        #draw bullet
        pygame.draw.circle(window, (0,0,0), (self.posx,self.posy), self.dim)

    #update 
    def date(self):

        #move bullet
        self.posx += self.velx
        self.posy += self.vely

        #draw bullet
        self.draw()

        #check if bullet is out of screen
        if self.posx + self.dim > win_width or self.posx < 0 or self.posy < 0 or self.posy + player.dim > win_width or self.hit or self.col:
            return True


#DISC CLASS
class disk:

    #init funtion
    def __init__(self,direction,posx,posy):
        
        #speed
        self.velx = 1 * direction

        #position
        self.posx = posx
        self.posy = posy

        #atributies
        self.length = 15
        self.width = 4
        self.time = 300
        self.bounce = 0
        self.color  = (61, 61, 61)
        self.hitbox = pygame.Rect(self.posx,self.posy,self.length,self.width)
        self.col = False



    #draw function
    def draw(self):

        #draw hit box
        self.hitbox = pygame.Rect(self.posx,self.posy,self.length,self.width)
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)

        #draw bullet
        pygame.draw.rect(window,self.color,self.hitbox)

    #update function
    def date(self):

        #move bullet
        self.posx += self.velx

        #draw bullet
        self.draw()

        #check for first bounce
        if (self.posx + self.length >= win_width or self.posx <= 0) and self.bounce == 0 or self.col:

            #track bounce 
            self.bounce += 1

            #change dir of bullet
            self.velx *= -1

        #check when bullet leaves screen
        elif (self.posx + self.length >= win_width or self.posx <= 0) and self.bounce == 1:
            return True


#GRENADE CLASS
class grenade:

    #init funtion
    def __init__(self,direction,posx,posy):
        #speed
        self.velx = 0.8 * direction
        self.vely = -0.9
        self.grav = 0.01

        #position
        self.posx = posx
        self.posy = posy

        #atributies
        self.dim = 3
        self.time = 300
        self.bounce = 0
        self.color  = (0,0,0)
        self.stage = 0
        self.count = 0
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
        self.hit = False
        self.bounce_time = 0
        self.air_time = 750
        self.drag = -(0.0001 * direction)
        

    #draw function
    def draw(self):

        
        #draw granade
        if self.stage == 0:
            
            #draw hit box
            self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
            pygame.draw.rect(window, (255,0,0), self.hitbox,2)

            #draw bullet
            pygame.draw.circle(window, self.color, (self.posx,self.posy), self.dim)

        #draw explotion
        elif self.stage == 1 or self.hit:

            #count time
            self.count += 1

            #draw hit box
            self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
            pygame.draw.rect(window, (255,0,0), self.hitbox,2)

            #draw explotion
            pygame.draw.circle(window, (54, 54, 54), (self.posx,self.posy), self.dim)

        

    #update function
    def date(self):

        #increment time
        self.bounce_time += 1


        #move bullet with gravity
        if self.bounce_time < self.air_time and not self.hit:
            self.vely += self.grav
            self.velx += self.drag
            self.posx += self.velx
            self.posy += self.vely
        

        #draw bullet
        self.draw()

        #if bullets hit side
        if (self.posx + self.dim >= win_width or self.posx <= 0):


            #change dir of bullet
            self.velx *= -1

        #bullets hits bottem or top bullet will bounce unless already bounced for 5
        elif(self.posy <= 0 or self.posy + self.dim >= win_height):

            #change dir and set bullet to bottem
            self.bounce += 1
            self.vely *= -0.9
            self.posy = win_height - self.dim


            
        #if bullets bounces 6 times or bullet hits enemy
        if self.bounce_time == self.air_time or self.hit:

            #explode bullet
            self.stage = 1
            self.dim = 40
            

        #when explotion finishes return true
        if self.count == 100:
            return True

      
        

#RPG CLASS
class rpg:

    #init funtion
    def __init__(self,direction,posx,posy):
        
        #speed
        self.velx = 1 * direction

        #position
        self.posx = posx
        self.posy = posy

        #atributies
        self.length = 15
        self.width = 10
        self.dim = 20
        self.time = 300
        self.color = (0,0,0)
        self.stage = 0
        self.count = 0
        self.hitbox = pygame.Rect(self.posx,self.posy,self.length,self.width)
        self.hit = False

    #draw function
    def draw(self):

        #draw bullet
        if self.stage == 0:

            #draw hit box
            self.hitbox = pygame.Rect(self.posx,self.posy,self.length,self.width)
            pygame.draw.rect(window, (255,0,0), self.hitbox,2)

            #draw bullet
            pygame.draw.rect(window,self.color,self.hitbox)

        #draw explotion
        elif self.stage == 1:

            #count time
            self.count += 1

            #draw hit box
            self.hitbox = pygame.Rect(self.posx + self.length/2 -self.dim,self.posy + self.width/2-self.dim,self.dim*2,self.dim*2)
            pygame.draw.rect(window, (255,0,0), self.hitbox,2)

            #draw explotion
            pygame.draw.circle(window, (54, 54, 54), (self.posx + self.length/2,self.posy + self.width/2), self.dim)


    #update funtion
    def date(self):

        #move bullet
        if self.stage == 0:
            self.posx += self.velx

        #draw bullet
        self.draw()

        #check if bullet hits something
        if self.posx + self.length >= win_width or self.posx <= 0 or self.hit:
            self.stage = 1

        #check when explotion finishes
        if self.count == 100:
            return True


#FLAME THROWER CLASS
class flame:

    #init function
    def __init__(self,direction,posx,posy):

        #position
        self.posx = posx
        self.posy = posy

        #atributs
        self.dim = 3
        self.time = 10
        self.hit = False
        self.col = False
        self.color = (235, 134, 52)
        self.direction = direction
        self.count = False

        #velocity
        self.vely = random.random()/4

        if random.randint(0,1) == 1:
            self.vely *= -1


        self.velx = (random.randint(10,13)/20) * self.direction     
        self.drag = 0.001 * self.direction
        self.grav = 0.001

        
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)

        

    #draw function  
    def draw(self):
        
        #draw hit box
        self.hitbox = pygame.Rect(self.posx-self.dim,self.posy-self.dim,self.dim*2,self.dim*2)
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)


        #draw bullet
        pygame.draw.circle(window, self.color, (self.posx,self.posy), self.dim)

    #update 
    def date(self):


        self.vely += self.grav
        self.posx += self.velx
        self.velx -= self.drag
        self.posy += self.vely



        if self.direction > 0 and self.velx < 0 :
            self.velx = 0
            self.drag = 0

        elif self.direction < 0 and self.velx > 0 :
            self.velx = 0
            self.drag = 0


            
        
        #draw bullet
        self.draw()

        #check if bullet is out of screen
        if self.posx + self.dim > win_width or self.posx < 0 or self.posy < 0 or self.posy + player.dim > win_width or self.hit:
            return True



        if self.col:
            self.count += 1
            self.vely = 0
            self.grav = 0
            self.velx = 0
            self.drag = 0

        
        if self.count == 1000:
            return True







#CRATE CLASS
class crate:

    #init function
    def __init__(self):

        #speed
        self.vely = 0
        self.grav = 0.001
        self.posx = random.randint(10,win_width - 20)
        self.posy = random.randint(10,win_height -20)


        #attrubutes
        self.gun = random.randint(1,8)
        self.color = (255, 193, 107)
        self.dim = 10
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)
        self.bottem = pygame.Rect(self.posx, self.posy + self.dim,self.dim,2)
        self.col = False
        

    #draw funtion
    def draw(self):

        #update hit boxes
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)
        self.bottem = pygame.Rect(self.posx, self.posy + self.dim,self.dim,2)


        #draw create
        pygame.draw.rect(window, self.color, self.hitbox)

    #fall fuction
    def fall(self):

        #if not collided with boarder
        if not self.col:

            #move crate with gravity
            self.vely += self.grav
            self.posy += self.vely




#update function
def update(self):

    #each object in array
    for i in self:

        #update
        condition = i.date()

        #if out of screen
        if condition:
            self.remove(i)


#collition function
def collition(object1,object2):

    #each object in class 1
    for i in object1:
        
        #each object in class 2
        for j in object2:

            #init hit boxs
            hit1 = i.hitbox
            hit2 = j.hitbox

            #if hit boxes collides
            if hit1.colliderect(hit2):

                #set hit to true
                i.hit = True
                j.hit = True


#player collition function
def player_collition(object1):

    #init hit box
    hit1 = player.hitbox

    #for every enemy
    for i in object1:

        #init hit box
        hit2 = i.hitbox

        #if hot boxes collides
        if hit1.colliderect(hit2):
    
            #set to quit
            quit_funtion()


def border_player_collition(player,borders):

    #re init variables
    up_count = 0
    left_count = 0
    right_count = 0
    
        #loop in boarders
    for i in range(0,len(borders)):

        #bottem of player
        if player.bottem.colliderect(borders[i].top):
            player.up = False
        else:
            up_count += 1        

        #top of player
        if player.top.colliderect(borders[i].bottem):
            player.move = True

        #left of player
        if player.hit_left.colliderect(borders[i].right):
            player.left = False
        else:
            left_count += 1        
        
        #right of player
        if player.hit_right.colliderect(borders[i].left):
            player.right = False
        else:
            right_count += 1        


    #if top is collided stop player
    if up_count == len(borders):
        player.up = True

    #if left is collided stop player
    if left_count == len(borders):
        player.left = True
        
    #if right is collided stop player
    if right_count == len(borders):
        player.right = True


#colliton of enemys and borders
def border_enemy_collition(borders,enemys):

    #for each enemy
    for j in enemys:

        #reinit count
        count = 0

        #for each boarder
        for i in borders:
  
            #check if bottem of enemy and top of barder collide
            if i.top.colliderect(j.bottem):

                #increment count
                count += 1
            
        #if collition
        if count > 0:

            #set vely to 0
            j.vely = 0

            #enemy stops droping
            j.drop = False

            #start player moveing horizontal
            j.move()

        #if no collition
        else:
            
            #enemys starts droping
            j.drop = True


#collition for bullets with borders
def border_guns_collition(guns):

    #for every bullet
    for i in guns:

        #for every boarder
        for j in borders:

            #if collition
            if i.hitbox.colliderect(j.hitbox):

                #bullet collide is true
                i.col = True
        
    

#new bullet function
def new_one(player,gun):

    #player facing right
    if player.is_right:

        #return new bullet of gun
        return gun(1,player.posx + player.dim,player.posy + player.dim/2)

    #player facing left
    elif not player.is_right:
        
        #return new bullet of gun
        return gun(-1,player.posx ,player.posy + player.dim/2)



#collition top of boarder and bottem of enemy
def bottem_collition():

    #for each boarder
    for i in borders:

        #for each crate
        for j in crates:

            #if collition
            if i.top.colliderect(j.bottem):
                
                #stop gravity
                j.col = True        
            

            
#GAME OVER FUNCTION
def quit_funtion():
    print("game over")
    pygame.quit() 

    


#create new player
player = player(200,100)


#init var
time = 0
shoot = True
gun_time = 150
enemy_time = 2000
run = True

# init arrays




pistol_bullets = []
dual_pistol_bullets = []
revolver_bullets = []
machine_bullets = []
mini_bullets = []
disk_bullets = []
granade_bullets = []
rpg_bullets = []
flame_bullets = []

guns = []

enemys = []
borders = []
crates = []


#create boarders
borders.append(border(0,115,10,100))
borders.append(border(win_width-98,115,10,100))

borders.append(border(100,50,10,win_width-200))

borders.append(border(100,180,10,win_width-200))


borders.append(border(0,win_height-10,10,win_width/2 - 30))


borders.append(border(win_width/2 + 28,win_height-10,10,win_width/2 - 30))


#gameloop
while True:
    
    #fill window
    window.fill((255,255,255))
     

    #draw player
    player.draw()

    #keys hit
    keys = pygame.key.get_pressed()


    ###CHANGE GUNS####
    if (keys[pygame.K_0]):
        player.gun = 0
    if (keys[pygame.K_1]):
        player.gun = 1
    if (keys[pygame.K_2]):
        player.gun = 2
    if (keys[pygame.K_3]):
        player.gun = 3
    if (keys[pygame.K_4]):
        player.gun = 4
    if (keys[pygame.K_5]):
        player.gun = 5
    if (keys[pygame.K_6]):
        player.gun = 6
    if (keys[pygame.K_7]):
        player.gun = 7
    if (keys[pygame.K_8]):
        player.gun = 8
    ########

    ###MOVES PLAYER####
    #Move player left
    if (keys[pygame.K_a]) and 0 < player.posx:
        player.move_left()
        player.is_right = False
      # player.right = False

    #Move player right
    if (keys[pygame.K_d]) and win_width > player.posx + player.dim:
        player.move_right()
        player.is_right = True
       # player.right = True

    #player jump
    if (keys[pygame.K_w]) and not player.up:
        player.jump()
        player.posy -= 1
        player.velovity = 0
    ########


    #CREATE BULLET
    if (keys[pygame.K_SPACE]):

        #PISTOL
        if player.gun == 0 and not shoot:

            #create new bullet
            new_bullet = new_one(player,pistol)
            
            #create bullet
            pistol_bullets.append(new_bullet)

            #set time condtions
            shoot = True
            time = 0
            gun_time = new_bullet.time

        #DUAL PISTOL
        elif player.gun == 1 and not shoot:

            #create bullet for right
            new_bullet = dual_pistol(1,player.posx + player.dim,player.posy + player.dim/2)
            dual_pistol_bullets.append(new_bullet)

            #create bullet for left
            new_bullet = dual_pistol(-1,player.posx + player.dim,player.posy + player.dim/2)
            dual_pistol_bullets.append(new_bullet)

            #set time condtionds
            shoot = True
            time = 0
            gun_time = new_bullet.time

        #REVOLVER
        elif player.gun == 2 and not shoot:

            #new bullet
            new_bullet = new_one(player,revolver)

            #set time condtions
            shoot = True
            time = 0
            gun_time = new_bullet.time

            #create bullet
            revolver_bullets.append(new_bullet)

        #MACHINE GUN
        elif player.gun == 3 and not shoot:

            #new bullet
            new_bullet = new_one(player,machine)

            #set time condtions
            shoot = True
            time = 0
            gun_time = new_bullet.time

            #create bullet
            machine_bullets.append(new_bullet)
          

        #MINI GUN
        elif player.gun == 4 and not shoot:

            #new bullet
            new_bullet = new_one(player,mini)

            #set time condtions
            shoot = True
            time = 0
            gun_time = new_bullet.time

            #create bullet
            mini_bullets.append(new_bullet)


        #DISC GUN
        elif player.gun == 5 and not shoot:
            
            #new bullet
            new_bullet = new_one(player,disk)

            #set time condtions
            shoot = True
            time = 0
            gun_time = new_bullet.time

            #create bullet
            disk_bullets.append(new_bullet)


        #GRENADE
        elif player.gun == 6 and not shoot:
            
            #new bullet
            new_bullet = new_one(player,grenade)

            #set time condtions
            shoot = True
            time = 0
            gun_time = new_bullet.time

            #create bullet
            granade_bullets.append(new_bullet)
            
            
        #RPG
        elif player.gun == 7 and not shoot:
            
            #new bullet
            new_bullet = new_one(player,rpg)

            #set time condtions
            shoot = True
            time = 0
            gun_time = new_bullet.time

            #create bullet
            rpg_bullets.append(new_bullet)

        #FLAME THROWER
        elif player.gun == 8 and not shoot:
            
            #new bullet
            new_bullet = new_one(player,flame)

            #set time condtions
            shoot = True
            time = 0
            gun_time = new_bullet.time

            #create bullet
            flame_bullets.append(new_bullet)

            
        ##FOR LATER GUNS
        elif player.gun == 8:
            pass
        elif player.gun == 9:
            pass
        elif player.gun == 10:
            pass
        elif player.gun == 11:
            pass
        ##########

    #check collition for each
        '''
Make all bullets into single array to run in loop
'''
    collition(pistol_bullets,enemys)
    collition(dual_pistol_bullets,enemys)
    collition(revolver_bullets,enemys)
    collition(machine_bullets,enemys)
    collition(mini_bullets,enemys)
    collition(disk_bullets,enemys)
    collition(granade_bullets,enemys)
    collition(rpg_bullets,enemys)
    collition(flame_bullets,enemys)




    player_collition(enemys)
    player_collition(disk_bullets)

    #create new enemys every 2000
    if enemy_time == 2000:
        enemys.append(enemy())
        enemy_time = 0

    if len(crates) == 0:
        crates.append(crate())

    if not crates[0].col:
            crates[0].fall()

    if crates[0].hitbox.colliderect(player.hitbox):
        player.gun = crates[0].gun
        crates[0] = crate()


        


    
        

    bottem_collition()
        
    


    #border collitions
    border_player_collition(player,borders)
    border_enemy_collition(borders,enemys)

  
    for j in granade_bullets:
             
            #loop in boarders
        for i in borders:

            #bottem of player
            if j.hitbox.colliderect(i.top):
                j.vely *= -0.7
                   

            #top of player
            if j.hitbox.colliderect(i.bottem):
                j.vely *= -0.7
                

            #left of player
            if j.hitbox.colliderect(i.right):
                j.velx *= -1
            
            
            #right of player
            if j.hitbox.colliderect(i.left):
                j.velx *= -1
                  

           
    #draw borders
    for i in borders:
        i.draw()
        

    #incroment enemy time
    enemy_time += 1

    #MAKE INTO FUNCTIONS
    #Track for shooting space
    if shoot:
        time += 1
    if time == gun_time:
        shoot = False

    #REMAKE
    #update bullet
    update(pistol_bullets)
    update(dual_pistol_bullets)
    update(revolver_bullets)
    update(machine_bullets)
    update(mini_bullets)
    update(disk_bullets)
    update(granade_bullets)
    update(rpg_bullets)
    update(flame_bullets)


    #update enemy function
    update(enemys)


    #INCLUDE ALL GUNS
    border_guns_collition(pistol_bullets)
    border_guns_collition(dual_pistol_bullets)
    border_guns_collition(revolver_bullets)
    border_guns_collition(machine_bullets)
    border_guns_collition(mini_bullets)
    border_guns_collition(disk_bullets)
    border_guns_collition(granade_bullets)
    border_guns_collition(rpg_bullets)
    border_guns_collition(flame_bullets)



    #draw all creats
    for i in crates:
        i.draw()


    #player gravity
    player.gravity()
        
    #if user quits
    for event in pygame.event.get() : 

        if event.type == pygame.QUIT:
            pygame.quit() 


    #update window
    pygame.display.update() 
 
