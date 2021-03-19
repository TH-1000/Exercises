import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight']/(df['height']/100)**2
df.loc[df['overweight'] < 25, 'overweight'] = 0
df.loc[df['overweight'] >= 25, 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars = 'cardio', value_vars = ('cholesterol','gluc', 'smoke', 'alco','active','overweight'), value_name='count')

    # Draw the catplot with 'sns.catplot()'    
    fig = sns.catplot(data=df_cat, kind="count",  x="variable", hue="value", col="cardio")

    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(9,9))
    
    # Draw the heatmap with 'sns.heatmap()'
    fig = sns.heatmap(corr, linewidths=1, mask=mask, vmax=.3, center=0.09,square=True, cbar_kws = {'orientation' : 'vertical'})

    # Save fig
    fig.savefig('heatmap.png')
    return fig
