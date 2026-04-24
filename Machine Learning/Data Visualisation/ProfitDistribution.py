import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('company_sales_data.csv')
profits = df['total_profit']

fig, ax = plt.subplots(figsize=(10, 6))

n, bins, patches = ax.hist(profits,
                            bins=6,
                            color='steelblue',
                            edgecolor='black',
                            linewidth=0.8,
                            alpha=0.85)

fracs = n / n.max()
norm  = plt.Normalize(fracs.min(), fracs.max())
for frac, patch in zip(fracs, patches):
    patch.set_facecolor(plt.cm.Blues(norm(frac)))


ax.axvline(profits.mean(),
           color='red', linestyle='--',
           linewidth=2, label=f'Mean: ${profits.mean():,.0f}')

ax.axvline(profits.median(),
           color='green', linestyle='-.',
           linewidth=2, label=f'Median: ${profits.median():,.0f}')

ax.set_title('Distribution of Monthly Profit\n(Most Common Profit Ranges)',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Profit Range (USD)', fontsize=12)
ax.set_ylabel('Number of Months', fontsize=12)
ax.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda val, _: f'${val:,.0f}'))
ax.legend(fontsize=11)
ax.grid(True, axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('profit_histogram.png', dpi=150)
plt.show()