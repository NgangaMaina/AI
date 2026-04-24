import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')

months  = df['month_number']
profits = df['total_profit']

month_labels = ['Jan','Feb','Mar','Apr','May','Jun',
                'Jul','Aug','Sep','Oct','Nov','Dec']

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(months, profits,
        color='steelblue',
        linewidth=2,
        linestyle='-',
        marker='o',
        markersize=6,
        label='Total Monthly Profit')

max_idx = profits.idxmax()
min_idx = profits.idxmin()

ax.annotate(f"Max: ${profits[max_idx]:,}",
            xy=(months[max_idx], profits[max_idx]),
            xytext=(months[max_idx] - 1.5, profits[max_idx] + 15000),
            arrowprops=dict(arrowstyle='->', color='green'),
            fontsize=9, color='green', fontweight='bold')

ax.annotate(f"Min: ${profits[min_idx]:,}",
            xy=(months[min_idx], profits[min_idx]),
            xytext=(months[min_idx] + 0.3, profits[min_idx] + 25000),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=9, color='red', fontweight='bold')


ax.set_title('Total Company Profit Per Month', fontsize=14,
             fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Total Profit (USD)', fontsize=12)
ax.set_xticks(months)
ax.set_xticklabels(month_labels)
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda val, _: f'${val:,.0f}'))
ax.legend(fontsize=11)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('monthly_profit_line.png', dpi=150)
plt.show()