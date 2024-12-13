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
Create .env file at project root  
Add needed variable in it : 
```
BDDPASS ="password"
BDDUSER= "username"
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
