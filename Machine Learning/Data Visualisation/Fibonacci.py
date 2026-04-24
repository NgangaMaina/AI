import matplotlib.pyplot as plt

#Generate the first 10 Fibonacci numbers
fib = [0, 1]
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])

x = list(range(1, 11))

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, fib,
        color='steelblue',
        linewidth=2,
        linestyle='-',
        label='Continuous Line')

ax.scatter(x, fib,
           color='red',
           s=80,
           zorder=5,
           label='Independent Dots')

for i, val in zip(x, fib):
    ax.annotate(str(val),
                xy=(i, val),
                xytext=(0, 10),
                textcoords='offset points',
                ha='center',
                fontsize=10,
                fontweight='bold')

ax.set_title('First 10 Fibonacci Numbers', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Position in Sequence', fontsize=12)
ax.set_ylabel('Fibonacci Value', fontsize=12)
ax.set_xticks(x)
ax.legend(fontsize=11)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('fibonacci_plot.png', dpi=150)
plt.show()