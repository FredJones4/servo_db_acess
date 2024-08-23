from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import nan
import pandas as pd

LAST_PAGE = 101  # Adjust the page limit as needed

# Initialize the Chrome driver
driver = webdriver.Chrome()


# Function to clean and split Torque/Speed data
def clean_split_data(data):
    if data.lower() == "(add)" or not data.strip():  # Check if the data is "(add)" or blank
        return []

    # Split by line break
    split_data = data.split('\n')
    cleaned_data = []

    for item in split_data:
        # Use regex to extract just the numeric part
        voltage_match = re.search(r"(\d+(\.\d+)?)V", item)
        value_match = re.search(r"(\d+(\.\d+)?)", item.split()[-2])

        if voltage_match and value_match:
            voltage = voltage_match.group(1)
            value = value_match.group(1)
            cleaned_data.append((voltage, value))

    return cleaned_data


# Open a CSV file to write the data
with open("servo_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    header = ["Make", "Model", "Modulation", "Weight(oz)", "L(in)", "W(in)", "H(in)", "Torque(which_V)",
              "Torque(oz-in)", "Speed(which_V)", "Speed(s/60deg)", "Motor Type", "Rotation", "Gear Material",
              "Typical Price"]
    writer.writerow(header)

    # Iterate through pages
    for curr_page_number in range(1, LAST_PAGE + 1):
        print(f"Processing page {curr_page_number}...")
        # Navigate to the website
        driver.get(f"https://servodatabase.com/servos/all?page={curr_page_number}")

        # Wait for the table to load
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.servos")))

        # Scrape the data from the table
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 12:
                # Extract base data
                make = cells[0].find_element(By.TAG_NAME, "a").text
                model = cells[1].find_element(By.TAG_NAME, "a").text
                modulation = cells[2].text
                weight = cells[3].text.replace(" oz", "")  # Extract weight

                # Extract dimensions and split them
                dimensions = cells[4].text.replace(" in", "").split("×")
                if len(dimensions) == 3:
                    length, width, height = dimensions
                else:
                    length, width, height = "", "", ""  # Handle missing dimensions

                # Clean and split Torque and Speed data
                torque_data = clean_split_data(cells[5].text)
                speed_data = clean_split_data(cells[6].text)

                # Extract other data
                motor_type = cells[7].text
                rotation = cells[8].text
                gear_material = cells[9].text
                typical_price = cells[10].text

                # Handle cases where either Torque or Speed data is missing or marked as "(add)"
                if not torque_data:
                    torque_data = [("", "")] * len(speed_data)
                if not speed_data:
                    speed_data = [("", "")] * len(torque_data)

                # Combine and write each set of Torque and Speed data
                for t_data, s_data in zip(torque_data, speed_data):
                    cleaned_price = typical_price.replace("$", "")  # Remove the "$" symbol from the price
                    writer.writerow(
                        [make, model, modulation, weight, length, width, height, t_data[0], t_data[1], s_data[0],
                         s_data[1], motor_type, rotation, gear_material, cleaned_price])

# Close the browser

driver.quit()

# Last but not least, we need to clean the data by replacing string values with NaN in the relevant columns.
# We can use the functions defined in the nan.py file to achieve this.
columns_to_check = [
        'Weight(oz)', 'L(in)', 'W(in)', 'H(in)', 'Torque(which_V)', 
        'Torque(oz-in)', 'Speed(which_V)', 'Speed(s/60deg)', 'Typical Price'
    ]
df = pd.read_csv("servo_data.csv")
df = nan.replace_strings_in_multiple_columns(df, columns_to_check)
# Save the cleaned DataFrame to servo_data.csv. This will intentionally overwrite the existing file.
df.to_csv("servo_data.csv", index=False)