import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Data setup with the corrected and complete set of data points
data_updated = {
    "Date": ["2021-02-10", "2021-08-10", "2021-08-17", "2021-08-29", "2021-09-05", "2021-12-09", "2022-05-03", "2023-03-01"],
    "Array Context Type": ["PyOpenCL (Eager)", "pytato-PyOpenCL (Switch to lazy)", "SGWB ()", "SGWB ()",
                           "SGWB ()", "Fusion (Switch to fusion)", "Fusion ()",
                           "fusion ()"],
    "Type": ["Eager", "Pytato", "SGWB", "SGWB", "SGWB", "Fusion", "Fusion", "Fusion"],
    "CNS(2sp)": [14.1, 3.3, 2.1, 1.3, 0.8, 0.5, 0.4, 0.37],
    "Mixture": [51.4, 12, 7.5, 4.6, 2.9, 1.9, 1.5, 1.24],
    "TTS": [608, 142, 89, 57, 34, 22, 17, 14]
}
df_updated = pd.DataFrame(data_updated)
df_updated["Date"] = pd.to_datetime(df_updated["Date"])

# Adjusting global plot settings for font size and weight
plt.rcParams.update({'font.size': 14, 'font.weight': 'normal', 'axes.titleweight': 'normal', 'axes.labelweight': 'normal'})

# Function to plot performance improvement over time
def plot_performance_corrected(df, title, include_eager=True, showit=True):
    if not include_eager:
        df = df[df["Type"] != "Eager"]
    
    x = range(len(df))  # Define x based on the current df length
    fig, ax1 = plt.subplots(figsize=(14, 8))
    width = 0.35  # Bar width

    # Dual y-axes setup
    ax2 = ax1.twinx()
    # ax1.bar([p - width/2 for p in x], df["CNS(2sp)"], width, label='CNS(2sp)', color='mediumblue')
    ax1.bar(x, df["Mixture"], width, label='Walltime per step', color='orange')
    ax2.plot(x, df["TTS"], label='Walltime per simulation', color='green',
             marker='o', linestyle='-', linewidth=4)

    # Axis labels and tick formatting
    ax1.set_xlabel("Date", fontsize=16, fontweight="bold")
    ax1.set_ylabel("Walltime per step (s)", fontsize=16, color='black', fontweight="bold")
    ax2.set_ylabel("Days on 200 Lassen Nodes", fontsize=16, color='green', fontweight="bold")
    ax1.set_xticks(x)
    ax1.set_xticklabels([f"{row.Date.strftime('%Y-%m-%d')}" for index, row in df.iterrows()], fontsize=16)

    # Annotations and legend configuration
    # if include_eager:
    for i, (index, row) in enumerate(df.iterrows()):
        annotation_text = row["Array Context Type"].split("(")[1].split(")")[0]
        annotation_point = (i, row["Mixture"])
        if annotation_text:
            ax1.annotate(annotation_text, annotation_point, textcoords="offset points",
                         xytext=(8,15), ha="left", fontsize=14, fontweight="bold", rotation=45,
                         arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='black'))
        #ax1.annotate(row["Array Context Type"].split("(")[1].split(")")[0],
        #             (i, max(row["CNS(2sp)"], row["Mixture"]) + 3), ha='right',
        #             va='bottom', fontsize=12, rotation=45)
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    combined_handles = handles1 + handles2
    combined_labels = labels1 + labels2

    # Create a single combined legend
    fig.legend(combined_handles, combined_labels, fontsize=14)
    # ax1.legend(fontsize=12)
    # ax2.legend(fontsize=12, loc='upper left')
    ax1.set_title(title, fontsize=20, fontweight="bold")
    if include_eager:
        ax2.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)
    else:
        ax1.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)
        ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
        ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))

    plt.tight_layout()
    if showit:
        plt.show()
    else:
        filename = "gas-only-perf-eager.pdf" if include_eager else "gas-only-perf.pdf" 
        fig.savefig(filename, bbox_inches="tight")

# Plotting both versions of the charts
plot_performance_corrected(df_updated, "Gas-Only ACTII Flowthrough", include_eager=True, showit=False)
plot_performance_corrected(df_updated, "Gas-Only ACTII Flowthrough - Lazy", include_eager=False, showit=False)
