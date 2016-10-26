install:
	sudo pip install -r requirements.txt
	npm install

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf static/js npm-debug.log static/npm-debug.log
