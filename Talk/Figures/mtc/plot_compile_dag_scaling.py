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


#fig, ax1 = plt.subplots(figsize=(12, 8))

x_ref = np.linspace(min(rhs), max(rhs), 500)
slope0 = compile_time[0]/rhs[0]
y_slope1 = x_ref * slope0
y_slope2 = (x_ref ** 2) * (compile_time[0] / rhs[0] ** 2)
slope, intercept = np.polyfit(np.log(rhs), np.log(compile_time), 1)
y_fit = np.exp(intercept) * x_ref ** slope

# Log-log plot of compile time vs. RHS DAG size for the updated dataset
fig, ax = plt.subplots(figsize=(10, 6))
ax.loglog(rhs, compile_time, 'o-', label='Compile Time', color='tab:red')
ax.loglog(x_ref, y_fit, label=f'Linear Fit (Slope: {slope:.2f})', color='black', linestyle='--')
ax.loglog(x_ref, y_slope1, label='Slope = 1', linestyle='--', color='tab:blue')
ax.loglog(x_ref, y_slope2, label='Slope = 2', linestyle='--', color='tab:orange')
ax.set_xlabel('Prediction RHS DAG Size', fontsize=14, fontweight="bold")
ax.set_ylabel('Compile Time (s)', fontsize=14, fontweight="bold")
ax.set_title('Prediction Features: RHS Compile Time vs. DAG Size', fontsize=20, fontweight="bold")
ax.tick_params(axis='y', labelcolor='black', labelsize=14)
ax.tick_params(axis='x', labelcolor='black', labelsize=14)
# ax.set_xticklabels(features, rotation=45, fontsize=14, fontweight="bold")
ax.legend()
fig.tight_layout()
plt.grid(True, which="both", ls="--")
showit = False
if showit:
    plt.show()
else:
    fig.savefig("compile_dag_scaling.pdf", bbox_inches="tight")

