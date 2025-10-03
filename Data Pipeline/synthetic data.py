import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
m, b = 2, 5
x = np.linspace(0, 10, 100)
noise = np.random.normal(0, 1, size=len(x))
y = m * x + b + noise

# Save to CSV
df = pd.DataFrame({"x": x, "y": y})
df.to_csv("data.csv", index=False)

print("✅ Data saved to data.csv")