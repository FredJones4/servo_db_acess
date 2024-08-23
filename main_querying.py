import querying_work
import pandas as pd
"""
Options:

1. Replace 'data_working_20240822.csv' with 'servo_data.csv' in the main_querying.py file to access the latest pull.

2. The querying_work.py file includes BETWEEN function for numerical columns and CONTAINS function for text columns.

write any combination of filtering functions to filter the data as desired in the df you loaded from the CSV file.

3. The data is currently saved to a new CSV file with a timestamp. You can change the filename to a more descriptive name if needed.

"""
df = pd.read_csv('data_working_20240822.csv')

filtered_df = querying_work.filter_by_range(df, 'Torque(oz-in)', 50.0, 100.0)


querying_work.save_filtered_df(filtered_df)