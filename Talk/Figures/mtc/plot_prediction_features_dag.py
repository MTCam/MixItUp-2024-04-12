import matplotlib.pyplot as plt
import numpy as np

# Data extraction
features = [
    "CNS", "Passive species", "Power Law Xport", "Artificial Visc 1", "Artificial Visc 2",
    "Wall coupling", "Mixture", "Chemistry", "Ignition", "State Limiting",
]
mfs = [
    29, 32, 34, 51, 66, 66, 735, 735, 735, 2384,
]
mfs_10 = [d * 10 for d in mfs]

rhs = [
    2091, 2852, 2872, 3232, 3870, 5801, 14620, 14834, 14890, 26483,
]
compile_time = [
    56.3, 98.5, 99.5, 138.8, 163.8, 286.2, 648.16, 681.91, 681.98, 1903.9,
]


# Adjusting the plot to correctly scale the RHS data and improve readability of the y-axis labels

fig, ax1 = plt.subplots(figsize=(12, 8))

# MFS sizes
ax1.set_xlabel('Prediction Feature', fontsize=16, fontweight="bold")
# ax1.set_ylabel('MFS DAG Size', color='tab:blue', fontsize=14, fontweight="bold")
ax1.set_ylabel('Number of DAG Nodes', color='black', fontsize=14, fontweight="bold")
ax1.set_ylim(0, 25000)
ax1.bar(features, mfs_10, width=-0.4, align='edge', label='MFSx10', color='tab:blue', alpha=0.6)
ax1.bar(features, rhs[:10], width=0.4, align='edge', label='RHS', color='tab:red', alpha=0.6)  # Original RHS data, no need for manual scaling
ax1.tick_params(axis='y', labelcolor='black', labelsize=14)
ax1.set_xticklabels(features, rotation=45, fontsize=12, fontweight="bold")
#ax1.legend(loc='upper left', bbox_to_anchor=(0, 1.12))
ax1.legend(loc='upper left', fontsize=14)
# Correct RHS sizes with proper scaling
#ax2 = ax1.twinx()
#ax2.bar(features, rhs[:10], width=0.4, align='edge', label='RHS', color='tab:red', alpha=0.6)  # Original RHS data, no need for manual scaling
#ax2.set_ylabel('RHS DAG Size', color='tab:red', fontsize=16, fontweight="bold")
#ax2.set_ylim(0, 25000)  # Adjust y-axis limit for RHS to top out at 25000 nodes
#ax2.tick_params(axis='y', labelcolor='tab:red')
#ax2.legend(loc='upper right', bbox_to_anchor=(1, 1.12))
#ax2.legend(loc='upper left')

# Compile time, adjusting for third y-axis
ax2 = ax1.twinx()
#ax2.spines['right'].set_position(('outward', 60))  # Offset the compile time axis to prevent label overlap
ax2.plot(features, compile_time, label='Compile Time (s)', color='tab:green', marker='o')
ax2.set_ylabel('Compile Time (s)', color='tab:green', fontsize=16, fontweight="bold")
ax2.tick_params(axis='y', labelcolor='tab:green', labelsize=14)
ax2.legend(loc='upper right', bbox_to_anchor=(1, 1.02), fontsize=14)
ax2.set_ylim(0, 2000)
plt.title('DAG Size and Compile Time vs. Prediction Feature Sets', fontsize=20, fontweight="bold")
fig.tight_layout()

showit = True
if showit:
    plt.show()
else:
    fig.savefig("prediction_features_dag.pdf", bbox_inches="tight")

