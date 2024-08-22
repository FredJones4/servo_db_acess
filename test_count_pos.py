import csv

def count_positions_in_csv(csv_file):
  """Counts the total number of characters in a CSV file.

  Args:
    csv_file: The path to the CSV file.

  Returns:
    The total number of characters in the file.
  """

  total_positions = 0
  with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      for cell in row:
        total_positions += len(cell)
  return total_positions

# Example usage:
csv_file_path = "servo_data.csv"
total_positions = count_positions_in_csv(csv_file_path)
print("Total positions:", total_positions)