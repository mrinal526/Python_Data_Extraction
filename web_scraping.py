# Description: This script fetches the menu data of a restaurant from Swiggy and saves it to a CSV file.
# Usage: python web_scraping.py <restaurant_id>
# Example: python web_scraping.py 217542
# importing the required libraries
import sys
import requests
import pandas as pd

# Function to fetch the menu data of a restaurant from Swiggy
def fetch_menu_data(restaurant_id):
    url = f"https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId={restaurant_id}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    menu_data = response.json()
    # print(menu_data) # for testing prupose
    return menu_data


# Function to extract the menu details from the menu data
def extract_menu_details(menu_data):
    print("Extracting menu details...")
    # Create an empty list to store the menu items
    menu_items = []
    
    # Check if 'cards' key exists in menu_data
    if 'cards' in menu_data["data"]:
        # Iterate through each card in the 'cards' list
        for card in menu_data["data"]['cards']:
            # Check if the card is a 'groupedCard'
            if 'groupedCard' in card:
                # Iterate through each 'card' in the 'REGULAR' group
                for regular_card in card['groupedCard']['cardGroupMap']['REGULAR']['cards']:
                    # Check if the card contains 'itemCards'
                    if 'itemCards' in regular_card['card']['card']:
                        # Iterate through each 'itemCard'
                        for item_card in regular_card['card']['card']['itemCards']:
                            # Check if the itemCard is a dish
                            if '@type' in item_card['card'] and item_card['card']['@type'] == 'type.googleapis.com/swiggy.presentation.food.v2.Dish':
                                info = item_card['card']['info']
                                menu_item = {
                                    'name': info.get('name'),
                                    'category': info.get('category'),
                                    'description': info.get('description')
                                }
                                menu_items.append(menu_item)
                                print(menu_item)
    else:
        print("Unexpected data structure:", menu_data)
    # fir tessting prupose
    print(f"Extracted {len(menu_items)} items. {menu_items}")
    return menu_items




# Function to save the menu items to a CSV file
def create_csv(menu_items):
    df = pd.DataFrame(menu_items)
    df.to_csv('menu_data.csv', index=False)

if __name__ == '__main__':
    # Check if restaurant_id is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a restaurant_id as a command-line argument.")
        sys.exit(1)
    # Get the restaurant_id from the command-line argument
    restaurant_id = sys.argv[1]


    # Error handling
    # Fetch the menu data and save it to a CSV file
    try:
        menu_data = fetch_menu_data(restaurant_id)
        menu_items = extract_menu_details(menu_data)
        create_csv(menu_items)
        print("Menu data has been successfully extracted and saved to menu_data.csv.")
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching menu data:", str(e))
    except KeyError:
        print("Invalid restaurant_id or error in menu data.")