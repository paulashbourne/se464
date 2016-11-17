install:
	sudo pip install -r requirements.txt
	npm install

init_data:
	PYTHONPATH=. python scripts/seed.py

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf static/js npm-debug.log static/npm-debug.log
