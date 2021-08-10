import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (8,5))
    colors = np.random.rand(134)
    ax.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level', c = colors, marker = '^', cmap = 'YlGnBu', alpha = 0.75)
   
    
    # Create first line of best fit
    # Get the linregress of subplot
    lin1 = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    # Extrend years to include on x
    extend_years = np.arange(1880, 2050, 1)
    
    # Got this formula online; plt.plot(x, m*x + b); where m is slope and b is intercept 
    extend_line = [lin1.slope*xi for xi in extend_years]
    ax.plot(extend_years, extend_line + lin1.intercept , linewidth = 1, color = 'indigo')
    
    
    # Create second line of best fit
    recent_years = df[df['Year'] >= 2000]
    # Get the lingress of the recent_years data
    lin2  = linregress(recent_years['Year'], recent_years['CSIRO Adjusted Sea Level'])
    # Extend X to forecast the year 2050
    forecast_years = np.arange(2001, 2050, 1)
    
    new_line = [lin2.slope*xi for xi in forecast_years]
    ax.plot(forecast_years, new_line + lin2.intercept, 'r--', color = 'red', label = 'Predicted levels after year: 2000')

    # Add labels and title
    ax.set_xlabel('Year', fontsize = 10)
    ax.set_ylabel('Sea Level (inches)', fontsize = 10)
    ax.set_title('Rise in Sea Level', fontsize = 25, font = 'Helvetica', color = 'navy')
    ax.legend(shadow = True)
    
    # Save plot and return data 
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()