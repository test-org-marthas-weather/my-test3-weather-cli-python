# Weather CLI Tool 🌤️

A simple Python command-line interface (CLI) tool that fetches current weather information for any given city.

## 📋 Description

This project demonstrates how to build a practical CLI application in Python that interacts with weather APIs to retrieve and display real-time weather data. Perfect for learning API integration, command-line argument parsing, and environment variable management.

## 🚀 Features

- Fetch current weather data for any city
- Clean command-line interface
- Secure API key management using environment variables
- Error handling for invalid cities and API failures
- JSON response parsing and formatted output

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **requests** - HTTP library for making API calls
- **python-dotenv** - Environment variable management
- **argparse** - Command-line argument parsing (built-in)

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/test-org-marthas-weather/my-test3-weather-cli-python.git
cd my-test3-weather-cli-python
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your weather API key:
```bash
WEATHER_API_KEY=your_api_key_here
```

> **Note:** You can get a free API key from services like [OpenWeatherMap](https://openweathermap.org/api) or [WeatherAPI](https://www.weatherapi.com/).

## 💻 Usage

Run the CLI tool with a city name:

```bash
python main.py --city "London"
```

Or use the short form:

```bash
python main.py -c "New York"
```

## 📚 Documentation

For detailed library documentation and implementation references, see:
- [Reference Guide](docs/reference_guide.md) - Comprehensive documentation on the libraries used

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 🔗 Links

- Repository: [https://github.com/test-org-marthas-weather/my-test3-weather-cli-python](https://github.com/test-org-marthas-weather/my-test3-weather-cli-python)
- Issues: [https://github.com/test-org-marthas-weather/my-test3-weather-cli-python/issues](https://github.com/test-org-marthas-weather/my-test3-weather-cli-python/issues)

---

Built with ❤️ using Python
