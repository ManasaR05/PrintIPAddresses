import json
import sys

def main(filename):
    try:
        # Opens the file and loads the JSON data
        with open(filename, 'r') as json_file:
            file_data = json.load(json_file)
    except FileNotFoundError:
        # Handles the exception if the file with the given filename is not present
        print(f"Error: File '{filename}' not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        # Handles the exception if the JSON file is not in the right format or is invalid
        print(f"Error: Invalid JSON in '{filename}'.", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        # Handles any other exception that arises
        print("Unexpected Error: ", e)
