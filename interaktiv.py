from globals import *

# =====================
# CLICK EVENT
# =====================

def on_click(event):
    global counter_hit, event_number, cycle, target_duration, left_right_bool

    counter_hit += 1
    event_number = gethurt_left_array[0] if not left_right_bool else gethurt_right_array[0] # bool false = left if bool true = right
    cycle = 0

    target_duration = 8

    #target_duration = 80
    #event_number = random.choice(hopping_left_array)
    print("Event number:", event_number) # after get hurt the pet is more likely to hop, because it is scared, but it can also do any other event, just for more variety


# =====================
# Death hitting PET
# =====================
def death_trigger():
    global counter_hit, event_number, target_duration, death_bool, left_right_bool

    if counter_hit >= 5:
        event_number = death_left_array[0] if not left_right_bool else death_right_array[0] # bool false = left if bool true = right
        #target_duration = 12
        death_bool = True

    #print("counter_hit:", counter_hit) # DEBUG