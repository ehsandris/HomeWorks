import numpy as np
gym_data = np.array([ 
    [28, 75, 175, 4], 
    [34, 68, 168, 3], 
    [45, 82, 180, 2], 
    [22, 58, 162, 5], 
    [38, 90, 0, 1], 
    [29, 65, 170, 0] 
])

member_names = np.array(["Ali", "Sara", "Reza", "Neda", "Hassan", "Maryam"]) 
 
    
for col in range(1,4):

    column = gym_data[:, col]

    mean = np.mean(column[column != 0])

    gym_data[:, col] = np.where(
        column == 0,
        np.round(mean),
        column
    )

gym_data_without_ages = gym_data[:,1:]

heights = gym_data[:,2] / 100

BMI = gym_data[:,1] / (heights ** 2)

W1 = 0.7
W2 = 0.3

physical_fitness_score = np.round((BMI * W1) + (gym_data[:,3] * W2) , 1)

physical_fitness_score = np.expand_dims(physical_fitness_score, axis=1)

gym_data_without_ages = np.column_stack((gym_data_without_ages, physical_fitness_score))

best_person_ind = np.argmax(gym_data_without_ages[:,3])

best_person = member_names[best_person_ind]

person_sessions = gym_data_without_ages[:,2]

person_sessions_mean = np.mean(person_sessions)

person_sessions_diff = np.abs(person_sessions - person_sessions_mean)

person_sessions_std = np.std(person_sessions)

person_sessions_score = person_sessions_diff / person_sessions_std

max_sesson_person_ind  = np.argmax(person_sessions_score)

max_sesson_person  = member_names[max_sesson_person_ind]


print(best_person)
print(max_sesson_person)