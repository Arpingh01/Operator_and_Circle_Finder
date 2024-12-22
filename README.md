# Operator_and_Circle_Finder

This project automates the process of extracting mobile number details (e.g., operator, circle) from the Paytm website using Python, Selenium, and Pandas.
The scraped data is stored in a CSV file for further analysis or use.

## Features
- Reads mobile numbers from a CSV file.
- Scrapes operator and circle details for each mobile number from Paytm's recharge page.
- Logs the extracted data (mobile number, operator, circle, date and time) into a CSV file.
- Implements error handling and logging for failed data extractions.

## Prerequisites
1. **Python**: Ensure Python 3.7+ is installed on your system.
2. **Google Chrome**: Install the latest version of Google Chrome.
3. **ChromeDriver**: Download the ChromeDriver version compatible with your Chrome browser from [here](https://chromedriver.chromium.org/downloads).
4. **Python Libraries**:
   - Selenium
   - Pandas

   You can install these using pip:
   ```bash
   pip install selenium pandas
   ```
   
## Error Handling
- If the ChromeDriver path is invalid, the script will raise a `FileNotFoundError`.
- If data extraction fails for a mobile number, the script logs the error and continues with the next number.

## Notes
- Ensure the Paytm website's structure hasn't changed; otherwise, the XPaths in the script may need to be updated.
- This script is for educational purposes. Respect website terms of service when scraping data.

## Acknowledgments
- Selenium documentation: [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)
- Paytm website: [https://paytm.com](https://paytm.com)

