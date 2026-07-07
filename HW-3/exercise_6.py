import numpy as np 

bib_numbers = np.array([101, 102, 103, 104, 105, 106]) 
times_5k = np.array([22.3, 25.1, 21.8, 26.4, 23.0, 24.7])

bib_numbers_2 = np.array([107, 108]) 
times_5k_2 = np.array([20.5, 27.9])

bib_numbers = np.concatenate((bib_numbers,bib_numbers_2))
times_5k = np.concatenate((times_5k,times_5k_2))

np.random.seed(43)
random_index = np.random.permutation(len(bib_numbers))

bib_numbers = bib_numbers[random_index]
times_5k = times_5k[random_index]

score = np.argsort(times_5k)

print(bib_numbers)
print(times_5k)

for rank, i in enumerate(score, start=1):
    print(f"Rank {rank}: Bib {bib_numbers[i]} Time {times_5k[i]}")

def bib_detail(bib):
        if bib in bib_numbers:
              bib_index = np.where(bib_numbers == bib)[0][0]
              rank = np.where(score == bib_index)[0][0] + 1
              print(f"Bib {bib}")
              print(f"Time = {times_5k[bib_index]}")
              print(f"Rank = {rank}")
              

bib_detail(104)
