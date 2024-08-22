import pandas as pd

def filter_by_range(df, column_name, lower_bound, upper_bound):
  """Filters a DataFrame based on a column's value range.

  Args:
    df: The input DataFrame.
    column_name: The name of the column to filter.
    lower_bound: The lower bound of the range.
    upper_bound: The upper bound of the range.

  Returns:
    A new DataFrame containing rows that meet the filtering criteria.
  """

  return df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]

def filter_by_text(df, column_name, text):
  """Filters a DataFrame based on a column's text content.

  Args:
    df: The input DataFrame.
    column_name: The name of the column to filter.
    text: The text to search for.

  Returns:
    A new DataFrame containing rows that match the text.
  """

  return df[df[column_name].str.contains(text, case=False)]


df = pd.read_csv('servo_data.csv')
filtered_df = filter_by_range(df, 'Torque(oz-in)', 50.0, 100.0)
print(filtered_df)


# # passed test cases, and therefore commented out
# Example usage:
# data = {'Age': [25, 30, 28, 18, 35],
#         'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#         'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
# df = pd.DataFrame(data)

# # Filter by age range
# filtered_df1 = filter_by_range(df, 'Age', 20, 30)
# print(filtered_df1)
#
# # Filter by text in the 'Name' column
# filtered_df2 = filter_by_text(df, 'Name', 'Alice')
# print(filtered_df2)