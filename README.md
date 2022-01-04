# Misskey-Bot-CeilingFox
Python code of CeilingFox https://ente.fun/@ceilingfox

# Dependencies
This bot is working with the mi.py framework
You can find it here: https://github.com/yupix/Mi.py

Mi.py needs Python 3.9 to run. Please make sure to have `python3.9` and `python3.9-dev` installed

Please install following packages via `pip`
```
psycopg2-binary
configparser
```

# Configuration
This bot is thought to be run on the same server as the PostgresDB.
It checks every 12 hours if there are new blobfox emojis added to the Database and writes them into the `blobfox`-File
The script reads the emojis from this file to get any emoji.

You can easily edit `LoadEmojis()` in the file ceilingfox.py to change what emoji he catches.

To run you must provide a API token.
In Misskey you can get one from "Settings"->"API"->"Generate Token" (Never let anyone know that token or they can post for your bot)

Edit `example-bot.cfg` to add your Information and rename it to `bot.cfg`

# Important
Works on my machine!
