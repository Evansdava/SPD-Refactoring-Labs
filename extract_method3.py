# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math
xc1 = 4
yc1 = 4.25

xc2 = 53
yc2 = -5.35


# Calculate the distance between the two circle
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


distance = calculate_distance(xc1, yc1, xc2, yc2)
print('distance', distance)
# *** somewhere else in your program ***
xa = -36
ya = 97

xb = .34
yb = .91

# Calculate the length of the vector AB
length = calculate_distance(xa, ya, xb, yb)
print('length', length)
