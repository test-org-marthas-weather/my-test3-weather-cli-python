#!/usr/bin/env python3
"""
Weather CLI Tool
A simple command-line interface for fetching current weather information.
"""

import os
import sys
import argparse
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
API_KEY = os.environ.get('WEATHER_API_KEY')
BASE_URL = "https://api.weatherapi.com/v1/current.json"


def validate_api_key():
    """
    Validate that the API key is available in environment variables.
    Exits the program if the key is not found.
    """
    if not API_KEY:
        print("❌ Error: WEATHER_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key:")
        print("  WEATHER_API_KEY=your_api_key_here")
        print("\nYou can get a free API key from: https://www.weatherapi.com/")
        sys.exit(1)


def fetch_weather(city):
    """
    Fetch weather data for a given city.
    
    Args:
        city (str): Name of the city to fetch weather for
        
    Returns:
        dict: Weather data dictionary or None if request fails
    """
    try:
        response = requests.get(
            BASE_URL,
            params={'key': API_KEY, 'q': city},
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 400:
            print(f"❌ Error: City '{city}' not found. Please check the spelling.")
        else:
            print(f"❌ HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching weather data: {e}")
        return None


def display_weather(data):
    """
    Display weather information in a formatted way.
    
    Args:
        data (dict): Weather data dictionary from API
    """
    if not data:
        return
    
    try:
        location = data['location']['name']
        country = data['location']['country']
        temp_c = data['current']['temp_c']
        temp_f = data['current']['temp_f']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind_kph = data['current']['wind_kph']
        
        print("\n" + "="*50)
        print(f"🌤️  Weather in {location}, {country}")
        print("="*50)
        print(f"🌡️  Temperature: {temp_c}°C ({temp_f}°F)")
        print(f"☁️  Condition: {condition}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_kph} km/h")
        print("="*50 + "\n")
    except KeyError as e:
        print(f"❌ Error parsing weather data: Missing key {e}")


def parse_arguments():
    """
    Parse command-line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Fetch current weather information for a given city.',
        epilog='Example: python main.py --city "London"'
    )
    parser.add_argument(
        '-c', '--city',
        type=str,
        required=True,
        help='Name of the city to fetch weather for'
    )
    return parser.parse_args()


def main():
    """
    Main entry point for the Weather CLI tool.
    """
    # Validate API key is available
    validate_api_key()
    
    # Parse command-line arguments
    args = parse_arguments()
    
    # Fetch and display weather data
    print(f"🔍 Fetching weather data for {args.city}...")
    weather_data = fetch_weather(args.city)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
