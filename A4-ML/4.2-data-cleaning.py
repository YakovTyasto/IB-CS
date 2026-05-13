
import numpy as np

# Create random array of values between 0 and 100
data = np.random.randint(0, 100, size=1000)

# Set one extreme value to act as an outlier
data[995] = 937

# Calculate outliers via Z-scores
mean = np.mean(data)
std_dev = np.std(data)

z_scores = (data - mean) / std_dev

threshold = 3  # Outliers if 3 stddev from mean
outliers = data[np.abs(z_scores) > threshold]

print("mean", mean, "stddev", std_dev)
print("Outliers:", outliers)

# Calculate outliers via IQR
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

iqr = q3 - q1
cutoff = 1.5 * iqr

lower_bound = q1 - cutoff
upper_bound = q3 + cutoff

outliers = data[(data < lower_bound) | (data > upper_bound)]

print("Outliers:", outliers)






































