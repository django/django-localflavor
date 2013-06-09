clean:
	git clean -Xfd

install:
	pip install --requirement=requirements/tests.txt

test:
	flake8 --ignore=W801,E128,E501,W402 localflavor
	coverage run `which django-admin.py` test --settings=localflavor.tests.settings localflavor
	coverage report

travis: test
