# DIGICHEES API

## Installation

Run the following commands from the project's root directory in a terminal emulator of your choice:

```
python -m venv venv

# Windows (PowerShell)
venv\bin\activate

# Linux/MacOS/etc.
source venv/bin/activate

pip install -r requirements.txt
```

### Create database

Open your MySQL/MariaDB client and run the following commands:

```
# if database isn't created 
CREATE DATABASE projet_dev

use projet_dev
```

### Configuration

Create a `.env` file in the project's root directory and add the following into it, replacing `[USER]` and `[PASSWORD]` with your own values. Modify the connection string at your convenience (if using Nix: supply the `?unix_socket=<path>` URI parameter and remove the `localhost` host parameter)

```
DB_CONN='mysql+pymysql://[USER]:[PASSWORD]@localhost/projet_dev'
```

## Run API

Run the following command from the project's root directory in a terminal emulator with the virtual environment activated:

```
uvicorn src.main:app --reload
```


<!-- all the readme stuff here -->

## Contributeurs

- Loïc Bréard
- Rémy Clairet
- Nabiya Chergui
- Amaury Viala
