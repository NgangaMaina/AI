import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('student-scores.csv')

subjects = ['math_score', 'history_score', 'physics_score',
            'chemistry_score', 'biology_score', 'english_score',
            'geography_score']

scores_data = [df[subject].dropna().values for subject in subjects]

subject_labels = ['Math', 'History', 'Physics',
                  'Chemistry', 'Biology', 'English', 'Geography']

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

colors = ['#FF6B6B','#4ECDC4','#45B7D1',
          '#96CEB4','#FFEAA7','#DDA0DD','#F0A500']

bp = axes[0].boxplot(scores_data,
                     patch_artist=True,
                     notch=False,
                     vert=True,
                     whis=1.5,
                     showfliers=True,
                     flierprops=dict(
                         marker='o',
                         markersize=3,
                         linestyle='none',
                         markeredgecolor='gray',
                         alpha=0.3
                     ),
                     medianprops=dict(color='red', linewidth=2),
                     whiskerprops=dict(linewidth=1.5),
                     capprops=dict(linewidth=2))

# Colour each box individually
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

# Add mean markers for each subject
for i, data in enumerate(scores_data, start=1):
    axes[0].scatter(i, np.mean(data),
                    marker='D', color='black',
                    s=40, zorder=5)

axes[0].set_title('Score Distribution by Subject\n(Box Plot)',
                  fontsize=13, fontweight='bold')
axes[0].set_ylabel('Score', fontsize=12)
axes[0].set_xticks(range(1, len(subjects) + 1))
axes[0].set_xticklabels(subject_labels, rotation=15, fontsize=9)
axes[0].grid(True, axis='y', linestyle='--', alpha=0.5)
axes[0].set_ylim(0, 115)

math_scores = df['math_score'].dropna()

axes[1].hist(math_scores, bins=20,
             color='#45B7D1', edgecolor='navy',
             alpha=0.85)

axes[1].axvline(math_scores.mean(),
                color='red', linestyle='--', linewidth=2,
                label=f"Mean:   {math_scores.mean():.1f}")

axes[1].axvline(math_scores.median(),
                color='green', linestyle='-.', linewidth=2,
                label=f"Median: {math_scores.median():.1f}")

axes[1].set_title('Math Score Distribution\n(Skewness Check)',
                  fontsize=13, fontweight='bold')
axes[1].set_xlabel('Score', fontsize=12)
axes[1].set_ylabel('Number of Students', fontsize=12)
axes[1].legend(fontsize=11)
axes[1].grid(True, axis='y', linestyle='--', alpha=0.5)

print("\n📊 SKEWNESS ANALYSIS — ALL SUBJECTS")
print("=" * 55)
print(f"{'Subject':<12} {'Mean':>7} {'Median':>8} {'Skewness':>10}")
print("-" * 55)

for subject, label in zip(subjects, subject_labels):
    data     = df[subject].dropna()
    mean     = data.mean()
    median   = data.median()
    skewness = data.skew()

    if skewness > 0.5:
        direction = "→ Right skew"
    elif skewness < -0.5:
        direction = "→ Left skew"
    else:
        direction = "→ Symmetric"

    print(f"{label:<12} {mean:>7.2f} {median:>8.2f} "
          f"{skewness:>8.4f}  {direction}")


print("\n📍 OUTLIER ANALYSIS — MATH SCORES")
print("=" * 40)
q1  = math_scores.quantile(0.25)
q3  = math_scores.quantile(0.75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

outliers = math_scores[(math_scores < lower_fence) |
                        (math_scores > upper_fence)]

print(f"Q1:           {q1:.2f}")
print(f"Q3:           {q3:.2f}")
print(f"IQR:          {iqr:.2f}")
print(f"Lower fence:  {lower_fence:.2f}")
print(f"Upper fence:  {upper_fence:.2f}")
print(f"Outliers found: {len(outliers)}")

plt.suptitle('Student Score Analysis — 2000 Students',
             fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('student_boxplot_real.png', dpi=150, bbox_inches='tight')
plt.show()