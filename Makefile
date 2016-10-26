install:
	sudo pip install -r requirements.txt
	npm install

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -r static/js
