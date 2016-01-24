# Implementation of classic arcade game Pong

import simplegui
import random
import math
# initialize globals - pos and vel encode vertical info for paddles
#####
image = simplegui.load_image("https://uberfacts.files.wordpress.com/2013/02/asteroid.jpg")

# Image dimensions
MAP_WIDTH = image.get_width()
MAP_HEIGHT = image.get_height()

# Canvas size
CAN_WIDTH = MAP_WIDTH /3
CAN_HEIGHT = MAP_HEIGHT /3
#####

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos= [HALF_PAD_WIDTH, HALF_PAD_HEIGHT]
paddle2_pos= [WIDTH-HALF_PAD_WIDTH, HALF_PAD_HEIGHT]
paddle1_vel=[0,0]
paddle2_vel=[0,0] 
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,0]
score1=0
score2=0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):              
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if direction==LEFT:
        ball_vel=[-random.randrange(12, 24)/5,random.randrange(6, 18)/5]
    elif direction==RIGHT:
        ball_vel=[random.randrange(12, 24)/5,random.randrange(6, 18)/5]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints    
    score1=0
    score2=0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
#### 	
    canvas.draw_image(image, 
            [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT], 
            [WIDTH // 2, HEIGHT // 2], [WIDTH, HEIGHT])

###        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,4,"#FFCC33",'Black')
    # update paddle's vertical position, keep paddle on the screen
    canvas.draw_line([paddle1_pos[0],paddle1_pos[1]-HALF_PAD_HEIGHT],[paddle1_pos[0],paddle1_pos[1]+HALF_PAD_HEIGHT],8, 'Gray')
    canvas.draw_line([paddle2_pos[0],paddle2_pos[1]-HALF_PAD_HEIGHT],[paddle2_pos[0],paddle2_pos[1]+HALF_PAD_HEIGHT],8, 'Gray')
    
    if (paddle1_pos[1]==HALF_PAD_HEIGHT and paddle1_vel[1]<0):
        paddle1_vel[1]=0    
    elif (paddle1_pos[1]==HEIGHT-HALF_PAD_HEIGHT and paddle1_vel[1]>0):
        paddle1_vel[1]=0
    paddle1_pos[1]=paddle1_vel[1]+paddle1_pos[1]    
    
    if (paddle2_pos[1]==HALF_PAD_HEIGHT and paddle2_vel[1]<0):
        paddle2_vel[1]=0    
    elif (paddle2_pos[1]==HEIGHT-HALF_PAD_HEIGHT and paddle2_vel[1]>0):
        paddle2_vel[1]=0
    paddle2_pos[1]+=paddle2_vel[1]
    
        
    # determine whether paddle and ball collide    
    if (ball_pos[0]-BALL_RADIUS <=PAD_WIDTH): 
        if (math.fabs(paddle1_pos[1]-ball_pos[1])<=HALF_PAD_HEIGHT):
            ball_vel[0]=-1.5*ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score1+=1
            
    if (ball_pos[0]+BALL_RADIUS >=WIDTH-PAD_WIDTH):
        if (math.fabs(paddle2_pos[1]-ball_pos[1])<=HALF_PAD_HEIGHT):
            ball_vel[0]=-1.5*ball_vel[0]
        else:
            spawn_ball(LEFT)
            score2+=1
            
    if ((ball_pos[1]-BALL_RADIUS)) <=0 or (ball_pos[1]+BALL_RADIUS)>=HEIGHT:
        ball_vel[1]=-1.5*ball_vel[1] 
    # draw scores
    canvas.draw_text(str(score1),[0.75*WIDTH,0.2*HEIGHT],30,"White")
    canvas.draw_text(str(score2),[0.25*WIDTH,0.2*HEIGHT],30,"White")
    
    if score1==15:
        canvas.draw_text("Player1 win",[0,0.5*HEIGHT],100,"White")
        ball_pos=[WIDTH/2,HEIGHT/2]
        ball_vel=[0,0]
    elif score2==15:
        canvas.draw_text("Player2 win",[0,0.5*HEIGHT],100,"White")
        ball_pos=[WIDTH/2,HEIGHT/2]
        ball_vel=[0,0]
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP['up']:  
        paddle1_vel[1]= -10
    elif key==simplegui.KEY_MAP['down']:
        paddle1_vel[1]= +10
        
    if key==simplegui.KEY_MAP['w']: 
        paddle2_vel[1]= -10
    elif key==simplegui.KEY_MAP['s']: 
        paddle2_vel[1]= +10
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP['up']:
        paddle1_vel[1]= 0
    elif key==simplegui.KEY_MAP['down']:
        paddle1_vel[1]= 0
    if key==simplegui.KEY_MAP['w']:
        paddle2_vel[1]= 0
    elif key==simplegui.KEY_MAP['s']:
        paddle2_vel[1]= 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game",new_game,100)
frame.add_label('How to play')
frame.add_label('Use up and down for player 1 and w and s for player 2')
# start frame
new_game()
frame.start()
