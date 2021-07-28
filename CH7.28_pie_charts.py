# Colby Darrah
# 3/23/2021
# 7-28. pie chart pg 420

# This program displays a simple pie chart

# create alias for matplotlib.pyplot
import matplotlib.pyplot as plt

def main():
  # Create a list of values
  values = [20,60,80,40]

  # Create a pie chart from the values.
  plt.pie(values)

  # Display the bar chart.
  plt.show()


# Call the main function
if __name__ == '__main__':
  main()

