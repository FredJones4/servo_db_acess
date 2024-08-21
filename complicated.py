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
    for curr_page_number in range(1, 2):
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
                base_data = [
                    cells[0].find_element(By.TAG_NAME, "a").text,
                    cells[1].find_element(By.TAG_NAME, "a").text,
                    cells[2].text,
                    cells[3].text.replace(" oz", ""),  # Extract weight
                    *cells[4].text.replace(" in", "").split()  # Extract dimensions
                ]

                # Clean and split Torque and Speed data
                torque_data = clean_split_data(cells[5].text)
                speed_data = clean_split_data(cells[6].text)

                # Extract other data
                other_data = [
                    cells[7].text,
                    cells[8].text,
                    cells[9].text,
                    cells[10].text
                ]

                # Combine and write each set of Torque and Speed data
                for t_data, s_data in zip(torque_data, speed_data):
                    writer.writerow(base_data + [t_data[0], t_data[1], s_data[0], s_data[1]] + other_data)

# Close the browser
driver.quit()
