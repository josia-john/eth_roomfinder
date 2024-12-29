import subprocess
import json
from datetime import datetime
from urllib.parse import quote

def get_room_names():
    url = "https://ethz.ch/bin/ethz/roominfo?path=/rooms"
    # Use curl to fetch the data
    try:
        result = subprocess.run(
            ["curl", "-s", url],  # -s flag makes curl silent
            capture_output=True,
            text=True,
            check=True
        )
        with open("data/rooms.json", "w") as f:
            f.write(result.stdout)
        # Parse JSON data
        data = json.loads(result.stdout)

        # Process JSON data (e.g., extract room names)
        def extract_room_names(data):
            room_names = []
            for entry in data:
                building = entry.get("building", "")
                floor = entry.get("floor", "")
                room = entry.get("room", "")
                # Construct room name
                room_name = f"{building} {floor} {room}"
                room_names.append(room_name)
            return room_names

        # Get room names
        room_names = extract_room_names(data)

        # Print room names
        return room_names

    except subprocess.CalledProcessError as e:
        print(f"Error executing curl: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")


def generate_room_url(room_name, start_date, end_date):
    """Generate the ETHZ room allocations URL."""
    encoded_room_name = quote(room_name)
    return f"https://ethz.ch/bin/ethz/roominfo?path=/rooms/{encoded_room_name}/allocations&from={start_date}&to={end_date}"


def fetch_room_allocations_with_curl(url):
    """Fetch room allocations using curl."""
    try:
        result = subprocess.run(
            ["curl", "-s", url],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing curl: {e}")
        return ""
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
        return ""


rooms = get_room_names()
for r in rooms:
    url = generate_room_url(r, datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%Y-%m-%d'))
    with open("data/"+r, "w") as f:
        f.write(fetch_room_allocations_with_curl(url))

