import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output.csv")

plt.bar(df["category"], df["total:])
plt.xlabel("Category")
plt.ylabel("Total")
plt.title("Totals by Category")
plt.tight_layout()
plt.show()
