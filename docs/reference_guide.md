# 📚 Library Reference Guide

This document provides a comprehensive reference for the Python libraries used in this Weather CLI project.

---

## Requests Library

### Overview
**Requests** is a simple, elegant, and widely-used Python HTTP library that makes sending HTTP requests incredibly easy.

- **Source:** [https://requests.readthedocs.io](https://requests.readthedocs.io)
- **Reputation:** High

### Basic GET Request

```python
import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)  # 200
print(r.headers['content-type'])  # 'application/json; charset=utf8'
data = r.json()
```

### Handling JSON Responses

```python
import requests

r = requests.get('https://api.example.com/data')

if r.status_code == requests.codes.ok:
    commit_data = r.json()
    print(commit_data.keys())
else:
    print(f"Request failed with status code: {r.status_code}")
```

### Error Handling

```python
import requests
from requests.exceptions import JSONDecodeError, RequestException

try:
    r = requests.get('https://api.example.com/data')
    r.raise_for_status()
    data = r.json()
except JSONDecodeError:
    print("Error: Response is not valid JSON")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except RequestException as e:
    print(f"Request failed: {e}")
```

---

## Python-dotenv Library

### Overview
**python-dotenv** reads key-value pairs from `.env` files and sets them as environment variables.

- **Source:** [https://github.com/theskumar/python-dotenv](https://github.com/theskumar/python-dotenv)
- **Reputation:** High

### Basic Usage

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get('API_KEY')
```

### .env File Format

```bash
DATABASE_URL=postgresql://localhost/mydb
API_KEY=your-weather-api-key-here
DEBUG=true
```

### Advanced Loading

```python
import os
from dotenv import load_dotenv

load_dotenv(override=True)
load_dotenv(dotenv_path='/path/to/production.env')
load_dotenv(verbose=True)
```

---

## Best Practices

### Security
- Never commit `.env` files to version control
- Add `.env` to your `.gitignore` file
- Use `.env.example` to document required variables

### Error Handling
- Always check HTTP status codes before parsing responses
- Use try-except blocks for network requests
- Handle missing environment variables gracefully

### API Usage
- Respect rate limits
- Use timeout parameters for requests
- Validate user input before making API calls

---

*This reference guide was compiled from official documentation sources via Context7.*
