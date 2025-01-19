import pandas as pd
import matplotlib.pyplot as plt

# Synthetic data
synthetic_age_group_data = {
    "Age Group": [
        "14 to 17 years", "18 to 29 years", "30 to 39 years", "40 to 49 years",
        "50 to 59 years", "60 to 64 years", "65 to 74 years", "75 to 79 years", "80 years and older"
    ],
    "agree": [35, 35.08329127, 34.10013532, 31.53745072, 35.30210455, 38.77118644, 36.09660574, 39.53934741, 34.74088292],
    "disagree": [24.4, 24.33114589, 26.18403248, 24.50722733, 24.16836388, 23.30508475, 25.19582245, 24.18426104, 23.41650672],
    "strongly agree": [25.6, 24.68450278, 24.56021651, 27.46386334, 26.54446707, 25.0, 25.32637076, 22.45681382, 26.87140115],
    "strongly disagree": [15, 15.90106007, 15.1556157, 16.49145861, 13.98506449, 12.92372881, 13.38120104, 13.81957774, 14.97120921]
}

# Real data
real_age_group_data = {
    "Age Group": [
        "14 to 17 years", "18 to 29 years", "30 to 39 years", "40 to 49 years",
        "50 to 59 years", "60 to 64 years", "65 to 74 years", "75 to 79 years", "80 years and older"
    ],
    "agree": [50, 50, 49, 52, 52, 50, 50, 51, 48],
    "disagree": [25, 17, 12, 13, 13, 13, 11, 13, 16],
    "strongly agree": [22, 30, 36, 32, 32, 35, 35, 32, 27],
    "strongly disagree": [3, 3, 2, 3, 3, 3, 3, 4, 8]
}

# Convert both datasets to DataFrames
synthetic_df = pd.DataFrame(synthetic_age_group_data)
real_df = pd.DataFrame(real_age_group_data)

# Set the Age Group as the index for better plotting
synthetic_df.set_index("Age Group", inplace=True)
real_df.set_index("Age Group", inplace=True)

# Plot the synthetic data with solid lines and real data with dashed grey lines
plt.figure(figsize=(12, 6))  # Wider diagram
for column in synthetic_df.columns:
    plt.plot(
        synthetic_df.index, synthetic_df[column], marker='o', label=f"{column} (synthetic)"
    )
    plt.plot(
        real_df.index, real_df[column], marker='o', linestyle='--', color='grey', alpha=0.7, label=f"{column} (real)"
    )

# Customize the plot
plt.title("Walking Preferences by Age Group: Synthetic vs Real Data", fontsize=14)
plt.ylabel("Percentage (%)", fontsize=12)
plt.ylim(0, 60)  # Adjust y-axis range to 0-60
plt.legend(title="Response", fontsize=10, bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45, fontsize=10, ha='right')
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Remove both x-axis label and tighten layout
plt.xlabel(None)
plt.tight_layout()
plt.show()
