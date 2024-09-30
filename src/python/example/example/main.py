import numpy as np
import pandas as pd

# Create a numpy array
array = np.array([1, 2, 3, 4, 5])

# Create a pandas DataFrame from the numpy array
df = pd.DataFrame(array, columns=['Values'])

# Perform some basic operations
df_sum = df['Values'].sum()
df_mean = df['Values'].mean()

# Print the results
print("DataFrame:\n", df)
print("Sum:", df_sum)
print("Mean:", df_mean)
