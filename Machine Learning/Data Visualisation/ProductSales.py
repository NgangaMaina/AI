import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('company_sales_data.csv')

months = df['month_number']
facecream = df['facecream']
facewash  = df['facewash']
month_labels = ['Jan','Feb','Mar','Apr','May','Jun',
                'Jul','Aug','Sep','Oct','Nov','Dec']

x     = np.arange(len(month_labels))
width = 0.35

fig, ax = plt.subplots(figsize=(13, 6))

bars1 = ax.bar(x - width/2, facecream,
               width, color='#FF6B6B',
               edgecolor='black', linewidth=0.5,
               label='Face Cream')

bars2 = ax.bar(x + width/2, facewash,
               width, color='#4ECDC4',
               edgecolor='black', linewidth=0.5,
               label='Face Wash')

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 30,
            str(int(bar.get_height())),
            ha='center', va='bottom',
            fontsize=7.5, fontweight='bold')

for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 30,
            str(int(bar.get_height())),
            ha='center', va='bottom',
            fontsize=7.5, fontweight='bold')

ax.set_title('Monthly Sales — Face Cream vs Face Wash',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Units Sold', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(month_labels)
ax.legend(fontsize=11)
ax.grid(True, axis='y', linestyle='--', alpha=0.5)  # horizontal grid only

plt.tight_layout()
plt.savefig('facecream_facewash_bar.png', dpi=150)
plt.show()