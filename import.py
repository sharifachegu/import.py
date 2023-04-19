import math

def speed_of_fall(height):
    g = 9.81 # ускорение свободного падения
    t = math.sqrt((2 * height) / g) # время падения
    speed = g * t # скорость при падении
    return speed

print(speed_of_fall(100)) # 44.27188724235732
