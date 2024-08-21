from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re

# Initialize the Chrome driver
driver = webdriver.Chrome()


# Function to clean and split Torque/Speed data
def clean_split_data(data):
    # Split by line break
    split_data = data.split('\n')
    cleaned_data = []

    for item in split_data:
        # Use regex to extract just the numeric part
        voltage = re.search(r"(\d+(\.\d+)?)V", item).group(1)
        value = re.search(r"(\d+(\.\d+)?)", item.split()[-2]).group(1)
        cleaned_data.append((voltage, value))

    return cleaned_data


# Open a CSV file to write the data
with open("servo_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    header = ["Make", "Model", "Modulation", "Weight(oz)", "L(in)", "W(in)", "H(in)", "Torque(which_V)",
              "Torque(oz-in)", "Speed(which_V)", "Speed(s/60°)", "Motor Type", "Rotation", "Gear Material",
              "Typical Price"]
    writer.writerow(header)

    # Iterate through pages 1 to 10
    # TODO: update with this prompt:
    """
    YES!!!!! ok, one thing I forgot to mention: sometimes, this database has (add) when the entry is blank. This is a problem for the columns that need to be parsed, especially when one column (like Torque) is "4.8V 0.07 s/60 
6.0V 0.06 s/60 " and the other (Speed) is (add) or vice versa

    """
    for curr_page_number in range(1, 102):
        print(curr_page_number)
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

                # Combine and write each set of Torque and Speed data
                for t_data, s_data in zip(torque_data, speed_data):
                    cleaned_price = typical_price.replace("$", "")  # Remove the "$" symbol from the price
                    writer.writerow(
                        [make, model, modulation, weight, length, width, height, t_data[0], t_data[1], s_data[0],
                         s_data[1], motor_type, rotation, gear_material, cleaned_price])

# Close the browser
driver.quit()
