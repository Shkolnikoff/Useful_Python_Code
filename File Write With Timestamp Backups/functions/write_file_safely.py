def write_file(content, destination):
    """ This function will write your file, and if file exists, it will create a backup of your previous file with a timestamp first
    Arguments:
        1. the content to write to file
        2. the destination of the file
    Returns:
        Nothing
    """
    #import operating system path module
    import os.path
    # import shell utility
    import shutil
    # import time package
    import time

    # If file exists, create a backup of the orignial before wrting to file
    if os.path.isfile(destination):
        shutil.copy2(destination, destination + ".backup" + str(time.time()))
    # Open and write the new temp_output to file
    with open(destination, "w") as file_output:
        file_output.write(content)

def append_file(content, destination):
    """ This function will check for your file, if it exists, it will create a backup and then append to your file and save it.
    1. the content to write to file
    2. the destination of the file
    Returns:
        Nothing
    """
    #import operating system path module
    import os.path
    # import shell utility
    import shutil
    # import time package
    import time
    # If file exists, create a backup of the orignial before appending to the file
    
    if os.path.isfile(destination):
        shutil.copy2(destination, destination + ".backup" + str(time.time()))
    with open(destination, "a") as file_output:
        file_output.write(content)

