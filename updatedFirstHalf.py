from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open a CSV file to write the data
with open("servo_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the updated header row
    header = ["Make", "Model", "Modulation", "Weight(oz)", "L(in)", "W(in)", "H(in)", "Torque", "Speed", "Motor Type", "Rotation", "Gear Material", "Typical Price"]
    writer.writerow(header)

    # Iterate through pages 1 to 10
    for curr_page_number in range(1, 2):
        driver.get(f"https://servodatabase.com/servos/all?page={curr_page_number}")

        # Wait for the table to load
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.servos")))

        # Scrape the data from the table
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 12:
                # Process weight to extract just the number
                weight_text = cells[3].text
                weight = re.findall(r"\d+\.\d+", weight_text)
                weight = weight[0] if weight else ""

                # Process dimensions to extract L, W, H
                dimensions_text = cells[4].text
                dimensions = re.findall(r"\d+\.\d+", dimensions_text)
                L, W, H = dimensions if len(dimensions) == 3 else ("", "", "")

                data = [
                    cells[0].find_element(By.TAG_NAME, "a").text,
                    cells[1].find_element(By.TAG_NAME, "a").text,
                    cells[2].text,
                    weight,
                    L,
                    W,
                    H,
                    cells[5].text,
                    cells[6].text,
                    cells[7].text,
                    cells[8].text,
                    cells[9].text,
                    cells[10].text
                ]
                writer.writerow(data)

# Close the browser
driver.quit()
