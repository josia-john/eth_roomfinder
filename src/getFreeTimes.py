import subprocess
import json
from datetime import datetime
from datetime import timedelta
from urllib.parse import quote

# URL to fetch JSON data from
def get_room_names():
    path = "data/rooms.json"
    # Use curl to fetch the data
    with open(path, "r") as f:
        result = f.read()
        # Parse JSON data
        data = json.loads(result)

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


def generate_room_path(room_name, start_date, end_date):
    """Generate the ETHZ room allocations URL."""
    return f"data/{room_name}"


def fetch_room_allocations_from_file(path):
    """Fetch room allocations using curl."""
    with open(path, "r") as f:
        result = f.read()
        return json.loads(result)


def get_next_free_time_room(room_name, allocations):
    """Check if the room is free based on current time."""
    res = []
    for allocation in allocations:
        date_from = datetime.fromisoformat(allocation['date_from'])
        date_to = datetime.fromisoformat(allocation['date_to'])
        res.append({"from": date_from, "to": date_to})

    return res

def get_room_info(room_list, start_date, end_date):
    """Determine currently free rooms from the room list."""
    free_rooms = []
    for room in room_list:
        try:
            path = generate_room_path(room, start_date, end_date)
            allocations = fetch_room_allocations_from_file(path)
            if allocations:
                next_free_time = get_next_free_time_room(room, allocations)
                free_rooms.append({"room": room, "info": next_free_time})
        except Exception as e:
            print(f"Error processing room {room}: {e}")
    return free_rooms


def use():

    # Example usage
    room_list = get_room_names()
    start_date = datetime.today().strftime('%Y-%m-%d')
    end_date = datetime.today().strftime('%Y-%m-%d')

    # free_rooms = get_room_info(room_list, start_date, end_date, datetime.now().replace(hour=10))
    free_rooms = get_room_info(room_list, start_date, end_date)
    # print("Currently Free Rooms:")
    # for room in free_rooms:
    #     print(room)
    return free_rooms
