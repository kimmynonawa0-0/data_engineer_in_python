import numpy as np
height = [74, 74, 72, 75, 75, 73]
np_height_in = np.array(height)
print(f"height in python list: {height}") #python lists have comma
print(f"height in inches: {np_height_in}\ndata type: {type(np_height_in)}") #the numpy array doesnt have comma

#converting to meters
np_height_m = np_height_in * 0.0254
print(f"height in meters: {np_height_m}\ndata type: {type(np_height_in)}")