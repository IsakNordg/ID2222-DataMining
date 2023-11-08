import numpy as np

# Create a sample matrix
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Permute the columns randomly
np.random.shuffle(matrix.T)

print(matrix)