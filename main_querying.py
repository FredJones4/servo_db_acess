import querying_work
import pandas as pd
"""
Options:

1. Replace 'data_working_20240822.csv' with 'servo_data.csv' in the main_querying.py file to access the latest pull.

2. The querying_work.py file includes BETWEEN function for numerical columns and CONTAINS function for text columns.

Write any combination of filtering functions to filter the data as desired in the df you loaded from the CSV file.

3. The data is currently saved to a new CSV file with a timestamp. You can change the filename to a more descriptive name if needed.

"""
df = pd.read_csv('data_working_20240822.csv')
# Sample filtering by range.
filtered_df = querying_work.filter_by_range(df, column_name='Torque(oz-in)', lower_bound=50.0, upper_bound=100.0)
# Sample filtering by text.
matching_filtered_df = querying_work.filter_by_text(filtered_df, column_name='Motor Type', text='DC')
# Save number 1.
querying_work.save_filtered_df(filtered_df)
# Save number 2. 
querying_work.save_filtered_df(matching_filtered_df)


# Example of combining multiple functions.

# Sample filtering by range.
filtered_df = querying_work.filter_by_range(df, column_name='Torque(oz-in)', lower_bound=50.0, upper_bound=100.0)
df_filtered_2 = querying_work.filter_by_range(filtered_df, column_name='Motor RPM', lower_bound=1000, upper_bound=2000)
df_filtered_3 = querying_work.filter_by_text(df_filtered_2, column_name='Motor Type', text='DC')
# Save number 3.
querying_work.save_filtered_df(df_filtered_3)