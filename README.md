# YouTube Channel Subscriber Count Check

This Python project uses the YouTube Data API to retrieve the subscriber count of a given YouTube channel. The project works with an API key obtained through the Google Developer Console.

## How to Use

1. **Generate an API Key:**
    - Go to [Google Developer Console](https://console.developers.google.com/).
    - Create a new project and enable YouTube Data API v3.
    - Create an API key in the "Credentials" section.

2. **Make Project Settings:**
    - Add the API key you created to the `api_key` variable in the `main.py` file.
    - Add the product ID of the YouTube channel you want to control to the `channel_id` variable.

3. **Install the Required Library:**
    ```bash
    pip install google-api-python-client
    ```

4. **Run the Project:**
    ```bash
    python main.py
    ```

## Things to Consider

- This project uses the YouTube Data API. Therefore, API limitations and policies should be observed.
- An internet connection is required for the project to work.

## Contributing

- This project is open source. It is open to all kinds of contributions and suggestions.

