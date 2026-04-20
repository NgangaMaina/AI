import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Load & clean ──────────────────────────────────────────────────
df = pd.read_csv('iebc_2017_presidential_results.csv')
df['Percentage of Votes Cast'] = df['Percentage of Votes Cast'].str.replace('%', '').astype(float)

# ── Group <1% into Others ─────────────────────────────────────────
main  = df[df['Percentage of Votes Cast'] >= 1.0]
small = df[df['Percentage of Votes Cast'] <  1.0]
plot_df = pd.concat([main, pd.DataFrame([{
    'Political Party / Independent': 'Others',
    'Percentage of Votes Cast': small['Percentage of Votes Cast'].sum()
}])], ignore_index=True)

# ── Plot on a wide figure to give legend room ─────────────────────
fig, ax = plt.subplots(figsize=(12, 7))

ax.pie(plot_df['Percentage of Votes Cast'],
       autopct='%1.2f%%', startangle=140,
       colors=['red', 'orange', 'green'],
       explode=[0.03]*3, pctdistance=0.75,
       textprops={'fontsize': 12, 'color': 'white', 'fontweight': 'bold'})

# ── Build legend with Others breakdown ───────────────────────────
others_detail = '\n'.join([
    f"  • {r['Candidate Name']} [{r['Political Party / Independent']}] — {r['Percentage of Votes Cast']:.2f}%"
    for _, r in small.iterrows()
])

handles = [
    mpatches.Patch(color='red',    label="Jubilee Party (54.27%)"),
    mpatches.Patch(color='orange', label="Orange Democratic Movement (44.74%)"),
    mpatches.Patch(color='green',  label=f"Others (0.99%):\n{others_detail}"),
]

# Place legend to the RIGHT, outside the pie ──────────────────────
ax.legend(handles=handles,
          loc='center left',
          bbox_to_anchor=(1.0, 0.5),   # right side, vertically centred
          fontsize=9,
          frameon=True,
          title='Political Parties',
          title_fontsize=11)

ax.set_title('Kenya 2017 Presidential Election Results\nVote Share by Political Party',
             fontsize=13, fontweight='bold', pad=15)

plt.savefig('kenya_2017_pie_final.png', dpi=150, bbox_inches='tight')
plt.show()