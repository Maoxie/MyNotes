# MyNotes

Based on MkDocs to build markdown files as docs pages.

## 1. Requirements

Python
MkDocs
pymdown-extensions==8.0.1

## 2. Install

```bash
python -m pip install -r requirements.txt

# clone the notes repository and rename it as docs
git clone git@github.com/xxxxxx/Notes.git
mv Notes docs
```

```bash
# build
python -m mkdocs build
# or serve for test
# python -m mkdocs serve
```

## 3. Run

Before run, make sure the nginx be configured correctly.

Refer to `deploy/nginx_conf/example.conf`

Create a `.env` file, append the token such as:

```bash
export MY_NOTES_TOKEN="your_secret_token"
```

Run the listener:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8008 --env-file .env
# or run at background
nohup uvicorn app.main:app --host 0.0.0.0 --port 8008 --env-file .env &> logs/app.log &
```