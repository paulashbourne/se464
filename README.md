# Getting set up

Make sure you have mongo installed and running

Recommended to have virtualenv installed for the Python environment

## Quick setup - Installs python and node dependencies
```bash
$ make install
```

## Manual setup
### Installing python dependencies
`$ sudo pip install -r requirements.txt`

### Installing npm dependencies
`$ npm install`

# Running the application

Make sure you have mongo running:
`$ mongod --db_path ~/data/db`
Create the `~/data/db` folder if necessary:
``$ mkdir -p ~/data/db`

Start the API Server:
`$ python app.py`

If you need the frontend, you also need to transpile `.jsx` files:
`$ npm run transpile`

# Miscellanious
## Clean up compiled files
`$ make clean`
