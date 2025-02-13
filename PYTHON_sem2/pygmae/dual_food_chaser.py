import pygame
import random

pygame.init()

#Colors

food_color=(169,169,0)

# Creating Window

w_w=1200
w_h=600
game_window=pygame.display.set_mode((w_w,w_h))
pygame.display.set_caption("DUAL FOOD CHASER")

# Necessary after ever change in display

pygame.display.update()
fps=69
clock=pygame.time.Clock()
# For printing score on window

def screen_score(text,color,x,y,font=pygame.font.SysFont(None,33)):
     screen_text=font.render(text,True,color)
     game_window.blit(screen_text,[x,y])
     
# Creating Game Loop
def gameloop():
     # Specific Variable

     exit_game=False
     game_over=False

     p1_x=42
     p1_y=222
     p2_x=w_w-(p1_x*2)
     p2_y=222
     snake_size=20
     v_x=0
     v_y=0
     f_x=random.randint(0,w_w-100)
     f_y=random.randint(0,0)
     v2_x=0
     v2_y=0
     score=0
     score2=0
     while not exit_game:
          if game_over:
               for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                         exit_game=True
                    if event.type==pygame.KEYDOWN:
                         if event.key==pygame.K_KP_ENTER:
                              gameloop()
               game_window.fill((7,13,0))
               screen_score("YOU FUCKED UP",(250,200,69),w_w-769,w_h-380,pygame.font.SysFont(None,64))
               screen_score("Player :  "+str(score),(247,69,0),w_w-660,w_h-330)
               screen_score("Player :  "+str(score2),(0,169,69),w_w-660,w_h-300)
               pygame.display.update()
          else:
               for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                         exit_game=True
                    if event.type==pygame.KEYDOWN:
                              if event.key==pygame.K_d:
                                   v_x=10;v_y=0
                              elif event.key==pygame.K_a:
                                   v_x=-10;v_y=0
                              elif event.key==pygame.K_w:
                                   v_y=-10;v_x=0
                              elif event.key==pygame.K_s:
                                   v_y=+10;v_x=0
                              elif event.key==pygame.K_KP_6:
                                   v2_x=10;v2_y=0
                              elif event.key==pygame.K_KP_4:
                                   v2_x=-10;v2_y=0
                              elif event.key==pygame.K_KP_8:
                                   v2_y=-10;v2_x=0
                              elif event.key==pygame.K_KP_5:
                                   v2_y=+10;v2_x=0
                              elif event.key==pygame.K_ESCAPE:
                                   exit_game=True
                                   break
               p1_x+=v_x   
               p1_y+=v_y  
               p2_x+=v2_x   
               p2_y+=v2_y

               # For changing color
               b1=abs(p1_x-f_x)<15 and abs(p1_y-f_y)<15
               b2=abs(p2_x-f_x)<15 and abs(p2_y-f_y)<15
               gm_ov=abs(p1_x-p2_x)<17 and abs(p1_y-p2_y)<17
               if b1:
                    score+=1
                    f_x=random.randint(0,w_w-100)
                    f_y=random.randint(0,0)
                    pygame.draw.rect(game_window,food_color,[f_x,f_y,10,10])
                    pygame.display.update()
               elif b2:
                    score2+=1
                    f_x=random.randint(0,w_w-100)
                    f_y=random.randint(0,0)
                    pygame.draw.rect(game_window,food_color,[f_x,f_y,10,10])
                    pygame.display.update()

               elif gm_ov:
                    game_over=True
               pygame.display.update()
               game_window.fill((27,21,13))
               screen_score("Score : "+str(score),(247,69,0),13,w_h-27)
               screen_score("Score : "+str(score2),(0,169,69),1069,w_h-27)
                    
               if p1_x>1180:
                    p1_x=0
               elif p1_y>580:
                    p1_y=0
               elif p1_y<0:
                    p1_y=579
               elif p1_x<0:
                    p1_x=1179
               elif p2_x>1180:
                    p2_x=0
               elif p2_y>580:
                    p2_y=0
               elif p2_y<0:
                    p2_y=579
               elif p2_x<0:
                    p2_x=1179
               # For drawing a rectangle
               pygame.draw.rect(game_window,(247,69,0),[p1_x,p1_y,snake_size,snake_size])
               pygame.draw.rect(game_window,(0,169,69),[p2_x,p2_y,snake_size,snake_size])
               pygame.draw.rect(game_window,food_color,[f_x,f_y,10,10])
               f_y+=3
               if f_y>592:
                    f_y=0
                    f_x=random.randint(0,w_w-100)
                    pygame.draw.rect(game_window,food_color,[f_x,f_y,10,10])
                    pygame.display.update()
                    score = (score-1) if score!=0 else 0
                    score2 = (score2-1) if score2!=0 else 0
               elif f_y<0:
                    f_y=592
                    f_x=random.randint(0,w_w-100)
                    pygame.draw.rect(game_window,food_color,[f_x,f_y,10,10])
                    pygame.display.update()
                    score= (score-1) if score!=0 else 0
                    score2 = (score2-1) if score2!=0 else 0
               pygame.display.update()
               clock.tick(fps)
     pygame.quit()
     quit()
gameloop()

# For Screen end touch error 

'''
    if p1_x>1180:
         exit_game=1
    elif p1_y>480:
         exit_game=1
    elif p1_y<0:
         exit_game=1
    elif p1_x<0:
         exit_game=1
    elif p2_x>1180:
         exit_game=1
    elif pw_y>480:
         exit_game=1
    elif pw_y<0:
         exit_game=1
    elif p2_x<0:
         exit_game=1
    if exit_game==1:
         print("Game Over")
         screen_score("GAME OVER",(255,255,0),w_w-700,w_h-280,pygame.font.SysFont(None,64))
         screen_score("Player 1 :"+str(score),(255,0,0),w_w-620,w_h-210)
         screen_score("Player 2 :"+str(score2),(0,0,255),w_w-600,w_h-180)
'''