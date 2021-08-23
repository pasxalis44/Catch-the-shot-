import pygame_menu
import pygame, time, random
from pygame.locals import *
from pygame_menu import sound




BLACK = (  0,   0,   0)
AQUA=(0,170,225)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
hurt = pygame.mixer.Sound("hurt.mp3")
gain = pygame.mixer.Sound("gain.mp3")
sounds = pygame.mixer.Sound("bluescut.mp3")
lvl = pygame.mixer.Sound("level.mp3")
confetti_list1=[]
confetti_list2=[]
confetti_list3=[]

surface = pygame.display.set_mode((1850, 1000))


def ournames():
    
    surface.fill(BLACK)
    font = pygame.font.SysFont('8-BITWONDER.TXT', 28, True, False)
    text2 = font.render("Credits ", True, AQUA)
    surface.blit(text2, [100, 30]) 
    text3 = font.render('Made by Pashalis Antoniou and Mary Isari', True, AQUA)
    surface.blit(text3,[50,150])
    time.sleep(2)
    


def start_the_game():
   
    
    def main():   

        
    #Game variables 
   
        y_ground =910
        floor1=760
        floor2=570
        floor3=390
        floor4=320
        floor5=280
        floor6=130
        arial = pygame.font.SysFont("Arial", 18)
        quit = False
        x = 400
        #enemy pos
        #1set
        xen11=25
        yen11=910
        
       
        
        xen13=1780
        yen13=570
        
        xen14=170
        yen14=390
        
        
        finish=False

  
        air=False
        taken1=False
        taken2=False
        taken3=False
        taken4=False
        taken5=False
        taken6=False
        bg= pygame.image.load("pp1.png").convert()
        
        shoot=pygame.image.load("vac.png")
        pill1=pygame.image.load("pill1.png")
        pill2=pygame.image.load("pill2.png")
        pill3=pygame.image.load("pill3.png")

        shoot = pygame.transform.scale(shoot, (45, 55))   

        
        health = 30
        points = 0
        realpoints=0

        
       
        y = y_ground
        # standing still
        player_stand = pygame.image.load("doctor_front.png").convert_alpha()
        player_stand = pygame.transform.scale(player_stand, (45, 55))   
        
       
        # Jumping
        player_jump = pygame.image.load("doctor_jump.png").convert_alpha()
        player_jump = pygame.transform.scale(player_jump, (45, 55))   
        player_jump_frame = 0
        
        
        # Landing
        player_land = pygame.image.load("doctor_duck.png").convert_alpha()
        player_land = pygame.transform.scale(player_land, (45, 55))   
        # Create a list of images for walking left
        player_right = [
            pygame.image.load("doctor_walk2.png").convert_alpha(),
            pygame.image.load("doctor_walk3.png").convert_alpha(),
            pygame.image.load("doctor_walk4.png").convert_alpha(),
            pygame.image.load("doctor_walk5.png").convert_alpha(),
            pygame.image.load("doctor_walk.png").convert_alpha(),
            pygame.image.load("doctor_walk6.png").convert_alpha(),
            pygame.image.load("doctor_walk7.png").convert_alpha(),
            pygame.image.load("doctor_walk8.png").convert_alpha(),
        ]
        
        enemy_right = [
            pygame.image.load("virus2-1.png").convert_alpha(),
            pygame.image.load("virus2-2.png").convert_alpha(),
            pygame.image.load("virus2-3.png").convert_alpha(),
            pygame.image.load("virus2-4.png").convert_alpha(),
            pygame.image.load("virus2-5.png").convert_alpha(),
            pygame.image.load("virus2-6.png").convert_alpha(),
            pygame.image.load("virus2-7.png").convert_alpha(),
        ]
        #resize 
        player_right = [ pygame.transform.scale(image, (45, 55)) for image in player_right ]
        #size enemy
        enemy_right = [ pygame.transform.scale(image, (45, 55)) for image in enemy_right ]
    
        # Variable to remember which frame from the list we last displayed
        player_right_frame = 0
        enemy_right_frame = 0
    
        #  mirror
        player_left = [ pygame.transform.flip(image, True, False) for image in player_right ]
       
    
        player_left_frame = 0
        
    
        # Maintain  direction
        direction = "front"
        world_offset = [0,0]
        
        
        Front1=True
        Front2=True
        Front3=True
        Front4=True
        
        sounds.play()
        # Start game loop 
        while not quit:
            
            
            
            
            window.fill((64,64,64))                            # Reset screen 
            
            window.blit(bg, [0, 0])
            if taken1==False:
                window.blit(shoot, (1050, 912)) 
                
            if taken2==False:
                window.blit(shoot, (420, 762))
                
                
            if taken3==False:
                window.blit(pill1, (60, 780))
            if taken4==False:
                window.blit(pill2, (1470, 930))
            if taken5==False:
                window.blit(pill3, (60, 590))
            if taken6==False:
                window.blit(shoot, (675, 390))
               
            
            points_image = arial.render("Points:"+str(realpoints), 1, (255,255,255))
            health_image = arial.render("Health: "+str(int((health/10))), 1, (255,255,255) )
            window.blit(points_image, (50, 10))
            window.blit(health_image, (50, 30))
            #Process events 
            keyspressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    quit = True
            if keyspressed[ord("a")]:
                    x = x - 5
                    direction = "left"
            if keyspressed[ord("d")]:
             
                    x = x + 5
                    direction = "right"
           
            
              
          
            if keyspressed[ord("w")] and (((x>290 and x<330) and (y>760) or((x>1340  and x<1390) and (y>765)))):
               
                    y=y-10   
                
                    air=True
            if keyspressed[ord("w")] and ((x>885 and x<920) and ((y>570) and y<800)):
               
                    y=y-10   
                
                    air=True
            
            
            if keyspressed[ord("w")] and ((x>290 and x<330) and ((y>390) and y<580)):
               
                    y=y-10   
                
                    air=True
 
                 
            if keyspressed[ord("w")] and ((x>1475 and x<1520) and ((y>320) and y<600)):
               
                    y=y-10   
                
                    air=True
                    
            
            if keyspressed[ord("w")] and ((x>1655 and x<1690) and ((y>280) and y<600)):
               
                    y=y-10   
                
                    air=True
                    
                    
                    
                    
                    
                    
                    
            if keyspressed[ord("w")] and ((x>600 and x<650) and ((y>120) and y<400)):
               
                    y=y-10   
                
                    air=True
                    
        
                    
            if air==True:
                y=y+2
                window.blit(player_land, (x,y))

            if keyspressed[ord("s")]:
        
                    y=y+5 
            if sum(keyspressed) == 0:   # No key is pressed
                direction = "stand"
            # Your game logic here 
          
            if points>=30:
                window.fill((BLACK))
                font = pygame.font.SysFont('8-BITWONDER.TXT', 48, True, False)
                text2 = font.render("Congratulations you won !  Thanks for playing !", True, AQUA)
                window.blit(text2, [500, 500])
                direction = "stand"
                y=900
                x=100
                xen11=25
                yen11=910
                finish=True
              
                xen13=1780
                yen13=570
        
                xen14=170
                yen14=390
            
                
             
    
              
                for i in range(1):
                    x1=random.randrange(0,1850)
                    y1=random.randrange(0,1850)
                    pygame.draw.circle(window, AQUA, [x1,y1], 1)
                    confetti_list1.append([x1,y1])
                    
                for i in range(len(confetti_list1)):
                    pygame.draw.circle(window,AQUA,confetti_list1[i],3)
                    confetti_list1[i][1]+=1
                    if confetti_list1[i][1]>1850:
                        y1=random.randrange(-100,-80)
                        confetti_list1[i][1]=y1
                        x1=random.randrange(0,1850)
                        confetti_list1[i][0]=x1
                        
                for i in range(1):
                    x2=random.randrange(0,1850)
                    y2=random.randrange(0,1850)
                    pygame.draw.circle(window, GREEN, [x2,y2], 1)
                    confetti_list2.append([x2,y2])
                    
                for i in range(len(confetti_list2)):
                    pygame.draw.circle(window,GREEN,confetti_list2[i],3)
                    confetti_list2[i][1]+=1
                    if confetti_list2[i][1]>1850:
                        y2=random.randrange(-100,-80)
                        confetti_list2[i][1]=y1
                        x2=random.randrange(0,1850)
                        confetti_list2[i][0]=x1
                        
                for i in range(1):
                    x3=random.randrange(0,1850)
                    y3=random.randrange(0,1850)
                    pygame.draw.circle(window, RED, [x3,y3], 1)
                    confetti_list3.append([x3,y3])
                    
                for i in range(len(confetti_list3)):
                    pygame.draw.circle(window,RED,confetti_list3[i],3)
                    confetti_list3[i][1]+=1
                    if confetti_list3[i][1]>1850:
                        y3=random.randrange(-100,-80)
                        confetti_list3[i][1]=y3
                        x3=random.randrange(0,1850)
                        confetti_list3[i][0]=x3
                        
            if health < 1:
                window.fill((BLACK))
                
                font = pygame.font.SysFont('8-BITWONDER.TXT', 48, True, False)
                text2 = font.render("Unfortunately you lost  Thanks for playing ", True, AQUA)
                window.blit(text2, [500, 500])
                direction = "stand"
                y=900
                x=100
                xen11=40
                yen11=860
                finish=True
                
               
                
                xen13=1735
                yen13=545
                
                xen14=90
                yen14=370
                
                
                
                
            
           
        
          
              
                
               
                
               
                
    
                
                
                
                
                
                
                
                
                        
    
        
            

            if (x>= 1050 and x<= 1100) and (y>=910 and y<=920) and taken1==False :
                taken1=True
                gain.play()
                points+=10
                realpoints+=10
                
                
            
                
            if (x>= 400 and x<= 450) and (y>=760 and y<=780) and taken2==False :
                taken2=True
                gain.play()
                points+=10
                realpoints+=10
                
                
            if (x>= 40 and x<= 90) and (y>=760 and y<=780) and taken3==False :
                taken3=True
                gain.play()
                realpoints+=5
                
            if (x>= 1470 and x<= 1520) and (y>=910 and y<=930) and taken4==False :
                taken4=True
                gain.play()
                realpoints+=5
            
            if (x>= 60 and x<= 110) and (y>=570 and y<=590) and taken5==False :
                taken5=True
                gain.play()
                realpoints+=5
                
            if (x>= 675 and x<= 690) and (y>=390 and y<=400) and taken6==False :
                taken6=True
                gain.play()
                points+=10
                realpoints+=10
                
                
                
            if x < 0: 
                x = 0
            if x >= window.get_width()-50: 
                x = window.get_width()-50
            if y < 0: 
                y = 0
            
            if y >= y_ground: 
                y = y_ground
                
            if (y >= floor1  and y<=810)and ((x<940  or x>1390) and(x<300  or x>340) ): 
                y = floor1
            
            if (y >= floor2 and y<=690)and (x<880  or x>940): 
                y = floor2
                
            if (y >= floor3 and y<=450)and ((x<50  or x>160) and(x<740  or x>1800)and(x<300  or x>340)  ): 
                
                
                
                
                y = floor3
                
                
                
                
                
            if (y >= floor4 and y<=370)and ((x<50  or x>980)and(x<1480  or x>1780) ): 
                y = floor4
            
            if (y >= floor5 and y<=350)and (x<50  or x>1685): 
                y = floor5
                
            if (y >= floor6 and y<=220)and (x<610  or x>640): 
                y = floor6
            
           
    
    
        #MOVE ENEMIES
        #move set1
        #move enemt1
            if Front1==True and xen11<=1000:
                xen11+=5
            else:
                Front1=False
                
            if Front1==False and xen11>0:
                xen11-=5
            else:
                Front1=True
           
            
           #move enemt2
           
                
      
                
            #move enemt3
            if Front3==True and xen13<=1735:
                xen13+=5
            else:
                Front3=False
                
            if Front3==False and xen13>1285:
                xen13-=5
            else:
                Front3=True
                
                
            #move enemt4
            if Front4==True and xen14<=495:
                xen14+=5
            else:
                Front4=False
                
            if Front4==False and xen14>180:
                xen14-=5
            else:
                Front4=True
                
                
                
                
                
                
            #moveset2
            
            
                
    
            # Draw the player
            if direction == "left":
                window.blit(player_left[ player_left_frame ], (x,y))               
                player_left_frame = (player_left_frame + 1) % len(player_left)                  
            elif direction == "right":
                window.blit(player_right[ player_right_frame ], (x,y))                
                player_right_frame = (player_right_frame + 1) % len(player_right)                 
            elif direction == "jump":
                window.blit(player_jump, (x,y))
            
            else:
                window.blit(player_stand, (x,y))
                
            
         
            if x==xen11  and (y==yen11 or y==yen11-5 or y==yen11+5) :
                
                hurt.play()
                health=health-10
                
        
                
            if x==xen13  and (y==yen13 or y==yen13-5 or y==yen13+5):
                hurt.play()
                health=health-10
                
            if x==xen14 and (y==yen14 or y==yen14-5 or y==yen14+5):
                hurt.play()
                health=health-10 
            
           
                
                
            
            if finish==False:
               
               window.blit(enemy_right[ enemy_right_frame ], (xen11,yen11))  
                               
    
               window.blit(enemy_right[ enemy_right_frame ], (xen13,yen13))                
    
               window.blit(enemy_right[ enemy_right_frame ], (xen14,yen14)) 
          
                         
            
                
                
            enemy_right_frame = (enemy_right_frame + 1) % len(enemy_right)                 
        
    
            # Update screen 
            pygame.display.update()                         
            clock.tick(25)                                  

                              
    
    
    # Initialise & run the game 
    if __name__ == "__main__":
        width, height = 1850, 1000                          
        pygame.init()                                      
        pygame.mixer.init()                                 
        pygame.display.set_caption("Catch the shot!")   
        window = pygame.display.set_mode((width, height))   
        clock = pygame.time.Clock()                         
        main()
        pygame.quit()
                
    
    
    
    
    
    
#MENu
engine = sound.Sound()
engine.set_sound(sound.SOUND_TYPE_CLICK_MOUSE, 'Button.mp3')
engine.set_sound(sound.SOUND_TYPE_KEY_ADDITION, 'Button.mp3')
menu = pygame_menu.Menu(1000,  1850, 'Catch the shot!',
                       theme=pygame_menu.themes.THEME_DARK)
menu.set_sound(engine, recursive=True) 

menu.add_button('Play', start_the_game)
menu.add_button("Credits",ournames)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)