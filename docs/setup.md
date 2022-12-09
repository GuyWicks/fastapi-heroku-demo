## Setup and Dependencies

```
python -m virtualenv venv
(activate)
pip install fastapi uvicorn python-jose 
pip install "passlib[bcrypt]" python-multipart
pip install mkdocs mkdocs-material
pip install gunicorn
```

## Local usage

I've created a very basic `Makefile`

## Start the uvicorn / FastAPI service
```
make start
```

## Start the mkdocs server
```
make serve
```


- [http://127.0.0.0:5000](http://127.0.0.0:5000)
- [http://127.0.0.0:8000](http://127.0.0.0:8000)
