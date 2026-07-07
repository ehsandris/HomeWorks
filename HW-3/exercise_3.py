import numpy as np 
scores = np.array([ 
    [18, 15, 20], 
    [12, 14, 16], 
    [20, 19, 18], 
    [10, 8, 15] 
])

scheme_A = np.array([0.5, 0.3, 0.2]) 
scheme_B = np.array([0.2, 0.3, 0.5]) 
scheme_C = np.array([0.1, 0.2, 0.7])

weight_matrix = np.vstack((scheme_A,scheme_B,scheme_C))
final_scores = scores @ weight_matrix.T

best_scheme_indices = np.argmax(final_scores, axis=1)

best_mean = np.mean(final_scores, axis=0)

best_mean_arg = np.argmax(best_mean)

scheme_D = np.array([0.2 , 0.4 , 0.4])

new_weight_matrix = np.vstack((weight_matrix, scheme_D))


print(best_scheme_indices)
print(best_mean_arg)
print(new_weight_matrix)
