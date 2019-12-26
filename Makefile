install:
	pip3 install -r requirements.txt
git:
	git add .
	git commit 
	git push
prereq:
	pipreqs --force .
test:
	python3 -m unittest
coverage_test:
	coverage run -m unittest
	coverage report

git_heroku:
	git add .
	git commit 
	git push heroku master
.PHONY: test

#  do this in package dir
package_update:
	source env/bin/activate
	# change version in setup.py
	rm dist/*
	python3 setup.py bdist_wheel sdist
	twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*
	deactivate

# Create an virtual environment
# python3 -m venv env
# source env/bin/active
# deactivate