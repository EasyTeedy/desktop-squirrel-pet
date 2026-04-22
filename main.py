import sys
import os
import random
from PyQt5 import QtWidgets, QtGui, QtCore

# =====================
# GLOBAL STATE
# =====================
x = 550
y_start = 740

#def of the probability of each event:

death_left_array = [0]
death_right_array = [1]

gethurt_left_array = [2]
gethurt_right_array = [3]

eating_left_array = [4]
eating_right_array = [5]
eating_array = eating_left_array + eating_right_array

# probability trimming, just change the numbers in the arrays 
# IMPORTANT!!! left contains odd numbers and rigt contains even numbers for the check variable in the event logic and animation selection
digging_left_array = [10,12]
digging_right_array = [11,13]
digging_array = digging_left_array + digging_right_array

standing_left_array = [14,16,18]
standing_right_array = [15,17,19]
standing_array = standing_left_array + standing_right_array

headshaking_left_array = [20,22,24]
headshaking_right_array = [21,23,25]
headshaking_array = headshaking_left_array + headshaking_right_array

hopping_left_array = [26,28,30,32,34]
hopping_right_array = [27,29,31,33,35]
hopping_array = hopping_left_array + hopping_right_array


prbability_array_eating_digging = eating_left_array + eating_right_array + digging_left_array + digging_right_array

all_probability_array = digging_left_array + digging_right_array + standing_left_array + standing_right_array + headshaking_left_array + headshaking_right_array + hopping_left_array + hopping_right_array # max spann array is the number of all events that are not eating or get hurt or death, because those are only triggered by the event logic and not random
max_spann_array = len(all_probability_array) # max spann array is the number of all events that are not eating or get hurt or death, because those are only triggered by the event logic and not random


print ("max spann array:", max_spann_array) # DEBUG
print("min und max von max spann array:", all_probability_array[0], all_probability_array[-1]) # DEBUG
 # DEBUG

# state vor Death
death_bool = False # True = death, False = alive

# temporary variable for logic and loop
counter_hit = 0
cycle = 0
check = 0
target_duration = 0 # Dauer eines Events in Zyklen (100ms pro Zyklus)
event_number = random.randint(all_probability_array[0], all_probability_array[-1]) # start event, random number between min and max of the probability array, because the event logic triggers the eating and get hurt events and not random

# direction variable for the movement and animation selection
piss_on_wall_bool = False # True = hitting wall, False = not hitting wall
left_right_bool = False # 0 = rechts, 1 = links
direction = 1  # 1 = rechts, -1 = links

# path vor reading and saving gifs 

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

impath = resource_path("zugeschnitten_gifs/")

# =====================
# QT SETUP
# =====================
app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
window.setAttribute(QtCore.Qt.WA_TranslucentBackground)

label = QtWidgets.QLabel(window)
label.setStyleSheet("background: transparent;")

# =====================
# CLICK EVENT
# =====================

def on_click(event):
    global gethurt_left_array, gethurt_right_array
    global event_number, cycle, target_duration, left_right_bool, counter_hit

    counter_hit+=1
    event_number = gethurt_left_array[0] if left_right_bool == False else gethurt_right_array[0] # bool false = left if bool true = right
    cycle = 0

    target_duration = 8

    #target_duration = 80
    #event_number = random.choice(hopping_left_array)
    print("Event number:", event_number) # after get hurt the pet is more likely to hop, because it is scared, but it can also do any other event, just for more variety
# Mausklick aufgezeichnet und aufgerufen
label.mousePressEvent = on_click



# =====================
# Death hitting PET
# =====================
def death_trigger():
    global death_left_array, death_right_array, left_right_bool
    global counter_hit, event_number, target_duration, death_bool

    if counter_hit >= 5:
        event_number = death_left_array[0] if left_right_bool == False else death_right_array[0] # bool false = left if bool true = right
        #target_duration = 12
        death_bool = True

    #print("counter_hit:", counter_hit) # DEBUG


# =====================
# GIF LOADER
# =====================
def load_gif(path, frame_count):
    frames = []
    movie = QtGui.QMovie(path)
    for i in range(frame_count):
        movie.jumpToFrame(i)
        frames.append(movie.currentPixmap())
    return frames

