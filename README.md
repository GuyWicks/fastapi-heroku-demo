# Fast API - Heroku demo

> Sadly, Heroku have withdrawn their free-tier layer (Nov 2022) so the live-demos no longer work.

Simple OAuth2 API implementation using Heroku to host, based on [OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

username: `johndoe`  
password: `secret`  

- [GitHub Pages](https://guywicks.github.io/fastapi-heroku-demo/)
- [Swagger Doc](https://fastapi-heroku-demo.herokuapp.com/docs)
- [Live API hosting](https://fastapi-heroku-demo.herokuapp.com)


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

```
make start
```

http://127.0.0.0:5000
http://127.0.0.0:8000
