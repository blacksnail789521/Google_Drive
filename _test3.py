import matplotlib.pyplot as plt
import numpy as np

# Example MAPE results (hypothetical):
# Assume these are mean absolute percentage errors obtained from each approach.
mape_tabular = {
    'RF': 12.5,
    'LGBM': 11.0,
    'SVR': 14.8,
    'PLS': 15.2,
    'XGB': 10.5
}

mape_timeseries = {
    'RF': 10.0,
    'LGBM': 9.5,
    'SVR': 12.0,
    'PLS': 13.0,
    'XGB': 9.0
}

models = list(mape_tabular.keys())
tab_values = [mape_tabular[m] for m in models]
ts_values = [mape_timeseries[m] for m in models]

# Set the width of the bars
bar_width = 0.35
x = np.arange(len(models))

fig, ax = plt.subplots(figsize=(8, 6))

# Plot tabular MAPE bars
tab_bars = ax.bar(x - bar_width/2, tab_values, width=bar_width, label='Tabular (Sklearn)', color='gray')

# Plot time series MAPE bars
ts_bars = ax.bar(x + bar_width/2, ts_values, width=bar_width, label='Time Series (Darts)', color='blue')

# Add labels, title, and custom x-axis tick labels, etc.
ax.set_ylabel('MAPE (%)')
ax.set_title('Comparison of Model Performance (Tabular vs. Time Series)')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

# Optional: Add a line for readability (lower is better)
ax.axhline(y=0, color='black', linewidth=1)

# Add data labels (optional)
for bar in tab_bars + ts_bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),
                textcoords='offset points',
                ha='center', va='bottom', fontsize=8, color='black')

plt.tight_layout()
plt.show()
