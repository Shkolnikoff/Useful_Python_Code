# Import the write file safely function in order to create unique timestamp files
from functions.write_file_safely import write_file, append_file

#####  Place file name and file path here !
file_name = "favorite_movies.txt"
file_path = "text_files"

# variable to be passed to function, creates the relative file path and file name
file = file_path + "/" + file_name

# content to write
content = "Hello World!"

# Call append function
append_file(content, file)

