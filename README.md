## Getting set up

Make sure you have mongo installed

Recommended to have virtualenv installed for the Python environment

To transpile jsx, run

npm install babel-preset-es2015 babel-preset-react -g
babel --presets es2015,react --watch jsx/ --out-dir js/

Then you can serve it from the static directory

# Quick setup - Installs python and node dependencies
`$ make install`

# Manual setup
## Installing python dependencies
`$ sudo pip install -r requirements.txt`

## Installing npm dependencies
`$ npm install`

# Clean up compiled files
`$ make clean`

# Transpiling jsx
`$ npm run transpile`
