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
        sys.exit(3)

    try:
        vm_private_ips = file_data["vm_private_ips"]["value"]
    except KeyError:
        # Handles the exception if the required Keys are not present in the JSON file
        print(f"Error: 'vm_private_ips' or 'value' key not found in '{filename}'.", file=sys.stderr)
        sys.exit(4)

    # Process network information if present
    network_ips = {}
    if "network" in file_data:
        for vm in file_data["network"]["vms"]:
            name = vm["attributes"]["name"]
            network_ips[name] = vm["attributes"]["access_ip_v4"]

    # Print IP addresses
    for name, ip in vm_private_ips.items():
        # Get network IP
        network_ip = network_ips.get(name, "")
        # Print the IP address and network IP (if present) on the same line
        print(ip, network_ip)


if __name__ == "__main__":
    # To verify the correct number of Command line arguments to run the script
    if len(sys.argv) != 2:
        print("Usage: ip_print FILENAME", file=sys.stderr)
        sys.exit(5)
    # Fetch the filename from the second argument in the command-line arguments
    filename = sys.argv[1]
    # Calls the main function with the provided filename
    main(filename)