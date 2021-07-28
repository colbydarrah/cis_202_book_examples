# Colby Darrah
# 3/23/2021
# 7-24. keyword argument markers in graph pg 414
# using matplotlib to graph a line.
# program puts in "o" circle marker for as keyword argument markers.
# MARKERS can be:
  # 'o', which shows a round dot
  # 's', which shows a square
  # '*', which shows a small star
  # 'D', which shows a small diamond
  # '^', which shows an upward triangle
  # 'v', which shows a downward triangle
  # '<', which shows a left pointed triange
  # '>', which shows a right-pointed triange

# create alias for matplotlib.pyplot
import matplotlib.pyplot as plt

def main():
  # Create lists with the X and Y coordinates of each data point
  x_coords = [0,1,2,3,4]
  y_coords = [0,3,1,5,2]

#======================================================
  # Build the line graph (in memory) & insert MARKER
  plt.plot(x_coords, y_coords, marker = 'o')
#======================================================


  # Add a TITLE.
  plt.title('Sample Data')

  # Add LABELS to the axes
  plt.xlabel('Year')
  plt.ylabel('Sales')

  # customize the tick marks.
  plt.xticks([0,1,2,3,4],
             ['2016', '2017', '2018', '2019', '2020'])
  plt.yticks([0,1,2,3,4,5],
             ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])


  # Add a GRID
  plt.grid(True)

  # Display the line graph
  plt.show()
  


# Call the main function
if __name__ == '__main__':
  main()

