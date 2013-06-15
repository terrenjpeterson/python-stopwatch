# template for "Stopwatch: The Game"

import simplegui

# define global variables

t = 0
whole_stops = 0
attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    min = int(t / 600)
    t = t - min * 600
    xsec = int(t / 100)
    t = t - xsec * 100
    sec = int(t / 10)
    t = t - sec * 10
    return str(min) + ":" + str(xsec) + str(sec) + "." + str(t)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_button():
    timer.start()
    return

def stop_button():
    global attempts, whole_stops
    attempts = attempts + 1
    x = int(t / 10) * 10
    if t == x:
        whole_stops = whole_stops + 1
    else:
        whole_stops = whole_stops
    timer.stop()
    return

def reset_button():
    global t, whole_stops, attempts
    t = 0
    whole_stops = 0
    attempts = 0
    return

# define event handler for timer with 0.1 sec interval

def timer_handler():
    global t
    t = t + 1
    return

# define draw handler

def draw(canvas):
    canvas.draw_text(str(whole_stops) + "/" + str(attempts), [10, 100], 100, "White")
    canvas.draw_text(format(t), [10, 250], 100, "White")
    
# create frame

frame = simplegui.create_frame("stopwatch", 300, 300)

frame.set_draw_handler(draw)

# register event handlers

button1 = frame.add_button("Start", start_button)
button2 = frame.add_button("Stop", stop_button)
button3 = frame.add_button("Reset", reset_button)
timer = simplegui.create_timer(100, timer_handler)

# start frame

frame.start()

# Please remember to review the grading rubric
