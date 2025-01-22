from datetime import datetime
from meteostat import Point, Hourly

class TemperatureReporter:
    def __init__(self):
        self.wroclaw = Point(51.1, 17.0333)
    
    def get_current_temp(self):
        now = datetime.now()
        data = Hourly(self.wroclaw, now, now).fetch()
        
        if not data.empty:
            return data.iloc[-1]['temp']
        return None