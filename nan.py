import pandas as pd
import numpy as np

def replace_strings_with_nan(df, column_name):
    """
    Replaces string values in the specified column with NaN.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to check and replace values.

    Returns:
    pd.DataFrame: The DataFrame with strings replaced by NaN in the specified column.
    """
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Replace string values with NaN
    df[column_name] = df[column_name].apply(lambda x: np.nan if isinstance(x, str) else x)
    
    return df

def replace_strings_in_multiple_columns(df, column_names):
    """
    Applies replace_strings_with_nan to multiple columns in the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_names (list of str): A list of column names to check and replace values.

    Returns:
    pd.DataFrame: The DataFrame with strings replaced by NaN in the specified columns.
    """
    for column in column_names:
        try:
            df = replace_strings_with_nan(df, column)
        except ValueError as e:
            print(e)
    
    return df

# Example usage
if __name__ == "__main__":
    # Sample DataFrame
    data = {
        'Weight(oz)': [2.5, 'unknown', 3.0, 'N/A'],
        'L(in)': [1.2, '1.5 inches', 'unknown', 2.0],
        'W(in)': [0.8, 0.9, 'not available', 1.0],
        'H(in)': [0.5, 0.6, '0.7 in', 'N/A'],
        'Torque(which_V)': [1.0, 'varies', 1.5, 1.2],
        'Torque(oz-in)': [150, 160, '180 oz', 'not sure'],
        'Speed(which_V)': [0.1, '0.2 V', 'not sure', 0.3],
        'Speed(s/60deg)': [0.08, 0.09, 'N/A', '0.1 s/60deg'],
        'Typical Price': [9.99, 'unknown', 'free', 12.99]
    }
    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)

    # Columns to check and replace strings with NaN
    columns_to_check = [
        'Weight(oz)', 'L(in)', 'W(in)', 'H(in)', 'Torque(which_V)', 
        'Torque(oz-in)', 'Speed(which_V)', 'Speed(s/60deg)', 'Typical Price'
    ]

    # Apply replacement function to specified columns
    df = replace_strings_in_multiple_columns(df, columns_to_check)

    print("\nModified DataFrame:")
    print(df)
