import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("data.csv")
x, y = df["x"], df["y"]

# Fit line
m_fit, b_fit = np.polyfit(x, y, 1)

# Plot
plt.scatter(x, y, label="Data")
plt.plot(x, m_fit*x + b_fit, color="red", label="Best fit")
plt.plot(x, 2*x + 5, color="green", linestyle="--", label="True line")
plt.legend()
plt.savefig("fit_plot.png")
