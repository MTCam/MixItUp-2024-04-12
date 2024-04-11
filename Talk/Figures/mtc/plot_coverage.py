import matplotlib.pyplot as plt

# Read and parse
with open('coverage_data.txt', 'r') as file:
    data = file.read()

lines = data.strip().split('\n')
all_modules = [line.split()[0] for line in lines]
all_coverages = [int(line.split()[-1][:-1]) for line in lines]

# Filter out "__init__.py" and remove prefixes, just for brevity
filtered_modules = []
filtered_coverages = []
for i in range(len(all_modules)):
    if "__init__.py" not in all_modules[i]:
        filtered_modules.append(all_modules[i].split("/")[-1])
        filtered_coverages.append(all_coverages[i])

# sort by coverage %
sorted_indices = sorted(range(len(filtered_coverages)), key=lambda k: filtered_coverages[k], reverse=True)
modules = [filtered_modules[i] for i in sorted_indices]
coverages = [filtered_coverages[i] for i in sorted_indices]

colors = []
for cov in coverages:
    if cov >= 95:
        colors.append("darkgreen")
    elif 80 <= cov < 95:
        colors.append("green")
    elif cov < 60:
        colors.append("red")
    else:
        colors.append("darkgoldenrod")

# Plot it
plt.figure(figsize=(14, 10))
bars = plt.bar(modules, coverages, color=colors, edgecolor='lightgray')
plt.xticks(rotation=90, fontsize=14, fontweight='bold')
# Set y-ticks at 10% intervals
plt.yticks(range(0, 101, 10), fontsize=14, fontweight='bold')
#plt.yticks(fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.6)
#plt.xlabel("Modules", fontsize=16, fontweight='bold')
plt.ylabel("Coverage (%)", fontsize=16, fontweight='bold')
# plt.title("CI Test Coverage", fontsize=18, fontweight='bold')
plt.tight_layout()

# Save the plot to a PDF file
plt.savefig("coverage_plot.pdf")

# Show the plot (optional)
plt.show()
