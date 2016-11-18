install:
	sudo pip install -r requirements.txt
	npm install

local:
	mongod --dbpath mongo &
	babel --presets es2015,react --watch static/jsx/ --out-dir static/js/ &
	python app.py

init_data:
	PYTHONPATH=. python scripts/seed.py

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf static/js npm-debug.log static/npm-debug.log
