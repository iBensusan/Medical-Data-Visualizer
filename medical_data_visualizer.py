import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

# Calculating BMI for each person and create new column overweight
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

# Normalizing the cholesterol and gluc columns.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Using pd.melt() to transform the df into long format, because I'll use catplot() which expects data in long format.
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

# Creating the categorical plot
fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count')
# Show the plot
plt.show()

# Filtering the data by removing outliers and inconsistent entries.
df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

# Correlation matrix between the numeric variables
corr = df_heat.corr()

# Generating mask
mask = np.triu(np.ones_like(corr, dtype=bool))

# Creating Heat Map
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, mask=mask, fmt='.1f', square=True, cmap='coolwarm')
plt.show()

