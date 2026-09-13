import numpy as np

heights2 = np.array([
                    [170, 165, 180, 175, 160, 185, 172, 168, 178, 162],
                    [190, 155, 182, 167, 173, 169, 177, 158, 188, 171]
                ])

weights2 = np.array([65, 58, 82, 74, 52, 90, 68, 61, 77, 55,
                    95, 48, 85, 60, 70, 63, 76, 50, 92, 66])

#print the first row
print(heights2[0])
#print the first column
print(heights2[:,0])
#mean of the weights
print(f"the mean is: {np.mean(weights2)}\nthe median is: {round(np.median(weights2,0))}\nthe standard deviation is: {np.std(weights2)}")
#sort the array
print(np.sort(weights2))