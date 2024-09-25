from math import cos, sin

x, y, theta = input().split()
x = int(x)
y = int(y)
theta = float(theta)


new_x = x*cos(theta) - y*sin(theta)
new_y = x*sin(theta) + y*cos(theta)

print(new_x, new_y)