# Colby Darrah
# 3/23/2021
# Pie Chart colors 422

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
  # Create a list of values
  sales = [100,400,300,600]

  # Create a list of labels for the slices.
  slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']

  # Create a pie chart from the values.
  plt.pie(sales, labels = slice_labels, colors = ('r', 'g', 'b', 'w', 'k'))

  # Add a title
  plt.title('Sales by Quater')

  # Display the bar chart.
  plt.show()


# Call the main function
if __name__ == '__main__':
  main()

