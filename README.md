# uniborg - Pluggable Telegram Userbot Based on Telethon

## Overview

**uniborg** is a modular [Telegram](https://telegram.org) userbot built on the [Telethon](https://github.com/LonamiWebs/Telethon) framework. Its design allows users to enhance their Telegram experience through a variety of plugins that can be enabled or disabled as needed.

## Features

- **Modular Design**: Easily add or remove plugins to customize functionality.
- **Asynchronous Operation**: Built with Python's [``asyncio``](https://docs.python.org/3/library/asyncio.html) for efficient performance.
- **Event Handling**: Utilizes Telethon's event system to respond to various Telegram events.
- **Simple Variables**: Each plugin gets the `borg`, `logger` and `storage` 
[variables](https://github.com/udf/uniborg/blob/4805f2f6de7d734c341bb978318f44323ad525f1/uniborg/uniborg.py#L66-L68)
to ease their use.

The core features offered by the custom `TelegramClient` live under the
[`uniborg/`](https://github.com/udf/uniborg/tree/master/uniborg)
directory, with some utilities, enhancements and the core plugin.

## Installation

### Prerequisites

Before installing, ensure you have:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- A [Telegram API key](https://my.telegram.org/apps)

### Setup Steps

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/udf/uniborg.git
   ```

2. **Navigate to the Project Directory**:

   ```sh
   cd uniborg
   ```

3. **Switch to the **kate** Branch**:

   ```sh
   git checkout kate
   ```

4. **Install Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

5. **Configure the Userbot**:

   - Rename `api_key.example.py` to `api_key.py`.
   - Edit `api_key.py` to include your Telegram API credentials:
     ```python
     api_id = 'YOUR_API_ID'
     api_hash = 'YOUR_API_HASH'
     ```

6. **Run the Userbot**:

   ```sh
   python stdborg.py
   ```

## Plugin Development

### Creating a New Plugin

1. **Create a New Plugin File**:

   Add a new Python file in the `stdplugins` directory. For example, `stdplugins/myplugin.py`.

2. **Define Event Handlers**:

```python
# stdplugins/myplugin.py
from telethon import events

@borg.on(events.NewMessage(pattern='hi'))
async def handler(event):
    await event.reply('hey')
```

   In this snippet, the bot listens for messages containing 'hi' and responds with 'hey'.
   
   Check out the 
   [plugins](https://github.com/udf/uniborg/tree/master/stdplugins)
   directory to learn how to write your own, and consider reading
   [Telethon's documentation](http://telethon.readthedocs.io/)
   for further information.

## Contributing

### How to Contribute

1. **Fork the Repository**.
2. **Create a New Branch**:
   ```sh
   git checkout -b feature-branch
   ```
3. **Commit Your Changes**:
   ```sh
   git commit -m "Added new feature"
   ```
4. **Push to Your Fork**:
   ```sh
   git push origin feature-branch
   ```
5. **Submit a Pull Request**.

## License

This project is licensed under the [Mozilla Public License 2.0](LICENSE).

## Acknowledgements

- [Telethon](https://github.com/LonamiWebs/Telethon) - The Python Telegram client library powering uniborg.

---

📌 *Note: This README is tailored for the **`kate`** branch of the UniBorg project. Ensure you're on the correct branch when following these instructions.*


