clean:
	git clean -Xfd

install:
	pip install --requirement=requirements/tests.txt
	pip install --editable=.

test:
	flake8 --ignore=W801,E128,E501,W402 localflavor
	coverage run --branch --source=localflavor `which django-admin.py` test --settings=localflavor.test_settings localflavor
	coverage report --omit=localflavor/*tests*

travis: test
