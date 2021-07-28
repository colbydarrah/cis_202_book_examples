# Colby Darrah
# 3/23/2021
# 7-27. bar chart pg 418
# add TITLE, axis LABELS, & customize the X & y axis w TICK MARKS


# create alias for matplotlib.pyplot
import matplotlib.pyplot as plt

def main():
  # Create a list with the X coordinates of each bar's left edge.
  left_edges = [0,10,20,30,40]

  # Create a list with the heights of each bar.
  heights = [100,200,300,400,500]

  # Create a variable for the bar width
  bar_width = 10

  # Build the bar chart.
  plt.bar(left_edges, heights, color = ('r', 'g', 'b', 'w', 'k'))
  #1st bar=red, 2nd bar=green, 3rd bar=blue, 4th bar= white, 5th bar=black

  # ========ADD TITLE==================================================================
  plt.title('Sales by Year')

  #======= ADD LABELS to axes ==========================================================
  plt.xlabel('Year')
  plt.ylabel('Sales')

  #======= customize the TICK MARKS ===================================================
  plt.xticks([5,15,25,35,45],
             ['2016', '2017', '2018', '2019', '2020'])
  plt.yticks([0,100,200,300,400,500],
             ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

  # Display the bar chart.
  plt.show()


# Call the main function
if __name__ == '__main__':
  main()

