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