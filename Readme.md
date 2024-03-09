

# Swiggy Menu Data Extractor

This script allows you to extract menu data from Swiggy's API for a given restaurant ID and save it to a CSV file for further analysis or processing.


***Python must be installed in the system***

## Functionality

The script performs the following tasks:

1. **Fetch Menu Data**: It sends a GET request to Swiggy's API to retrieve menu data for a specific restaurant ID.

2. **Extract Menu Details**: It extracts relevant information such as dish name, category, and description from the fetched menu data.

3. **Create CSV File**: It creates a CSV file containing the extracted menu details for easy storage and analysis.

4. **Handle Errors**: It handles exceptions such as invalid restaurant IDs or errors in menu data retrieval, providing informative error messages.

## How to Use

To use the script, follow these steps:

1. Clone or download the repository to your local machine.

2. Install the required dependencies by running:

        pip install -r requirements.txt


3. Run the script with the desired restaurant ID as a command-line argument:

        python web_scraping.py <restaurant_id>


4. The script will fetch the menu data, extract the relevant details, and save them to a CSV file named `menu_data.csv` in the current directory.

## Requirements

- Python 3.7
- `requests` library (for sending HTTP requests)
- `pandas` library (for data manipulation)

***Install these libraries using command***

        pip install requests pandas

## Example

Suppose you want to extract menu data for a restaurant with the ID `217542`. You can run the script as follows:

        python web_scraping.py 217542


The script will fetch the menu data for the restaurant with ID `217542`, extract the menu details, and save them to a CSV file named `menu_data.csv`.

## Note

Ensure you have a stable internet connection to fetch menu data from Swiggy's API. Additionally, make sure the provided restaurant ID is valid.

