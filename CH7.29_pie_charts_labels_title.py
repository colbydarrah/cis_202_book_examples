# Colby Darrah
# 3/23/2021
# 7-28. pie chart - slice labels & titlepg 421

# This program labels the slices of the pie chart and
# gives the pie chart a title.

# create alias for matplotlib.pyplot
import matplotlib.pyplot as plt

def main():
  # Create a list of values
  sales = [100,400,300,600]

  # Create a list of labels for the slices.
  slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']

  # Create a pie chart from the values.
  plt.pie(sales, labels = slice_labels)

  # Add a title
  plt.title('Sales by Quater')

  # Display the bar chart.
  plt.show()


# Call the main function
if __name__ == '__main__':
  main()