# =====================
# LOAD GIFS
# =====================
death_right = load_gif(os.path.join(impath, 'death_right.gif'), 11)
death_left = load_gif(os.path.join(impath, impath+'death_left.gif'), 11)
digging_right = load_gif(os.path.join(impath,impath+'digging_right.gif'), 70)
digging_left = load_gif(os.path.join(impath, impath+'digging_left.gif'), 70)
eating_right = load_gif(os.path.join(impath, impath+'eating_right.gif'), 51)
eating_left = load_gif(os.path.join(impath, impath+'eating_left.gif'), 51)
get_hurt_right = load_gif(os.path.join(impath, impath+'get_hurt_right.gif'), 6)
get_hurt_left = load_gif(os.path.join(impath, impath+'get_hurt_left.gif'), 6)
head_shaking_right = load_gif(os.path.join(impath, impath+'head_shaking_right.gif'), 37)
head_shaking_left = load_gif(os.path.join(impath, impath+'head_shaking_left.gif'), 37)
hopping_right = load_gif(os.path.join(impath, impath+'hopping_right.gif'), 47)
hopping_left = load_gif(os.path.join(impath, impath+'hopping_left.gif'), 47)
standing_right = load_gif(os.path.join(impath, impath+'standing_right.gif'), 51)
standing_left = load_gif(os.path.join(impath, impath+'standing_left.gif'), 51)

# =====================
# EVENT CHOOSER
# =====================
def choose_next_event():
    global digging_left_array, digging_right_array, eating_left_array, eating_right_array
    global standing_left_array, standing_right_array, headshaking_left_array, headshaking_right_array, hopping_left_array, hopping_right_array
    global event_number, target_duration

    if event_number in digging_left_array or event_number in digging_right_array or event_number in eating_left_array or event_number in eating_right_array: # if number is in digging or eating arrays
        
        if random.random() < 2/3:  # 2x in more likely
            event_number = random.choice(prbability_array_eating_digging)
        else:
            event_number = random.randint(all_probability_array[0], all_probability_array[-1])
    else:
        event_number = random.randint(all_probability_array[0], all_probability_array[-1])

    # time of the animation besed on the event type
    
    #hopping duration
    if event_number in hopping_array:
        target_duration = 13 * random.randint(3, 10)
    
    # digging duration
    elif event_number in digging_array:
        target_duration =  50 * random.randint(1, 2)

    # eating duration
    elif event_number in eating_array:
        target_duration = 52 *random.randint(1, 3)

    # hit and death duration
    # is in the cklick logic set. becouse new duration is selecteted
    # after an animation is over!

    #head shaking duration
    elif event_number in headshaking_left_array or event_number in headshaking_right_array:
        target_duration = 12 * random.randint(1, 2)
    
    #standing duration
    elif event_number in standing_left_array or event_number in standing_right_array:
        target_duration = 12 * random.randint(3, 10)
    else:
        target_duration = 123

    print("event:", event_number, "target duration:", target_duration) # DEBUG

# =====================
# EVENT LOGIC (KEINE BEWEGUNG HIER!)
# =====================
def handle_event():
    global check, event_number, left_right_bool, direction, piss_on_wall_bool
    death_trigger()

    # connenctiong probability of an event withe the check variable 
    # for the animation selection in the update loop
    
    # variable check if odd or even 
    # for right left check in the animation selection in the update loop

    #death
    if event_number == death_left_array[0] and left_right_bool == False: # left death
        check = 0
        left_right_bool = False
    elif event_number == death_right_array[0]: # right death
        check = 1
        left_right_bool = True

    #digging
    elif event_number in digging_left_array:
        check = 2
        left_right_bool = False
        direction = -1
    elif event_number in digging_right_array:
        check = 3
        left_right_bool = True
        direction = 1

    #eating
    elif event_number in eating_array and left_right_bool == False: # left eating
        check = 4
        direction = -1
        #left_right_bool = False
    elif event_number in eating_array and left_right_bool == True: # right eating
        check = 5
        direction = 1
        #left_right_bool = True

    #standing
    elif event_number in standing_left_array:
        check = 6
        left_right_bool = False
        if piss_on_wall_bool == True: # if it is hitting a wall, it can randomly change direction or keep it, for more variety
            direction = random.choice([1, -1]) # if it is not hitting a wall, it can randomly change direction or keep it, for more variety
            piss_on_wall_bool = False # reset the bool for the next wall hit
            print("random direction:", direction) # DEBUG
        else:
            direction = -1
    
    elif event_number in standing_right_array:
        check = 7
        left_right_bool = True
        if piss_on_wall_bool == True: # if it is hitting a wall, it can randomly change direction or keep it, for more variety
            direction = random.choice([1, -1]) # if it is not hitting a wall, it can randomly change direction or keep it, for more variety
            piss_on_wall_bool = False # reset the bool for the next wall hit
            print("random direction:", direction) # DEBUG
        else:
            direction = 1
    
    #head shaking
    elif event_number in headshaking_array and left_right_bool == False:
        check = 8
        direction = -1
        
    elif event_number in headshaking_array and left_right_bool == True:
        check = 9
        direction = 1
    
    #hopping
    elif event_number in hopping_left_array:
        check = 10
        left_right_bool = False
        direction = -1
        print("pissbirne left")
    elif event_number in hopping_right_array:
        check = 11
        left_right_bool = True
        direction = 1
        print("pissbirne right")

    # get hurt
    elif event_number in gethurt_left_array:
        check = 12
    elif event_number in gethurt_right_array:
        check = 13

    else:
        print("Error: event_number not in any array", event_number, left_right_bool) # DEBUG

