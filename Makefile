.PHONY: test clean install travis release docs

clean:
	git clean -Xfd

install:
	pip install --requirement=requirements/tests.txt

test:
	flake8 --ignore=W801,E128,E501,W402 localflavor
	coverage run `which django-admin.py` test --settings=tests.settings tests
	coverage report

travis: test

release:
	python setup.py sdist bdist_wheel register upload -s

docs:
	cd docs; make html; cd ..
