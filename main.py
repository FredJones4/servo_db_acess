from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open a CSV file to write the data
with open("servo_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    header = ["Make", "Model", "Modulation", "Weight", "Dimensions (L x W x H)", "Torque", "Speed", "Motor Type", "Rotation", "Gear Material", "Typical Price"]
    writer.writerow(header)

    # Iterate over the first 10 pages
    for curr_page_number in range(1, 2):
        # Navigate to the current page
        driver.get(f"https://servodatabase.com/servos/all?page={curr_page_number}")

        # Wait for the table to load
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.servos")))

        # Scrape the data from the table
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 12:
                data = [
                    cells[0].find_element(By.TAG_NAME, "a").text,
                    cells[1].find_element(By.TAG_NAME, "a").text,
                    cells[2].text,
                    cells[3].text,
                    cells[4].text,
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

print("Data scraping completed and saved to servo_data.csv")
