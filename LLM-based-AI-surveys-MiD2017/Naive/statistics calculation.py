from scipy.spatial.distance import jensenshannon
from scipy.stats import entropy, chi2_contingency
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Function to calculate Cramer's V
def cramers_v(contingency_table):
    chi2, _, _, _ = chi2_contingency(contingency_table)
    n = np.sum(contingency_table)
    phi2 = chi2 / n
    r, k = contingency_table.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))

# Adjust the contingency table to avoid empty bins
def adjusted_contingency_table(real, synthetic, bins=10):
    real_bins = np.linspace(min(real), max(real), bins + 1)
    synthetic_bins = np.linspace(min(synthetic), max(synthetic), bins + 1)
    contingency_table, _, _ = np.histogram2d(real, synthetic, bins=[real_bins, synthetic_bins])
    # Ensure no zero rows or columns
    contingency_table = contingency_table[~np.all(contingency_table == 0, axis=1)]
    contingency_table = contingency_table[:, ~np.all(contingency_table == 0, axis=0)]
    return contingency_table

# Prepare synthetic and real distributions for comparison
synthetic_distribution = synthetic_df.values.flatten()
real_distribution = real_df.values.flatten()

# Normalize distributions
synthetic_prob = synthetic_distribution / np.sum(synthetic_distribution)
real_prob = real_distribution / np.sum(real_distribution)

# Calculate metrics
mae_value = mean_absolute_error(real_distribution, synthetic_distribution)
rmse_value = np.sqrt(mean_squared_error(real_distribution, synthetic_distribution))
js_distance = jensenshannon(real_prob, synthetic_prob)
real_entropy = entropy(real_prob)
synthetic_entropy = entropy(synthetic_prob)
conditional_entropy = real_entropy - synthetic_entropy

# Create a contingency table for Cramer's V
contingency_table = adjusted_contingency_table(real_distribution, synthetic_distribution)
cramers_v_value = cramers_v(contingency_table)

# Metrics summary
metrics_summary = {
    "Mean Absolute Error (MAE)": mae_value,
    "Root Mean Squared Error (RMSE)": rmse_value,
    "Jensen-Shannon Distance (JS Distance)": js_distance,
    "Real Distribution Entropy": real_entropy,
    "Synthetic Distribution Entropy": synthetic_entropy,
    "Conditional Entropy": conditional_entropy,
    "Cramer's V": cramers_v_value
}
