clean:
	git clean -Xfd

install:
	pip install --requirement=requirements/tests.txt

test:
	coverage run setup.py test
	flake8 localflavor
	coverage report

travis: test
