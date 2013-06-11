clean:
	git clean -Xfd

install:
	pip install --requirement=requirements/tests.txt

test:
	flake8 --ignore=W801,E128,E501,W402 localflavor
	coverage run setup.py test
	coverage report

travis: test
