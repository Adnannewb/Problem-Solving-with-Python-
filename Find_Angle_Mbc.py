import math
AB = float(input())
BC = float(input())
angle_radians = math.atan(AB / BC)
angle_degrees = math.degrees(angle_radians)
print(f"{round(angle_degrees)}\N{DEGREE SIGN}")
