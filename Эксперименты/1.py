import pandas as pd
import matplotlib.pyplot as plt

# Comparative data for quota types over 20 years
years = [2005, 2010, 2015, 2020, 2024]
data = {
    'Year': years,
    'Targeted Quotas (k)': [15, 30, 45, 50, 51.5],
    'Preferential Quotas (k)': [40, 50, 56, 57.25, 59],
    'Foreign Quotas (k)': [5, 20, 40, 60, 65],
    'Regional Quotas (k)': [5, 15, 30, 35, 38]
}

df_quota_trends = pd.DataFrame(data)

# Plotting comparative trends
plt.figure()
plt.plot(df_quota_trends['Year'], df_quota_trends['Targeted Quotas (k)'], marker='o', label='Targeted Quotas')
plt.plot(df_quota_trends['Year'], df_quota_trends['Preferential Quotas (k)'], marker='s', label='Preferential Quotas')
plt.plot(df_quota_trends['Year'], df_quota_trends['Foreign Quotas (k)'], marker='^', label='Foreign Quotas')
plt.plot(df_quota_trends['Year'], df_quota_trends['Regional Quotas (k)'], marker='d', label='Regional Quotas')
plt.xticks(range(2005, 2026, 5))
plt.xlabel('Year')
plt.ylabel('Number of Places (thousands)')
plt.title('Trends in University Quotas in Russia (2005–2024)')
plt.legend()
plt.grid(True)
plt.tight_layout()


plt.show()
