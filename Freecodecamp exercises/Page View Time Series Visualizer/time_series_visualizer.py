import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker #had to use ticker to change axis ticks.
import seaborn as sns 

# Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the "date" column.
df = pd.read_csv('Fcc-forum-pageviews.csv')
df.set_index('date', inplace = True)

# Parse datetime
df.index = pd.to_datetime(df.index)

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
clean_df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    fig,ax = plt.subplots(figsize = (10,8), dpi = 200)
    ax.plot(clean_df, 'r-', linewidth = 0.4)
    ax.set_ylabel('Page Views', fontsize = 10)
    ax.set_xlabel('Date', fontsize = 10)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save figure
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = clean_df.copy()
    df_bar.reset_index(inplace = True )
    df_bar['year']=pd.DatetimeIndex(df_bar['date']).year
    df_bar['month']=pd.DatetimeIndex(df_bar['date']).month_name()

    # Draw bar plot 
    fig, ax = plt.subplots(figsize = (10,8), dpi = 200)
    sns.barplot(ax = ax, x = 'year', y = 'value', hue = 'month', data = df_bar, hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    ax.set_xlabel('Years', fontsize = 10)
    ax.set_ylabel('Average Page Views', fontsize = 10)

    
    # Save image and return fig 
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = clean_df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # Create a figure with 2 axes
    fig, (ax1,ax2) = plt.subplots(ncols = 2, figsize = (10,8), constrained_layout = True, dpi = 200)
    
    # First Axes
    sns.boxplot(data = df_box, ax = ax1, x = 'year', y = 'value')
    ax1.yaxis.set_major_formatter(ticker.EngFormatter()) #This line could be better
    ax1.set(ylim = (20000,200000))
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot(Trend)')
    
    # Second Axes
    sns.boxplot(data = df_box, ax = ax2, x = 'month', y = 'value')
    ax2.yaxis.set_major_formatter(ticker.EngFormatter())
    ax2.set(ylim = (20000,200000))
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot(Seasonality)')
    
    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
