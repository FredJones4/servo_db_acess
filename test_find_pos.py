import pandas as pd

def find_character_at_position(csv_file, position):
  """Finds the character at a given position in a CSV file.

  Args:
    csv_file: The path to the CSV file.
    position: The desired character position.

  Returns:
    The character at the specified position, or None if it doesn't exist.
  """

  with open(csv_file, 'r') as f:
    for line in f:
      if len(line) >= position:
        return line[position - 1]
  return None

# Example usage:
csv_file = 'servo_data.csv'
position = 40977

character = find_character_at_position(csv_file, position)

if character:
  print("Character at position", position, ":", character)
else:
  print("Character position not found in the file.")