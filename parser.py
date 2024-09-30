import json
import re
from urllib.parse import urlparse, parse_qs

# Function to extract file ID from Google Drive URL
def extract_file_id(drive_url):
    # Use regex to extract the file ID from Google Drive URL
    match = re.search(r"(?<=\/d\/)(.*?)(?=\/)", drive_url)
    if match:
        return match.group(0)
    return None

# Function to generate the download link
def generate_download_link(file_id):
    return f"https://drive.google.com/uc?export=download&id={file_id}"

# Function to load the existing data from JSON file
def load_json_data():
    with open("data.json", "r") as file:
        return json.load(file)

# Function to save updated data back to JSON file
def save_json_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# Main function to populate the data.json
def populate_json():
    # Load the existing data
    data = load_json_data()

    # Step 1: Get the section (dsa, los, etc.)
    section = input("Enter the section (e.g., dsa, los): ").strip()

    # Check if the section exists in data
    if section not in data:
        print(f"Section '{section}' not found in the data.")
        return

    # Step 2: Get the array within the section (practical, assignment, etc.)
    array_name = input("Enter the array name (e.g., practical, assignment): ").strip()

    # Check if the array exists in the section
    if array_name not in data[section]:
        print(f"Array '{array_name}' not found in the section '{section}'.")
        return

    # Step 3: Gather the details to add
    name = input("Enter the name of the item: ").strip()
    preview_link = input("Enter the preview link (Google Drive link): ").strip()

    # Step 4: Extract file ID and generate the download link
    file_id = extract_file_id(preview_link)
    if file_id is None:
        print("Invalid Google Drive URL. File ID could not be extracted.")
        return

    download_link = generate_download_link(file_id)

    # Step 5: Get the last modified date
    last_modified = input("Enter the last modified date (dd-mm-yyyy): ").strip()

    # Create the new item
    new_item = {
        "name": name,
        "preview": preview_link,
        "download": download_link,
        "lastModified": last_modified
    }

    # Add the new item to the specified array in the section
    data[section][array_name].append(new_item)

    # Step 6: Save the updated data back to the JSON file
    save_json_data(data)

    print("Data has been updated successfully.")

# Run the function to populate the JSON file
populate_json()

