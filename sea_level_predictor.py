import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    y=df['CSIRO Adjusted Sea Level']
    x=df['Year']
    fig,ax=plt.subplots(figsize=(6,4))
    ax=plt.scatter(x,y)
    
    # plt.xlabel('Year')
    # plt.ylabel('Sea Level (inches)')
    

    # Create first line of best fit
    reg=linregress(x,y)
    x_forecast=pd.Series([i for i in range(1880,2051,1)])
    y_forecast=reg.slope*x_forecast+reg.intercept
    plt.plot(x_forecast,y_forecast,'r-')
    # plt.xlabel('Year')
    # plt.ylabel('Sea Level (inches)')

    # Create second line of best fit
    df_forc=df.loc[df['Year']>=2000]
    x_new=df_forc['Year']
    y_new=df_forc['CSIRO Adjusted Sea Level']

    new_reg=linregress(x_new,y_new)
    x_new_forecast=pd.Series([i for i in range(2000,2051,1)])
    y_new_forecast=new_reg.slope*x_new_forecast+new_reg.intercept
    plt.plot(x_new_forecast,y_new_forecast,'orange')
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()