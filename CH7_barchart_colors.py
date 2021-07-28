# Colby Darrah
# 3/23/2021
# bar chart colors graph pg 418
# change the bar chart's color.
# color codes are
    # 'b' = blue
    # 'g' = green
    # 'r' = red
    # 'c' = cyan
    # 'm' = magenta
    # 'y' = yellow
    # 'k' = black
    # 'w' = white


# create alias for matplotlib.pyplot
import matplotlib.pyplot as plt

def main():
  # Create a list with the X coordinates of each bar's left edge.
  left_edges = [0,10,20,30,40]

  # Create a list with the heights of each bar.
  heights = [100,200,300,400,500]

  #===============================================================================
  # Build the bar chart.... with COLOR
  plt.bar(left_edges, heights, color = ('r', 'g', 'b', 'w', 'k'))
  #1st bar=red, 2nd bar=green, 3rd bar=blue, 4th bar= white, 5th bar=black
  # ===============================================================================

  # Display the bar chart.
  plt.show()


# Call the main function
if __name__ == '__main__':
  main()

