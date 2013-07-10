lang = all

clean:
	git clean -Xfd

install:
	pip install --requirement=requirements/tests.txt

test:
ifeq ($(lang),all)
	flake8 --ignore=W801,E128,E501,W402 localflavor
	coverage run `which django-admin.py` test --settings=tests.settings tests
	coverage report
else ifeq "$(wildcard localflavor/$(lang))" ""
	@echo 'This language is not supported yet.'
else
	flake8 localflavor/$(lang)
	coverage run `which django-admin.py` test --settings=tests.settings tests.test_$(lang)
	coverage report -m --include=localflavor/$(lang)/*
endif

travis: test
