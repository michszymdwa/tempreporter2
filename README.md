# Temperature Reporter

A simple Python library for retrieving current temperature data for Wrocław, Poland using the Meteostat API.

## Features

- Retrieves real-time temperature data for Wrocław (coordinates: 51.1°N, 17.0333°E)
- Uses the reliable Meteostat API for weather data
- Simple and clean interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/michszymdwa/tempreporter2.git
cd tempreporter2
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from temperature_reporter import TemperatureReporter

# Create an instance of the reporter
reporter = TemperatureReporter()

# Get the current temperature
temperature = reporter.get_current_temp()

if temperature is not None:
    print(f"Current temperature in Wrocław: {temperature}°C")
else:
    print("Unable to fetch temperature data")
```

## Requirements

- Python 3.x
- meteostat >= 1.1.0

## API Reference

### TemperatureReporter

#### `__init__()`
Initializes the reporter with Wrocław's coordinates.

#### `get_current_temp()`
Returns the current temperature in Celsius for Wrocław.
- Returns: Float (temperature in °C) or None if data is unavailable

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

[michszymdwa](https://github.com/michszymdwa)