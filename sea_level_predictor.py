import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df = pd.read_csv('epa-sea-level.csv')

    df.index = df['Year']
    df.drop('Year', axis=1, inplace=True)
    df

    # Create scatter plot

    plt.scatter(df.index, df.iloc[:, 0]);

    # Create first line of best fit

    x = df.index
    y = df.iloc[:, 0]
    result = linregress(x, y)

    print(f"Intercept: {result.intercept}, Slope: {result.slope}")
    
    x_fit = np.arange(x.min(), 2051)
    y_fit = result.slope * x_fit + result.intercept

    # Create second line of best fit

    df_new = df[df.index >= 2000]
    x_new = df_new.index
    y_new = df_new.iloc[:, 0]
    result_new = linregress(x_new, y_new)

    print(f"Intercept: {result_new.intercept}, Slope: {result_new.slope}")

    x_fit_new = np.arange(2000, 2051)
    y_fit_new = result_new.slope * x_fit_new + result_new.intercept

    # Add labels and title

    fig, ax = plt.subplots()

    ax.scatter(x, y, color="#3AABE4")
    ax.plot(x_fit, y_fit, color="#B8003A")
    ax.plot(x_fit_new, y_fit_new, color="#B8003A")
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level');
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()