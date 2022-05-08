# Misskey-Bot-CeilingFox
Python code of CeilingFox https://ente.fun/@ceilingfox

# Dependencies
This bot is working with the MiPA framework of [yupix](https://github.com/yupix)
You can find it here: https://github.com/yupix/MiPA

MiPa needs Python 3.10 to run. Please make sure to have `python3.10` installed. (Be aware that some programs still need python3.8 or python3.9 to run)

Please install following packages via `pip` or `poetry`
```
psycopg2-binary
configparser
git+https://github.com/yupix/mipa.git
mipac
usjon
msgpack
```

```bash
# pip
pip install -r requirements.txt

# poetry
poetry env use 3.10.x # When using a virtual environment
poetry install
```

# Configuration
This bot is thought to be run on the same server as the PostgresDB.
It checks every 12 hours if there are new Blobfox emojis added to the Database and writes them into the `blobfox`-File
The script reads the emojis from this file to get any emoji.

You can easily edit `LoadEmojis()` in the file ceilingfox.py to change what emoji he catches.

To run you must provide an API token.
In Misskey you can get one from "Settings"->"API"->"Generate Token" (Never let anyone know that token or they can post for your bot)

Edit `example-bot.cfg` to add your Information and rename it to `bot.cfg`

## Contributers
A big thank you to [Yupix](https://github.com/yupix/) for all the help with the MiPA framework and making the code more readable!

# Important
Works on my machine!
