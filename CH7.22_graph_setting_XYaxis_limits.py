# Colby Darrah
# 3/23/2021
# 7-22. line graph pg 410
# using matplotlib to graph a line.
# Program plots graph but sets Y axis limits to -1 to 6 and X axis limits to -1 to 10


# create alias for matplotlib.pyplot
import matplotlib.pyplot as plt

def main():
  # Create lists with the X and Y coordinates of each data point
  x_coords = [0,1,2,3,4]
  y_coords = [0,3,1,5,2]

  # Build the line graph (in memory)
  plt.plot(x_coords, y_coords)

  # Add a TITLE.
  plt.title('Sample Data')

  # Add LABELS to the axes
  plt.xlabel('This is the X axis')
  plt.ylabel('This is the Y axis')

  #========== Set the axis LIMITS ====================================
  plt.xlim(xmin = -1, xmax = 10)
  plt.ylim(ymin = -1, ymax = 6)
#====================================================================

  # Add a GRID
  plt.grid(True)

  # Display the line graph
  plt.show()
  


# Call the main function
if __name__ == '__main__':
  main()

