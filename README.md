# Discord Message Relay Bot

This bot is designed to relay messages from one Discord channel to another. The bot uses the Discord API to fetch messages from a source channel and then sends them to a target channel. The bot runs continuously and checks for new messages every 30 seconds.

## Features
- Fetches messages from a source Discord channel.
- Relays messages to a target Discord channel.
- Supports checking for new messages every 30 seconds.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have Python 3.x installed.
- You have `discord.py` installed (`pip install discord.py`).
- You have `requests` library installed (`pip install requests`).

## Installation
1. Clone the repository or download the script to your local machine.
2. Install the required Python libraries:
    ```bash
    pip install discord.py requests
    ```

## Configuration
1. Open the script file and set your bot token, user token, and channel IDs in the following variables:
    ```python
    BOT_TOKEN = 'your_bot_token'
    USER_TOKEN = 'your_user_token'
    SOURCE_CHANNEL_ID = your_source_channel_id  # ID of the source channel
    TARGET_CHANNEL_ID = your_target_channel_id  # ID of the target channel
    ```

2. Save the changes to the script file.

## Usage
1. Run the script using Python:
    ```bash
    python relaybot.py
    or
    python3 relaybot.py
    ```

2. The bot will log in and start monitoring the source channel for new messages. Any new messages found will be relayed to the target channel.
