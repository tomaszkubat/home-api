# home-api
My test project to learn FastAPI possibilities.

- [Setup](#setup)
- [Run](#run)

# Setup

Bellows the `Windows` commands presented.

Create `virtualenv`:

```commandline
python -m venv .venv
```
Activate `virtualenv`:

```commandline
.\.venv\Scripts\activate
```

Install requirements from `requirements.txt`:

```commandline
pip install -r .\requirements.txt
```

Install `dev` requirements from `requirements.txt`:

```commandline
pip install -r .\requirements-dev.txt
```

# Run

To run the app locally in the `reload` mode: 

```commandline
cd .\src\
uvicorn app.main:app --reload
```
