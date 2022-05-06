import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15, 5))
    plt.plot(df.index, df["value"], color="red")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontdict = {'size':20})
    plt.xlabel("Date", fontdict = {'size':20})
    plt.ylabel("Page Views", fontdict = {'size':20})

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month
    df_bar = df_bar.groupby(["Years", "Months"])["value"].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot
    fig = df_bar.plot(kind ="bar", legend = True, figsize = (15,10)).figure
    plt.xlabel("Years", fontdict = {'size':20})
    plt.ylabel("Average Page Views", fontdict = {'size':20})
    plt.legend(title="Months", labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    # Draw box plots (using Seaborn)

    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")

    fig, axis = plt.subplots(1, 2, figsize=(25,10))
    

    sns.boxplot(x=df_box["year"],y=df_box["value"], ax = axis[0])
    axis[0].set_title("Year-wise Box Plot (Trend)", fontdict = {'size':15}) 
    axis[0].set_xlabel('Year', fontdict = {'size':15})
    axis[0].set_ylabel('Page Views', fontdict = {'size':15})

    sns.boxplot(x=df_box["month"], y=df_box["value"], ax = axis[1])
    axis[1].set_title("Month-wise Box Plot (Seasonality)", fontdict = {'size':15})
    axis[1].set_xlabel('Month', fontdict = {'size':15})
    axis[1].set_ylabel('Page Views', fontdict = {'size':15})




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
