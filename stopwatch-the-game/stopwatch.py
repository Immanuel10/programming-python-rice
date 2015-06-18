# template for "Stopwatch: The Game"

import simplegui
# define global variables

time = 0
points = 0
tries = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    seconds  =  t//1000 
    tenths =(t%1000)//100
    
    minutes = seconds//60
    seconds = seconds % 60 
    
    if seconds < 10:
        return str(minutes) + ":" + str(0) + str(seconds) + "." + str(tenths)
    else:
        return str(minutes) + ":" + str(seconds) + "." + str(tenths)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler1():
    timer.start()

def button_handler2():
    global time, tries, points
    if timer.is_running():
        timer.stop()
        if time %1000 == 0:
            points += 1            
        tries += 1
def button_handler3():
    global time, tries, points
    points = 0
    tries = 0
    time = 0
    timer.stop()
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    if timer.is_running():
        time += 100
    

timer = simplegui.create_timer(100, timer_handler)


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(format(time)), (60, 100), 35, 'white')
    canvas.draw_text((str(points) + "/" + str(int(tries))), [90, 40], 25, "White")

    
# create frame

frame = simplegui.create_frame('Stopwatch', 200, 200)
frame.set_draw_handler(draw_handler)
button1 = frame.add_button('Start', button_handler1, 50)
button2 = frame.add_button('Stop', button_handler2, 50)
button3 = frame.add_button('Reset', button_handler3, 50)


# register event handlers


# start frame
frame.start()
timer.start()



# Please remember to review the grading rubric
