# Introduction

This repository contains a basic example of interacting with the OpenAI API using Python. The code in `app.py` demonstrates how to create a chat completion using the OpenAI API.

# Functionality

The `app.py` file contains a Python script that:
- Loads environment variables from a .env file
- Creates an OpenAI client using the openai library
- Sends a chat completion request to the OpenAI API
- Prints the response from the API

# Requirements

To run this code, you'll need to have the following installed:
- Python 3
- openai
- dotenv
- A `.env` file with your OpenAI API key and base URL

# Usage
- Clone this repository using git clone
- Create a .env file with your OpenAI API key and base URL
- Install the required libraries using `pip install -r requirements.txt`
- Run the script using python `app.py`

# Example

The script sends a chat completion request to the OpenAI API with the following prompt:
```
"What is in this image?"

The response from the API is then printed to the console.
```

# License
This repository is licensed under the MIT License. Please see [License File](LICENSE.md) for more information.

Let me know if you'd like me to add or modify anything!
