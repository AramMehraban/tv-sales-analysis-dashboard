import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet

df = pd.read_csv("../data/advertising.csv")

os.makedirs("reports", exist_ok=True)

# images
scatter_path = "reports/scatter.png"
heatmap_path = "reports/heatmap.png"

# recreate plots if missing
sns.scatterplot(x="TV", y="Sales", data=df)
plt.savefig(scatter_path, dpi=300)
plt.close()

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.savefig(heatmap_path, dpi=300)
plt.close()

# PDF
doc = SimpleDocTemplate("reports/final_report.pdf")
styles = getSampleStyleSheet()
content = []

content.append(Paragraph("Sales Analysis Report", styles["Title"]))
content.append(Spacer(1, 10))

content.append(Paragraph("Correlation between TV ads and Sales", styles["Normal"]))
content.append(Spacer(1, 10))

content.append(Image(scatter_path, width=400, height=250))
content.append(Spacer(1, 10))

content.append(Image(heatmap_path, width=400, height=250))

doc.build(content)

print("PDF created")