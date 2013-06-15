clean:
	git clean -Xfd

install:
	pip install --requirement=requirements/tests.txt
	echo "ATTENTION: you need to install a Django version, too!"

test:
	flake8 --ignore=W801,E128,E501,W402 localflavor
	coverage run `which django-admin.py` test --settings=tests.settings tests
	coverage report

travis: test
