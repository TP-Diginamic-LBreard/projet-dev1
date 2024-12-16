# DIGICHEES API

## Installation

```
python -m venv venv

# Windows (PowerShell)
venv\bin\activate

# Linux
source venv/bin/activate

pip install -r requirements.txt
```

## Create database

Open mariaDB client

```
# if database isn't created 
CREATE DATABASE projet_dev

use projet_dev
```

## Create .env file

Create a `.env` file in the project's root directory and add the following into it, replacing `[USER]` and `[PASSWORD]` with your own values. Modify the connection string at your convenience (if using Nix: supply the `?unix_socket=<path>` URI parameter and remove the `localhost` host parameter)

```
DB_CONN='mysql+pymysql://[USER]:[PASSWORD]@localhost/projet_dev'
```

## Connect to database

In the shell with venv activated

```
uvicorn src.main:app --reload
```


<!-- all the readme stuff here -->

## Contributeurs

- Loïc Bréard
- Rémy Clairet
- Nabiya Chergui
- Amaury Viala
