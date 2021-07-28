# 1 of 2 programs 6-11 of 6-11/6-12
# This program saves a sequence of video running times to
# the video_times.txt file.

def main()
    # Get the number of videos in the project
    num_videos = int(input('How many videos are in the project? '))

    # Open the file to hold the running times.
    video_file = open('video_times.txt', 'w')

    # Get each video's running time and write it to the file
    print('Enter the running times for each video.')
    for count in range(1, num_videos + 1):
        run_time = float(input(f'Video #{count}: '))
        video_file.write(f'{run_time}\n')

    # Close the file
    video_file.close()
    print('The times have been saved to video_times.txt')

# call the main function
if __name__ == '__main__':
    main()

#=======OUTPUT=============
# How many videos are in the project? 3 *enter
# Enter the running times for each video.
# Video #1: 24.5 *enter
# Video #2: 34.5 *enter
# Video #3: 14.5 *enter
# The times have been saved to video_times.txt.