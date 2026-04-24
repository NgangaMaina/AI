import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

products = ['facecream', 'facewash', 'toothpaste',
            'bathingsoap', 'shampoo', 'moisturizer']

annual_units = df[products].sum()

fig, ax = plt.subplots(figsize=(10, 7))

colors   = ['#FF6B6B', '#4ECDC4', '#45B7D1',
            '#96CEB4', '#FFEAA7', '#DDA0DD']
explode  = [0.03] * len(products)

wedges, texts, autotexts = ax.pie(
    annual_units,
    labels=products,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode,
    startangle=140,
    pctdistance=0.75,
    textprops={'fontsize': 11}
)

for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

legend_labels = [f"{p.capitalize()}: {int(v):,} units"
                 for p, v in zip(products, annual_units)]

ax.legend(legend_labels,
          loc='center left',
          bbox_to_anchor=(1.0, 0.5),
          fontsize=10,
          frameon=True,
          title='Annual Units Sold',
          title_fontsize=11)

ax.set_title('Number of Units Sold Per Product (Annual)\nAs Percentage of Total Units',
             fontsize=13, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('annual_units_pie.png', dpi=150, bbox_inches='tight')
plt.show()