import pygame
import random
pygame.init()

#Colors

food_color=(0,169,0)

# Creating Window

w_w=1200
w_h=500
game_window=pygame.display.set_mode((w_w,w_h))
pygame.display.set_caption("Snake game")
# Necessary after ever change in display
#--pygame.display.update()
clock=pygame.time.Clock()


# For printing score on window

def screen_score(text,color,x,y,font=pygame.font.SysFont(None,33)):
     screen_text=font.render(text,True,color)
     game_window.blit(screen_text,[x,y])

def draw_snake(game_window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])


# Creating Game Loop
def gameloop():
     # Specific Variable
     exit_game=False
     game_over=False
     snake_x=42
     snake_y=42
     snake_size=20
     v_x=0
     v_y=0
     f_x=random.randint(0,w_w-100)
     f_y=random.randint(69,w_h-100)
     fps=51
     score=0
     
     snake_list=[]
     snake_length=1
     while not exit_game:
          if game_over:
               for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                         exit_game=True
                    if event.type==pygame.KEYDOWN:
                         if event.key==pygame.K_KP_ENTER:
                              gameloop()
               game_window.fill((100,0,0))
               screen_score("GAME OVER",(255,255,0),w_w-700,w_h-280,pygame.font.SysFont(None,64))
               screen_score("Final Score :"+str(score),(255,255,255),w_w-620,w_h-210)
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
               snake_x+=v_x   
               snake_y+=v_y  

               # For changing color
               
               if abs(snake_x-f_x)<15 and abs(snake_y-f_y)<15:
                    score+=1
                    f_x=random.randint(0,w_w-100)
                    f_y=random.randint(60,w_h-100)
                    pygame.draw.rect(game_window,food_color,[f_x,f_y,10,10])
                    snake_length+=5
               game_window.fill((27,21,13))
               screen_score("Score : "+str(score),(255,255,255),7,w_h-27)
               if snake_x>1180 or snake_y>480 or snake_y<0 or snake_x<0:
                    game_over=True
               
               head=[]
               head.append(snake_x)
               head.append(snake_y)
               if head in snake_list[:-1]:
                    game_over=True
               snake_list.append(head)
               
               # For drawing a rectangle
               
               draw_snake(game_window,(255,0,0),snake_list,snake_size)
               
               if len(snake_list)>snake_length:
                    del snake_list[0]
               pygame.draw.rect(game_window,food_color,[f_x,f_y,10,10])
          pygame.display.update()
          clock.tick(fps)
     pygame.quit()
     quit()
gameloop()