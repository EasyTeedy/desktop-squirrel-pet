# =====================
# GLOBAL VARIABLES
# =====================

# Probability arrays
death_left_array = [0]
death_right_array = [1]

gethurt_left_array = [2]
gethurt_right_array = [3]

eating_left_array = [4]
eating_right_array = [5]
eating_array = eating_left_array + eating_right_array

digging_left_array = [10, 12]
digging_right_array = [11, 13]
digging_array = digging_left_array + digging_right_array

standing_left_array = [14, 16, 18]
standing_right_array = [15, 17, 19]
standing_array = standing_left_array + standing_right_array

headshaking_left_array = [20, 22, 24]
headshaking_right_array = [21, 23, 25]
headshaking_array = headshaking_left_array + headshaking_right_array

hopping_left_array = [26, 28, 30, 32, 34]
hopping_right_array = [27, 29, 31, 33, 35]
hopping_array = hopping_left_array + hopping_right_array

prbability_array_eating_digging = eating_left_array + eating_right_array + digging_left_array + digging_right_array

all_probability_array = digging_left_array + digging_right_array + standing_left_array + standing_right_array + headshaking_left_array + headshaking_right_array + hopping_left_array + hopping_right_array
max_spann_array = len(all_probability_array)

# State
death_bool = False
counter_hit = 0
cycle = 0
check = 0
target_duration = 0
event_number = 0

# Position and direction
piss_on_wall_bool = False
left_right_bool = False
direction = 1
x = 0
y_start = 0
min_x = 328
max_x = 0

# Animation frames (will be set in main)
death_right = []
death_left = []
digging_right = []
digging_left = []
eating_right = []
eating_left = []
get_hurt_right = []
get_hurt_left = []
head_shaking_right = []
head_shaking_left = []
hopping_right = []
hopping_left = []
standing_right = []
standing_left = []
