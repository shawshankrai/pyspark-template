build:
	mkdir ./dist
	cp ./src/main.py ./dist
	cd ./src && zip -x main.py -r ../dist/jobs.zip .