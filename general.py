import os
#function for creating a new directory
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# function for writing data to file