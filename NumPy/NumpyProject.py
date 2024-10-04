import numpy as np

# Load the taxi data from the CSV file
taxi = np.genfromtxt(r'D:\Abdelraouf\Python_Libraries\Python_Libraries\NumPy\nyc_taxis.csv', delimiter=',', skip_header=True)

# Calculate the speed in miles per hour (mph)
speed = taxi[:, 7] / (taxi[:, 8] / 3600)

# Calculate the mean speed
mean_speed = speed.mean()
print(mean_speed)  # Print the mean speed

# Filter rides that occurred in February (month == 2)
rides_feb = taxi[taxi[:, 1] == 2, 1]
print(rides_feb.shape[0])  # Print the number of rides in February

# Filter and count the number of rides with a tip amount greater than $50
print(taxi[taxi[:, -3] > 50, -3].shape[0])

# Filter and count the number of rides with payment type 2 (credit card)
print(taxi[taxi[:, 6] == 2, 6].shape[0])
