pip-upgrade:
	pip install --upgrade pip

pip-install:		
	pip install -r requirements.txt

make-env:
	source env-store/bin/activate 

format:
	black *.py

d-build:
	docker build -t fmt-rest-api-new_store-v2 .

d-run:
	docker run -d -p 80:5000 fmt-rest-api-new_store