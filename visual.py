# Perquisites
import shapes as sh
import numpy as np
from matplotlib.patches import Rectangle, Circle, Polygon
import matplotlib.pyplot as plt


#!square
fig, ax = plt.subplots()
ax.plot([0, 0],[0, 0])
square = sh.Square(4)
ax.add_patch(Rectangle((1, 1), square.a, square.a))

# ! rhombus
fig, ax = plt.subplots()
ax.plot([0, 0],[0, 0])
square = sh.Square(4)
ax.add_patch(Rectangle((1, 1), square.a, square.a,angle=45))

# !circle
fig, ax = plt.subplots()
ax.plot([0, 0], [0, 0])
circle = sh.Circle(3)
ax.add_patch(Circle((1,1), circle.radius))

# !rectangle
fig, ax = plt.subplots()
ax.plot([0, 0],[0, 0])
rectangle = sh.Rectangle(4, 7)
ax.add_patch(Rectangle((1, 1), rectangle.a, rectangle.b))

# ! trapezoid
fig, ax = plt.subplots()
ax.plot([0, 0],[0, 0])
trapezoid = sh.Trapezoid(4, 6, 4, 6, 5)
x = [1,2,6,5,1]
y = [1,4,4,1,1]
ax.add_patch(Polygon(xy=list(zip(x,y))))

# ! triangle
fig, ax = plt.subplots()
ax.plot([0, 0],[0, 0])
x = [1,3,5,1]
y = [1,10,1,1]
ax.add_patch(Polygon(xy=list(zip(x,y))))


plt.show()