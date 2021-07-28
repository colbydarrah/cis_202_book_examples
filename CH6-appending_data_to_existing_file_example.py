

# Assuming the file "friends.txt" already exists and contains
# the names Joe, Rose, and Geri... the following code opens
# the file and appends additional data to the existing
# content.

myfile = open('friends.txt','a')
myfile.write('Matt\n')
myfile.write('Chris\n')
myfile.write('Suze\n')
myfile.close()

# ==============OUTPUT=========================
# Joe       **original
# Rose      **original
# Geri      **original
# Matt      **appended/added to file
# Chris     **appended/added to file
# Suze      **appended/added to file