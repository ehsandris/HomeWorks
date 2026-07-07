import numpy as np

recipes = np.array([ 
    [15, 350, 2, 5], 
    [45, 600, 7, 10], 
    [10, 200, 0, 3], 
    [30, 450, 5, 7], 
    [60, 800, 8, 12] 
]) 

users = np.array([ 
    [10, 250, 1, 4], 
    [50, 700, 8, 11], 
    [25, 400, 4, 6] 
])

recipe_names = ["Salad", "Curry", "Toast", "Pasta", "Stew"]


max_recipes = np.max(recipes, axis=0)
min_recipes = np.min(recipes, axis=0)

recipes_scaled = (recipes - min_recipes) / (max_recipes - min_recipes)
users_scaled = (users - min_recipes) / (max_recipes - min_recipes)

recipes_scaled_reshaped = recipes_scaled.reshape(5,1,4)
users_scaled_reshaped = users_scaled.reshape(1,3,4)

food_dist = np.linalg.norm(recipes_scaled_reshaped - users_scaled_reshaped, axis=2).T

user_taste_ind = np.argmin(food_dist ,axis=1)

for user, recipe in enumerate(user_taste_ind):
    print(f"User {user} = {recipe_names[recipe]}")

for user, user_taste in enumerate(food_dist):

    print(f"\nUser {user}")

    indexes = np.argsort(user_taste)

    for ind in indexes:
        print(recipe_names[ind])