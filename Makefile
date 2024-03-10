default: init build test clean run

init:
	pip install -r requirements.txt

build:
	pip install .

test:
	py.test tests

clean:
	-del /s /q *.db
	-rm -r *.db

run:
	py src/main/main.py

.PHONY: default init build test clean run