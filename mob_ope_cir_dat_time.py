import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime  # Importing datetime module
import csv  # For handling CSV operations

# Path to your chromedriver.exe file
driver_path =  "C:\\Users\\DELL\\PycharmProjects\\Data_Scrapper_Project\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"

# Check if the driver path is valid
if not os.path.isfile(driver_path):
    raise FileNotFoundError(f"ChromeDriver not found at {driver_path}. Please verify the path.")

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")

# Set up the Service object
service = Service(driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Read mobile numbers from the 'mobileNumber1' column in the specified CSV file
data_file = 'Indiamart 13_cleaned_cleaned.csv'
df = pd.read_csv(data_file)

# Verify column names and make sure 'mobileNumber1' exists
if 'mobileNumber1' not in df.columns:
    raise KeyError("Column 'mobileNumber1' not found in the input CSV file.")

# Extract the mobile numbers from the 'mobileNumber1' column
mobile_numbers = df['mobileNumber1']

# Path for the output CSV file
output_file = r'Indiamart_Extracted_Data.csv'

# Create the CSV file and write headers if the file doesn't exist
if not os.path.exists(output_file):
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Mobile Number', 'Operator', 'Circle', 'Date', 'Time'])  # Write headers

# Iterate over each mobile number
for mobile_number in mobile_numbers:
    print(f"Processing {mobile_number}...")  # Debugging statement

    # Open Paytm recharge page
    driver.get('https://paytm.com/recharge')
    time.sleep(3)  # Add a small delay to ensure the page loads completely

    try:
        # Wait for the Mobile Number input field to be present
        mobile_number_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='app']/div/div[4]/div[1]/div/div/div[2]/div[2]/ul/li[1]/div[1]/div/input"))
        )
        mobile_number_input.clear()
        mobile_number_input.send_keys(str(mobile_number))
        mobile_number_input.send_keys(Keys.RETURN)

        # Wait for a few seconds before extracting the operator and circle details (to slow down the process)
        time.sleep(3)  # Delay added here to slow down the extraction process

        # Wait for operator and circle details to be visible using the provided XPaths
        operator = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='app']/div/div[4]/div[1]/div[1]/div/div/div[2]/ul/li[2]/div[1]/div/input"))
        ).get_attribute('value') or 'N/A'  # Get the value or default to 'N/A'

        circle = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id='app']/div/div[4]/div[1]/div[1]/div/div/div[2]/ul/li[3]/div[1]/div/input"))
        ).get_attribute('value') or 'N/A'  # Get the value or default to 'N/A'

        print(f"Operator: {operator}, Circle: {circle}")

    except Exception as e:
        print(f"Error extracting data for {mobile_number}: {e}")
        operator = 'N/A'
        circle = 'N/A'

    # Get the current date and time
    current_datetime = datetime.now()
    scraping_date = current_datetime.strftime('%Y-%m-%d')  # Extract date
    scraping_time = current_datetime.strftime('%H:%M:%S')  # Extract time

    # Append the data to the CSV file
    with open(output_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([mobile_number, operator, circle, scraping_date, scraping_time])  # Append data

    print(f"Data for {mobile_number} saved to {output_file}")

# Close the browser
driver.quit()

print("Data scraping completed!")







