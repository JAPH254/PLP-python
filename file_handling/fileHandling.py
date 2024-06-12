def write_to_file(filename, content):

  try:

    with open(filename, 'w') as file_object:
   
      for line in content:
        file_object.write(line + "\n")  # Adding newline character at the end
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permissions to write to '{filename}'.")
  finally:
    # Closing the file object, even if an exception occurs
    if file_object:
      file_object.close()


  try:
   
    with open(filename, 'r') as file_object:
    
      contents = file_object.read()
      print(contents)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permissions to read from '{filename}'.")
  finally:
    if file_object:
      file_object.close()

def append_to_file(filename, content):
  """
  Appends content to a text file in append mode ('a').

  Args:
      filename: The name of the file to append to (str).
      content: The content to append to the file (list of strings).
  """
  try:
    # Open the file in append mode ('a')
    with open(filename, 'a') as file_object:
      # Write each line of content to the file with newline characters
      for line in content:
        file_object.write(line + "\n")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permissions to append to '{filename}'.")
  finally:
    # Close the file object, even if an exception occurs
    if file_object:
      file_object.close()

# File creation (write mode)
write_to_file("my_file.txt", [
  "This is the first line of text.\n",
  "Here's another line with a number: 42\n",
  "And some more text to write."
])

# File reading and display
read_from_file("my_file.txt")

# File appending (append mode)
append_to_file("my_file.txt", [
  "\nAppending some additional content.\n",
  "This line is appended after the existing content.\n",
  "Another line to demonstrate appending."
])

# Read the entire file content again to show the appended data
read_from_file("my_file.txt")
