import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('company_sales_data.csv')

months  = df['month_number']
profits = df['total_profit']
month_labels = ['Jan','Feb','Mar','Apr','May','Jun',
                'Jul','Aug','Sep','Oct','Nov','Dec']

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(months, profits,
        color='purple',
        linewidth=3,
        linestyle='--',
        marker='s',
        markersize=8,
        markerfacecolor='red',
        markeredgecolor='black',
        markeredgewidth=1.5,
        alpha=0.85,
        label='Total Profit')

ax.fill_between(months, profits,
                alpha=0.15,
                color='purple',
                label='Profit Area')

ax.set_title('Total Monthly Profit — Styled Line Plot',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Total Profit (USD)', fontsize=12)
ax.set_xticks(months)
ax.set_xticklabels(month_labels)
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda val, _: f'${val:,.0f}'))
ax.legend(fontsize=11)
ax.grid(True, linestyle=':', alpha=0.6)   # dotted grid this time

plt.tight_layout()
plt.savefig('styled_profit_line.png', dpi=150)
plt.show()