import numpy as np 

importance = np.array([3, 8, 1, 9, 4, 7])

importance_1 = importance.reshape(-1,1)
importance_2 = np.expand_dims(importance, axis=1)

print(importance_1)
print(importance_2)

model_out = np.array([[[0.9]]])

model_out_1 = model_out.item()

model_out_2 = model_out[0,0,0]
print(model_out_1)
print(model_out_2)

notes = np.array([5, 10, 15, 20, 25]) 
pinned = notes[1:3].copy()
pinned[0] = 999 
print(notes) 

notes = np.array([5, 10, 15, 20, 25]) 
pinned = notes[1:3]
pinned[0] = 999 
print(notes)
