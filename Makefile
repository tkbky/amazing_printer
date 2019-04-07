init:
	pip install pipenv --upgrade
	pipenv install --dev

test:
	tox

ci:
	pipenv run pytest --junitxml=report.xml

coverage:
	pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=amazing_printer
