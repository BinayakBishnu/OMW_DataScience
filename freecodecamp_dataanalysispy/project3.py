import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('freecodecamp_dataanalysispy\project3.csv')

# Add 'overweight' column
df['BMI'] = df['weight'] * 10000 / ((df['height'])**2)
# print(df['BMI'])
df['overweight'] = df['BMI'] > 25
df['overweight'] = df['overweight'].astype(int)
# print(df['overweight'])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

# print(df['cholesterol'])
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
# print(df['cholesterol'])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = df_cat.sort_values(by='cardio')
    # print(df_cat)

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x ="variable", hue = "value", col ="cardio", data = df_cat, kind ="count")
    fig.set_axis_labels("variable", "total")
    print(fig)
    
    # sns.catplot(x ="variable", hue = "value", col ="cardio", data = df_cat, kind ="count")
    # plt.show()

    # Do not modify the next two lines
    # fig.savefig('catplot.png')
    # return fig

draw_cat_plot()

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype = bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask , vmax = .258, center = 0, 
            square = True, linewidths = .5, cbar_kws = {"shrink": .5}, annot = True, fmt ='.1f')
    
    # # Do not modify the next two lines
    # fig.savefig('heatmap.png')
    # return fig


draw_cat_plot()
draw_heat_map()