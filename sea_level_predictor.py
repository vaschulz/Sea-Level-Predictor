import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
from scipy import stats

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv', float_precision='legacy', index_col = 'Year')

  # Create scatter plot
  plt.scatter(df.index, df['CSIRO Adjusted Sea Level'])

  # Create first line of best fit
  x_first = np.arange(1880, 2051)
  lin_first = stats.linregress(df.index, df['CSIRO Adjusted Sea Level'])
  plt.plot(x_first, lin_first.intercept + lin_first.slope*x_first, 'r', label='first line of best fit')

  # Create second line of best fit
  x_second = np.arange(2000, 2051)
  from2000 = df[df.index >= 2000]
  lin_second = stats.linregress(from2000.index, from2000['CSIRO Adjusted Sea Level'])
  plt.plot(x_second, lin_second.intercept + lin_second.slope*x_second, 'r', label='second line of best fit')

  # Add labels and title
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
