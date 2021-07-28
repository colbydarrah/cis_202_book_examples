# Colby Darrah
# 3/23/2021
# 7-20. line graph pg 405
# using matplotlib to graph a line.
# change the name of "matplotlib.pylot" to "plt" for ease of re-writing


# create alias for matplotlib.pyplot
import matplotlib.pyplot as plt

def main():
  # Create lists with the X and Y coordinates of each data point
  x_coords = [0,1,2,3,4]
  y_coords = [0,1,2,3,4]

  # Build the line graph (in memory)
  plt.plot(x_coords, y_coords)

  # Display the line graph
  plt.show()
  


# Call the main function
if __name__ == '__main__':
  main()

