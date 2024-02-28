# program to show volume and surface area of cylinder
# volume = pir*2*h
# area = 2pirh * 2pirh
# example input radius = 24.2 height = 7.2
# volume = 1225.9 & surface area = 4332.5
import math

radius = float(input())
height = float(input())

volume = math.pi*pow(radius,2)*height
surfacearea = (2*math.pi*radius*height)*(2*math.pi*pow(radius,2))

print("volume:{:.if}".format(volume))
print("surface area:{:.if".format(surfacearea))