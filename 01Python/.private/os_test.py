import os


print('-'*20)

print("Terminal current working directory")
print(os.getcwd())

print("This python3 script File path")
print(os.path.abspath(__file__))

print("This script parent directory")
script_path = os.path.dirname(os.path.abspath(__file__)  )
print(script_path)

os.chdir(script_path)

# Specify the path to the text file
file_path = "mydir/file.txt"

# Open the file in read mode
with open(file_path, "r") as file:
    file_contents = file.readlines()

# Print the contents of the file
print(file_contents)


