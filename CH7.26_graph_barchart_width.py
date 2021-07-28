# Colby Darrah
# 3/23/2021
# 7-26. bar chart width graph pg 417
# change the bar chart's width.


# create alias for matplotlib.pyplot
import matplotlib.pyplot as plt

def main():
  # Create a list with the X coordinates of each bar's left edge.
  left_edges = [0,10,20,30,40]

  # Create a list with the heights of each bar.
  heights = [100,200,300,400,500]

#===============================================================================
  # Create a variable for the bar width
  bar_width = 5

  # Build the bar chart.
  plt.bar(left_edges, heights, bar_width)
  # ===============================================================================

  # Display the bar chart.
  plt.show()


# Call the main function
if __name__ == '__main__':
  main()

