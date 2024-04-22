# File Creation
try:
    # Creating and writing to a new text file
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("These are the numbers\n")
        file.write("Another line with mixture of text and numbers: #am here 1\n")
except Exception as e:
    print(f"Error occurred while creating the file: {e}")
else:
    print("File created successfully.")

# File Reading and Display
try:
    # Opening the file in read mode and displaying its contents
    with open("my_file.txt", "r") as file:
        file_contents = file.read()
        print("File contents:")
        print(file_contents)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print(f"Error occurred while reading the file: {e}")

# File Appending
try:
    # Opening the file in append mode and adding more lines
    with open("my_file.txt", "a") as file:
        file.write("Appending a new line\n")
        file.write("New numbers 070700\n")
        file.write("Another line appended: #am here again !\n")
except Exception as e:
    print(f"Error occurred while appending to the file: {e}")
else:
    print("File appended successfully.")

# Error Handling with finally block
try:
    # Attempting to read a non-existent file to trigger an error
    with open("non_existent_file.txt", "r") as file:
        file_contents = file.read()
        print(file_contents)
except FileNotFoundError:
    print("File called non_existent_file.txt not found.")
except PermissionError:
    print("Permission denied to access the file.")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    print("End of the script.")
