from geopy.distance import geodesic
from datetime import datetime
current_time = datetime.now().strftime("%H:%M")

def calculate_distance(user_locations,spot_location):
    return round(geodesic(user_locations,spot_location).km,2)

def is_open_spot(row):
    open_time = row['opening_time']
    close_time = row['closing_time']
    if open_time <= current_time<= close_time:
        return "Open"
    else:
        return 'Close'