serve:
	mkdocs serve

deploy: 
	rm -r site
	marp  --input-dir docs/Articles --output site/Slides
	pipenv run mkdocs gh-deploy --dirty

install:
	pipenv install 

upgrade: update

update: 
	pipenv update

docbuild:
	mkdocs build -d static

start: docbuild
	uvicorn --port 5000 --host 127.0.0.1 app.main:app --reload