Make Jobmine Great Again!

# Getting set up

Make sure you have mongo installed and running

Recommended to have virtualenv installed for the Python environment

## Quick setup - Installs python and node dependencies
```
$ make install
```

## Manual setup
### Installing python dependencies
```
$ sudo pip install -r requirements.txt
```

### Installing npm dependencies
```
$ npm install
```

# Running the application

## Using makefile
```
make local
```
Starts mongodb, transpiler, and server

## Manually
Make sure you have mongo running:
```
$ mongod --db_path mongo
```
Create the `mongo` folder if necessary:
```
$ mkdir mongo
```
Start the server:
```
$ python app.py
```

If you need the frontend, you also need to transpile `.jsx` files:
```
$ npm run transpile
```

# Development tools
## Database Shell
Use for testing queries, manipulating data, or experimenting with
methods/classes
```
$ python dbshell.py
```

# Miscellaneous
## Clean up compiled files
```
$ make clean
```
