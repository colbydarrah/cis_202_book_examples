# Colby Darrah
# 3/23/2021
# 7-25. bar chart graph pg 416
# using matplotlib to graph a BAR CHART.


# create alias for matplotlib.pyplot
import matplotlib.pyplot as plt

def main():
  # Create a list with the X coordinates of each bar's left edge.
  left_edges = [0,10,20,30,40]

  # Create a list with the heights of each bar.
  heights = [100,200,300,400,500]

  # Build the bar chart.
  plt.bar(left_edges, heights)

  # Display the bar chart.
  plt.show()


# Call the main function
if __name__ == '__main__':
  main()

