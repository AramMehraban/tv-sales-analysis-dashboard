import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/advertising.csv")

os.makedirs("reports", exist_ok=True)

# -------------------
# Correlation
# -------------------
corr = df.corr()

plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("reports/heatmap.png", dpi=300)
plt.close()

# -------------------
# Scatter Plot
# -------------------
plt.figure()
sns.scatterplot(x="TV", y="Sales", data=df)
plt.title("TV vs Sales")
plt.savefig("reports/scatter.png", dpi=300)
plt.close()

print("Analysis done")