# =====================
# UPDATE LOOP
# =====================
def update():
    global cycle, check, event_number, x, direction,left_right_bool, piss_on_wall_bool, death_bool

    handle_event()
    #debugging
    #print(left_right_bool)
    print("event:", event_number, "check:", check, "x:", x, "dir:", direction, "left_right:", left_right_bool) # DEBUG

    # =====================
    # MOVEMENT
    # =====================
    if check == 10:
        x += 6 * direction
    elif check == 11:
        x += 6 * direction

    # WAND LOGIC (sauberer Turn)
    min_x = 328
    max_x = 1000

    if x >= max_x: # if it hits the right wall and is moving right, change direction to left
        piss_on_wall_bool = True 
        left_right_bool = False
        direction = -1
        event_number = hopping_left_array[0]

    elif x <= min_x: # if it hits the left wall and is moving left, change direction to right
        piss_on_wall_bool = True
        left_right_bool = True
        direction = 1
        event_number = hopping_right_array[0]

    # =====================
    # ANIMATION SELECTION
    # =====================

    #Death
    #print("check:", check) # DEBUG

    if check == 0:
        frames = death_left
    elif check == 1:
        frames = death_right
    
    #Digging
    elif check == 2:
        frames = digging_left
    elif check == 3:
        frames = digging_right
    
    #Eating
    elif check == 4:
        #print("try eating bool is:", right_left_checker_bool) # DEBUG
        frames = eating_left if left_right_bool == False else eating_right # direction check für sauberen Turn)
    elif check == 5:
        #print("try eating bool is:", right_left_checker_bool) # DEBUG
        frames = eating_right if left_right_bool == True else eating_left # direction check für sauberen Turn)
    #Standing
    elif check == 6:
        frames = standing_left
    elif check == 7:
        frames = standing_right
    
    #Head Shaking
    elif check == 8:
        frames = head_shaking_left
    elif check == 9:
        frames = head_shaking_right
    
    elif check == 10:
        frames = hopping_left if direction == -1 else hopping_right # direction check für sauberen Turn
    elif check == 11:
        frames = hopping_right if direction == 1 else hopping_left # direction check für sauberen Turn
    
    
    # Get Hurt
    elif check == 12:
        frames = get_hurt_left
    elif check == 13:
        frames = get_hurt_right


    # =====================
    # FRAME UPDATE
    # =====================
    frame = frames[cycle % len(frames)]
    label.setPixmap(frame)
    label.resize(frame.size())

    window.setGeometry(x, y_start, frame.width(), frame.height())

    # DEBUG
    #print("event:", event_number, "check:", check, "x:", x, "dir:", direction, "left_right:", right_left_checker_bool)

    # =====================
    # CYCLE + EVENT SWITCH
    # =====================
    cycle += 1

    if cycle >= target_duration:    
        if death_bool == True:
            print("PET is dead. restart to survive...") # DEBUG
            timer.stop()
        else:
            cycle = 0
            choose_next_event()

# =====================
# TIMER
# =====================
timer = QtCore.QTimer()
timer.timeout.connect(update)
#timer.start(50) #debugging
timer.start(100) # 100ms pro Zyklus
# =====================
# START
# =====================
window.show()
sys.exit(app.exec_())
