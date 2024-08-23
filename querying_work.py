import pandas as pd
import datetime

from pip._internal.utils.misc import tabulate


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


def save_filtered_df(filtered_df):
  """Saves the filtered DataFrame to a new CSV file with a timestamp.

  Args:
    filtered_df: The filtered DataFrame.
  """

  timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
  filename = f"queryAt_{timestamp}.csv"
  filtered_df.to_csv(filename, index=False)
  print(f"Filtered DataFrame saved to {filename}")






df = pd.read_csv('servo_data.csv')

filtered_df = filter_by_range(df, 'Torque(oz-in)', 50.0, 100.0)


save_filtered_df(filtered_df)