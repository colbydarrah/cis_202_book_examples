# 2 of 2 programs 6-12 of 6-11/6-12
# This program takes the values in video_times.txt file
# and calculates their total.

def main()
    # Open the video_times.txt file for reading.
    video_file = open('video_times.txt', 'r')

    #initialize an accumulator to 0.0
    total = 0.0

    # Initialize a variable to keep count of the videos.
    count = 0

    print('Here are the running times for each video:')

    # Get the values from the file and total them.
    for line in video_file:
        # convert a line to a float.
        run_time = float(line)

        # add 1 to the count variable.
        count += 1

        # Display the time.
        print('Video #', count, ': ', run_time, sep='')

        # Add the time to total.
        total += run_time

    # Close the file.
    video_file.close()

    # Display the total of the running times.
    print(f'The total running time is {total} seconds.')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT============+
# Here are the running times for each video:
# Video #1: 24.5
# Video #2: 34.5
# Video #3: 14.5
# The total running time is 73.5 seconds
