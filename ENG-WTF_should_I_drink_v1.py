import csv
import openai

# Add your OpenAI API key here
openai.api_key = 'YOUR OPEN API KEY'

# Path to the CSV file
file_path = 'YOUR FILE PATH'

# Define your ASCII art logo
logo = """
*                           )   *
              )     *      (
    )        (                   (
   (          )     (             )
    )    *           )        )  (
   (                (        (      *
    )                )        )
              [ ]            (
       (  *   |-|       *     )    (
 *      )     |_|        .          )
       (      | |    .  
 )           /   \     .    ' .        *
(           |_____|  '  .    .  
 )          | ___ |  \~~~/  ' .   (
        *   | \ / |   \_/  \~~~/   )
            | _Y_ |    |    \_/   (
*           |-----|  __|__   |      *
            `-----`        __|__     
            Cheers!
"""
# Define your ASCII logo text
logotext = """
__        _______ _____       _                 _     _  
\ \      / /_   _|  ___|  ___| |__   ___  _   _| | __| | 
 \ \ /\ / /  | | | |_    / __| '_ \ / _ \| | | | |/ _` | 
  \ V  V /   | | |  _|   \__ \ | | | (_) | |_| | | (_| | 
 __\_/\_/  _ |_| |_|     |___/_|_|_|\___/ \__,_|_|\__,_| 
|_ _|   __| |_ __(_)_ __ | | _|__ \                      
 | |   / _` | '__| | '_ \| |/ / / /                      
 | |  | (_| | |  | | | | |   < |_|                       
|___|  \__,_|_|  |_|_| |_|_|\_\(_)     by Marius                                                                                                        
"""
print(logotext)

def collect_wine_data(file_path):
    wines = []
    with open(file_path, mode='r', encoding='ISO-8859-1') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            wine_info = {
                'Wine': row['Wine'],
                'Vintage': row['Vintage'],
                'Producer': row['Producer'],
                'Type': row['Type'],
                'Locale': row['Locale']
            }
            wines.append(wine_info)
    # Display the collected wine data
    return wines

def get_vegetarian_pairings(wine_info):
    prompt = (
        f"I have the following wines: Name: {wine_info['Wine']}, "
        f"Vintage: {wine_info['Vintage']}, Producer: {wine_info['Producer']}, "
        f"Type: {wine_info['Type']}, Locale: {wine_info['Locale']}. "
        "Please describe the wine in one sentence and recommend in a list three good vegetarian food pairings with these wines. After each recommendation briefly describe why this dish fits the wine."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are my humorous sommelier."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    
    return response.choices[0].message['content'].strip()

def check_drinking_window(wine_info):
    # Example logic for checking the drinking window
    # In a real-world application, you would consult a data source that specifies drinking windows
    current_year = 2025
    vintage_year = int(wine_info['Vintage'])
    years_old = current_year - vintage_year
    
    # Simplistic rule: wine is best at 5-15 years from vintage
    if 5 <= years_old <= 15:
        return f"The vintage {wine_info['Vintage']} of {wine_info['Wine']} is currently in a good drinking window."
    else:
        if years_old < 5:
            return f"The vintage {wine_info['Vintage']} of {wine_info['Wine']} may be too young."
        else:
            return f"The vintage {wine_info['Vintage']} of {wine_info['Wine']} may have passed its optimal drinking window."

def main(file_path):
    wines = collect_wine_data(file_path)
    
    # One-time user input to select the option
    print("Choose an option:")
    print("1. Food recommendations for all wines")
    print("2. Check drinking window for all wines\n")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    for wine in wines:
        print(f"Wine: {wine['Wine']} - Vintage: {wine['Vintage']}")
        
        if choice == '1':
            # Option 1: Get food recommendations
            pairing_suggestion = get_vegetarian_pairings(wine)
            print(f"Food Recommendations: {pairing_suggestion}\n")
        elif choice == '2':
            # Option 2: Check if the vintage is in the optimal drinking window
            drinking_window = check_drinking_window(wine)
            print(f"Drinking Window: {drinking_window}\n")
        else:
            print("Invalid choice. Please restart the program and enter 1 or 2.\n")
            break
        
        # Print a separator for clarity
        print("-"*40 + "\n")

# Retrieve and process wines
main(file_path)

print(logo)
