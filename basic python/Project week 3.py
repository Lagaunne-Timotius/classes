# template for "Stopwatch: The Game"
import simplegui
import math
import random
# define global variables
t=0
convert=str("0:00.0")
counter=0
death=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global convert
    minute=t//600
    second=float(t%600)/10
    if second<10:
        convert=str(minute)+":0"+str(second)
    else:
        convert=str(minute)+":"+str(second)
    str(convert)
       
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    global death,counter
    timer.stop()
    death+=1
    if (t%50)==0:
        counter+=1
def reset():
    global t,death,counter
    t=0
    format(t)
    death=0
    counter=0
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t+=1
    format(t)

# define draw handler
def draw(canvas):
    total=str(str(counter)+"/"+str(death))
    canvas.draw_text(convert,[100,150],50,"White")
    canvas.draw_text(total,[200,50],25,"Green")
# create frame
frame=simplegui.create_frame("STOPWATCH",300,300)

# register event handlers
frame.add_button("Start",start,50)
frame.add_button("Stop",stop,50)
frame.add_button("Reset",reset,50)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,tick)
# start frame
frame.start()
print convert
# Please remember to review the grading rubric
