import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x=df["Year"]
    y=df["CSIRO Adjusted Sea Level"]
    plt.scatter(x, y, s = 50, c = "red");

    # Create first line of best fit
    result = linregress(x, y)
    x_fl = pd.Series(range(1880,2051))
    y_fl = result.intercept + result.slope*x_fl
    plt.plot(x_fl, y_fl, "r")

    
    # Create second line of best fit
    sec_df = df.loc[df["Year"] >= 2000]
    sec_x = sec_df["Year"]
    sec_y = sec_df["CSIRO Adjusted Sea Level"]
    sec_result = linregress(sec_x, sec_y)
    x_sl = pd.Series(range(2000,2051))
    y_sl = sec_result.intercept + sec_result.slope*x_sl
    plt.plot(x_sl, y_sl, "blue")

  
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()