import pandas as pd
import matplotlib.pyplot as plt

# Prepare the data for the line plot
age_group_line_data = {
    "Age Group": [
        "14 to 17 years", "18 to 29 years", "30 to 39 years", "40 to 49 years",
        "50 to 59 years", "60 to 64 years", "65 to 74 years", "75 to 79 years", "80 years and older"
    ],
    "agree": [35, 35.08329127, 34.10013532, 31.53745072, 35.30210455, 38.77118644, 36.09660574, 39.53934741, 34.74088292],
    "disagree": [24.4, 24.33114589, 26.18403248, 24.50722733, 24.16836388, 23.30508475, 25.19582245, 24.18426104, 23.41650672],
    "strongly agree": [25.6, 24.68450278, 24.56021651, 27.46386334, 26.54446707, 25.0, 25.32637076, 22.45681382, 26.87140115],
    "strongly disagree": [15, 15.90106007, 15.1556157, 16.49145861, 13.98506449, 12.92372881, 13.38120104, 13.81957774, 14.97120921]
}

# Convert the data into a DataFrame for plotting
line_plot_df = pd.DataFrame(age_group_line_data)

# Set the Age Group as the index for better plotting
line_plot_df.set_index("Age Group", inplace=True)

# Plot the data without the x-axis label
plt.figure(figsize=(10, 6))
line_plot_df.plot(kind="line", marker='o', figsize=(10, 6))

# Customize the plot
plt.title("Walking Preferences by Age Group", fontsize=14)
plt.ylabel("Percentage (%)", fontsize=12)
plt.legend(title="Response", fontsize=10, bbox_to_anchor=(1.05, 1), loc="upper left")
plt.xticks(rotation=45, fontsize=10, ha='right')
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Remove x-axis label
plt.xlabel(None)

# Adjust layout
plt.tight_layout()
plt.show()
