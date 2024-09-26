# tests/test_weather.py

import pytest
from weather_info_fetcher.weather import get_weather

def test_get_weather():
    result = get_weather("London")
    assert result is not None
    assert "weather" in result
    assert result["name"] == "London"
    
if __name__ == "__main__":
    pytest.main()