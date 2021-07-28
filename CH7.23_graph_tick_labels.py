# Colby Darrah
# 3/23/2021
# 7-23. line graph pg 412
# Program uses Tick-Mark Labels on X-axis to display years and
# on Y-axis to display sales in millions of dollars.


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
  plt.xlabel('Year')
  plt.ylabel('Sales')

  #======== customize the tick marks. =======================================
  plt.xticks([0,1,2,3,4],
             ['2016', '2017', '2018', '2019', '2020'])
  plt.yticks([0,1,2,3,4,5],
             ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

  #============================================================================
  # ==== OR  OR  OR  OR  OR  OR  OR  OR  OR  OR  OR============================
# plt.xticks([0,1,2], ['Baseball', 'Basketball', 'Football'])
# plt.yticks ([0,1,2,3], ['Zero', 'Quarter', 'Half', 'Three Quarters'])



  # Add a GRID
  plt.grid(True)

  # Display the line graph
  plt.show()
  


# Call the main function
if __name__ == '__main__':
  main()

