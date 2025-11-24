import json
import os

# This file is just for loading and saving the study data.
# Everything will be stored in one JSON file.

DATA_FILE = "data/study_data.json"

def load_data():
    # If the data folder doesn't exist, just make it
    if not os.path.exists("data"):
        os.makedirs("data")

    # If the json file doesn't exist yet, return empty data
    if not os.path.isfile(DATA_FILE):
        return {
            "subjects": [],
            "tasks": [],
            "sessions": []
        }

    # Otherwise try to read the file
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data
    except:
        # If something goes wrong, just return empty structure
        return {
            "subjects": [],
            "tasks": [],
            "sessions": []
        }

def save_data(data):
    # Save the given dictionary back into the json file
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)