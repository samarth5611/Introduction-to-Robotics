# Samartha Jadhao
# 2019BCS-026
import numpy as np

coordinates = np.array(list(map(float, input(
    "ENTER COORDINATES OF INTIAL"
    "POINT SEPERATED BY SPACES: ").split()))).reshape((3, 1))

ax = np.deg2rad(float(input("ENTER ROTAION ABOUT X AXIS: ")))
ay = np.deg2rad(float(input("ENTER ROTAION ABOUT Y AXIS: ")))
az = np.deg2rad(float(input("ENTER ROTAION ABOUT Z AXIS: ")))

valX = np.array([[1, 0, 0], [0, np.cos(ax), -np.sin(ax)], [0, np.sin(ax), np.cos(ax)]])

valY = np.array([[np.cos(ay), 0, np.sin(ay)], [0, 1, 0], [-np.sin(ay), 0, np.cos(ay)]])

valZ = np.array([[np.cos(az),  -np.sin(az), 0], [np.sin(az), np.cos(az), 0], [0, 0, 1]])

rotation = ((valX @ valY) @ valZ)
print("NEW COORDINATES: ", rotation@coordinates)	