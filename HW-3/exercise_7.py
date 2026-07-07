import numpy as np 

X_messages = np.array([ 
    [12, 0, 1], 
    [45, 5, 8], 
    [8, 0, 0], 
    [30, 3, 4] 
]) 



w = np.array([0.1, 0.8, 0.5]) 
b = -2.0

X = X_messages @ w + b

X = np.where(X < 0 , 0 , X)

#X = np.maximum(0, X)

labels = np.where(X > 5 , "Energetic", "Normal")

print(X)
print(labels)