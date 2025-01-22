from datetime import datetime
from meteostat import Point, Hourly
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

class TemperatureReporter:
    def __init__(self, location="Wrocław"):
        """
        Initialize the TemperatureReporter with a location.
        
        Args:
            location (str): Name of the location (city, address, etc.). Defaults to "Wrocław"
        """
        self.geolocator = Nominatim(user_agent="tempreporter2")
        self.set_location(location)
    
    def set_location(self, location):
        """
        Set a new location for temperature reporting.
        
        Args:
            location (str): Name of the location (city, address, etc.)
            
        Returns:
            bool: True if location was set successfully, False otherwise
        """
        try:
            location_data = self.geolocator.geocode(location)
            if location_data is None:
                self.point = Point(51.1, 17.0333)  # Default to Wrocław if location not found
                return False
                
            self.point = Point(location_data.latitude, location_data.longitude)
            return True
        except (GeocoderTimedOut, GeocoderUnavailable):
            self.point = Point(51.1, 17.0333)  # Default to Wrocław on error
            return False
    
    def get_current_temp(self):
        """
        Get the current temperature for the set location.
        
        Returns:
            float or None: Current temperature in Celsius, or None if data is unavailable
        """
        now = datetime.now()
        data = Hourly(self.point, now, now).fetch()
        
        if not data.empty:
            return data.iloc[-1]['temp']
        return None
